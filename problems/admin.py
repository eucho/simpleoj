from django.contrib import admin
from problems.models import Problem, Submission

class ProblemAdmin(admin.ModelAdmin):
	fields = ['title', 'description', 'time_limit']
	list_display = ['title', 'time_limit']

admin.site.register(Problem, ProblemAdmin)
admin.site.register(Submission)
