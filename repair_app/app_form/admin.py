from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import User, Request, Comment


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = DjangoUserAdmin.fieldsets + (
        ('Дополнительные данные', {'fields': ('fio', 'phone', 'role')}),
    )
    list_display = ('username', 'fio', 'role', 'phone', 'is_staff', 'is_superuser')
    list_filter = ('role', 'is_staff', 'is_superuser')


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('request_id', 'climate_tech_type', 'request_status', 'client', 'master', 'start_date')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment_id', 'request', 'master', 'created_at')
