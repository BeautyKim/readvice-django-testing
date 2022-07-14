from django.db import models

class User(models.Model):
    use_in_migrations = True
    email = models.EmailField(max_length=128, primary_key=True, verbose_name="이메일")
    password = models.CharField(max_length=32, verbose_name="비밀번호")
    username = models.CharField(max_length=32, verbose_name="이름")
    birth = models.CharField(max_length=10, verbose_name="생일")
    gender = models.CharField(max_length=10, verbose_name="성별")

    class Meta:
        db_table = "users"
        verbose_name = '사용자'

    def __str__(self):
        return f'{self.pk} {self.email}'
    # verbose_name 옵션 : 관리자가 읽기 쉽게 화면에 표시