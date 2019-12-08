from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.Job)
admin.site.register(models.Company)
admin.site.register(models.Manager)
admin.site.register(models.Employee)
admin.site.register(models.Workplace)
admin.site.register(models.WorkTime)