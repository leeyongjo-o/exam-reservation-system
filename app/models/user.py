from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, **data):
        data['username'] = User.normalize_username(data.get('username'))
        password = data.pop('password')
        user = User(**data)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_admin(self, **data):
        data.setdefault('is_admin', True)
        return self.create_user(**data)

    def create_superuser(self, **data):
        data.setdefault('is_admin', True)
        data.setdefault('is_superuser', True)
        return self.create_user(**data)


class User(AbstractUser):
    id = models.BigAutoField('유저 고유번호', primary_key=True)
    name = models.CharField('유저 이름', max_length=255)
    is_admin = models.BooleanField(
        "어드민 여부",
        default=False,
        help_text="Designates whether the user can log into this admin site.",
    )
    created_at = models.DateTimeField('등록일시', auto_now_add=True)
    updated_at = models.DateTimeField('수정일시', auto_now=True)

    class Meta:
        db_table = "user"
        indexes = (
            models.Index(fields=['name']),
            models.Index(fields=['created_at']),
            models.Index(fields=['updated_at']),
        )

    objects = UserManager()
    email = None
    first_name = None
    last_name = None
    date_joined = None
    is_staff = None

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']
