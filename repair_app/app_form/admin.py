from django.contrib import admin
from .models import User, Request, Comment

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'fio', 'phone', 'role', 'login']
    list_filter = ['role']
    search_fields = ['fio', 'login']

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ['request_id', 'climate_tech_type', 'client', 'master', 'request_status', 'start_date']
    list_filter = ['request_status', 'climate_tech_type', 'start_date']
    search_fields = ['climate_tech_model', 'problem_description']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment_id', 'request', 'master', 'message', 'created_at']
    list_filter = ['created_at']

