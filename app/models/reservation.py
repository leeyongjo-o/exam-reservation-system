from django.core.validators import MaxValueValidator
from django.db import models

from app.models import User


class ReservationStatus(models.IntegerChoices):
    WAITING = 0, '대기중'
    CONFIRMED = 1, '확정됨'


class Reservation(models.Model):
    id = models.BigAutoField('예약 고유번호', primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')

    MAX_DIFF_DAYS_START_DATE_FROM_NOW = 3  # days
    start_date = models.DateTimeField('시험 시작일시')
    end_date = models.DateTimeField('시험 종료일시')

    MAX_PARTICIPANTS = 50_000
    participants = models.PositiveIntegerField('응시인원',
                                               validators=[MaxValueValidator(MAX_PARTICIPANTS)])

    status = models.IntegerField('예약 상태', choices=ReservationStatus.choices, default=ReservationStatus.WAITING)

    created_at = models.DateTimeField('등록일시', auto_now_add=True)
    updated_at = models.DateTimeField('수정일시', auto_now=True)

    class Meta:
        db_table = "reservation"
        indexes = (
            models.Index(fields=['start_date', 'end_date']),
            models.Index(fields=['created_at']),
            models.Index(fields=['updated_at']),
        )
