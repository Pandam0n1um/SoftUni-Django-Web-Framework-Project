from django.contrib import admin
# Register your models here.
from django.contrib.auth.admin import UserAdmin

from django_final_project.authentication.models import Profile, ClimbingGuideUser


#
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'user_id',)
    # readonly_fields = ('user_id',)


@admin.register(ClimbingGuideUser)
class ClimbingGuideAdmin(UserAdmin):
    list_display = ('email', 'is_staff', 'is_active', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'groups')
    ordering = ('email','is_staff','is_superuser')
    search_fields = ('email', 'phone_number')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {
            'fields': ('is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions'),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    readonly_fields = ('date_joined', 'last_login')
