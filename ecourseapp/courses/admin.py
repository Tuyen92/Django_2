from django.contrib import admin
from .models import Category, Courses


class CoursesAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'create_date', 'active']
    search_fields = ['subject']
    list_filter = ['id', 'subject', 'create_date']


admin.site.register(Category)
admin.site.register(Courses, CoursesAdmin)
