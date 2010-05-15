from django.contrib import admin
from ootd.students.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'student_of_the_month')

admin.site.register(Student, StudentAdmin)

