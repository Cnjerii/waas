from django.db import models

# Create your models here.
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
	# role = models.ForeignKey(Role, models.DO_NOTHING, blank=True, null=True)
	password_changed = models.IntegerField(default=0)
	is_self_registered = models.IntegerField(default=1)

	class Meta:
		# managed = False
		db_table = 'user'

class VerificationCode(models.Model):
	mobile_number = models.CharField(max_length=17)
	otp = models.CharField(max_length=9)
	validated = models.BooleanField(default=False)

	def __str__(self):
		return f'{self.mobile_number}-{self.otp}'

	class Meta:
		# managed = False
		db_table = 'verification_code'







