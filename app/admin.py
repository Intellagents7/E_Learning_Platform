from django.contrib import admin
from .models import Student, Course, Assignment

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'address')
    search_fields = ('first_name', 'last_name')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'instructor')
    search_fields = ('name', 'instructor')

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'description', 'deadline')
    list_filter = ('course',)
    search_fields = ('title', 'description')

