from django.contrib import admin
from .models import Task
import sys

reload(sys)
sys.setdefaultencoding('UTF8')
# Register your models here.


class TaskAdmin(admin.ModelAdmin):
	# customize change list 
	list_display = ('context', 'status', 'pub_date')
	search_fields = ['context']
	list_filter = ['pub_date']
	fieldsets = [
		('Content' , {'fields' : ['context', 'status']}),
		('DeadLine', {'fields' : ['deadline']}),
		('Date information: ' , {'fields' : ['pub_date']}),
	]
# register form admin 
admin.site.register(Task, TaskAdmin)