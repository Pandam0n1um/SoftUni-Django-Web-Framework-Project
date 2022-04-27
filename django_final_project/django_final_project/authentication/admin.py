from django.contrib import admin

# Register your models here.
from django_final_project.authentication.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # inlines = (PetInlineAdmin,)
    list_display = ('first_name', 'last_name')