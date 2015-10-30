from django.contrib import admin
from .models import Member, Equipment
# Register your models here.


class EquipInLine(admin.StackedInline):
	model = Equipment
	extra = 4
	# fields = ['name', 'amount']
	fields = ['name', 'amount', 'size', 'detail', 'address']

class MemberAdmin(admin.ModelAdmin):
	fields = ['user', 'nick_name', 'year', 'student_id']
	inlines = [EquipInLine]


admin.site.register(Member, MemberAdmin),
admin.site.register(Equipment),
