from rest_framework import serializers

from app.models import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    status_desc = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Reservation
        fields = ('id', 'user_id', 'start_date', 'end_date', 'participants', 'status', 'status_desc',
                  'created_at', 'updated_at',)
        read_only_fields = ('status',)

    def validate(self, attrs):
        # TODO: 예약 시간과 응시 인원 검증
        return super().validate(attrs)
