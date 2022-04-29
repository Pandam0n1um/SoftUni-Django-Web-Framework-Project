from django.contrib import admin

# Register your models here.
from django_final_project.climbing_guide.models import ClimbingTrip, ClimbingLocation


@admin.register(ClimbingTrip)
class ClimbingGuideAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'start_date',
        'end_date',
        'application_deadline_date',
        'trip_cost',
        'trip_description',
        'trip_capacity',
        'trip_location',
    )


@admin.register(ClimbingLocation)
class ClimbingGuideAdmin(admin.ModelAdmin):
    list_display = ('name', 'rock_type', 'climbing_type')
