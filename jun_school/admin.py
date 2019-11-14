from django.contrib import admin
from .models import Subject, TheClass, Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('student', 'the_class')

admin.site.register(Subject)
admin.site.register(TheClass)
admin.site.register(Student, StudentAdmin)

