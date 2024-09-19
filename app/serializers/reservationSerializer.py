from collections import defaultdict

from django.db.models import Q
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from app.models import Reservation
from app.models.reservation import ReservationStatus


class ReservationSerializer(serializers.ModelSerializer):
    status_desc = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Reservation
        fields = ('id', 'user_id', 'start_date', 'end_date', 'participants', 'status', 'status_desc',
                  'created_at', 'updated_at',)
        read_only_fields = ('status',)

    def to_internal_value(self, data: dict):
        return {**data, 'user': self.context['request'].user}

    def validate(self, attrs):
        start_date = attrs.get('start_date')
        end_date = attrs.get('end_date')
        participants = attrs.get('participants')
        if participants > Reservation.MAX_PARTICIPANTS:
            raise ValidationError({'participants': f'응시 인원은 최대 {Reservation.MAX_PARTICIPANTS}명까지 가능합니다.'})

        # 예약 시간과 응시 인원 검증
        reservations = Reservation.objects.filter(
            Q(status=ReservationStatus.CONFIRMED),
            Q(start_date__gte=start_date, start_date__lt=end_date) |
            Q(end_date__gt=start_date, end_date__lte=end_date)
        )
        reservation_dict = defaultdict(int)
        for r in reservations:
            reservation_dict[r.start_date] += r.participants
            reservation_dict[r.end_date] -= r.participants

        total_participants = 0
        min_participants = Reservation.MAX_PARTICIPANTS
        for k in sorted(reservation_dict.keys()):
            total_participants += reservation_dict[k]
            if total_participants + participants > Reservation.MAX_PARTICIPANTS:
                available_participants = Reservation.MAX_PARTICIPANTS - total_participants
                min_participants = min(min_participants, available_participants)
        if min_participants != Reservation.MAX_PARTICIPANTS:
            if min_participants <= 0:
                raise ValidationError({'participants': f'해당 시간대에는 예약이 불가합니다.'})
            else:
                raise ValidationError({'participants': f'해당 시간대에 {min_participants}명 이하까지만 예약 가능합니다.'})
        return super().validate(attrs)

    def update(self, instance, validated_data):
        # 확정된 건은 수정 불가
        if instance.status == ReservationStatus.CONFIRMED:
            raise ValidationError({'status': f'이미 확정된 예약은 수정이 불가합니다.'})
        return super().update(instance, validated_data)
