from rest_framework.exceptions import ValidationError

from app.models import Reservation
from app.models.reservation import ReservationStatus
from app.serializers.reservationSerializer import ReservationSerializer


class ReservationConfirmSerializer(ReservationSerializer):
    class Meta:
        model = Reservation
        fields = ('id',)

    def to_internal_value(self, data: dict):
        return {**data, **self.instance.__dict__, 'status': ReservationStatus.CONFIRMED}

    def validate(self, attrs):
        if self.instance.status == ReservationStatus.CONFIRMED:
            raise ValidationError({'status': '이미 확정된 예약입니다.'})
        return super().validate(attrs)
