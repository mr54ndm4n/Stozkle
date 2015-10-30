from django.conf import settings
from django.db import models

# Create your models here.
class Member(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	nick_name = models.CharField(max_length=20)
	year = models.PositiveSmallIntegerField(default=0)
	student_id = models.PositiveSmallIntegerField(default=0)
	def __str__(self):
		return self.nick_name


class Equipment(models.Model):
	member = models.ForeignKey(Member)
	name = models.CharField(max_length=80)
	size = models.CharField(max_length=30, blank=True)
	amount = models.PositiveSmallIntegerField(default=0)
	detail = models.TextField(blank=True, default='None')
	address = models.TextField(blank=True, default='None')
	def __str__(self):
		return self.name
