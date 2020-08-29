from django.contrib import admin
from .models import Course, CourseEnrollment, CourseModule, Section, Unit


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', )
    prepopulated_fields = {"slug": ("title",)}


# admin.site.register(Course, CourseAdmin)
admin.site.register(CourseEnrollment)
admin.site.register(CourseModule)
admin.site.register(Section)
admin.site.register(Unit)