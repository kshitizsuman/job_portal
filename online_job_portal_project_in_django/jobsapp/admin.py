from django.contrib import admin

# Register your models here.

from jobsapp.models import Job, Applicant

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    pass

@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    pass
