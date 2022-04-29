from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.

UserModel = get_user_model()


class ClimbingTrip(models.Model):
    NAME_MAX_LENGTH = 50

    CAPACITY_MIN_VALUE = 0
    TRIP_COST_MIN_VALUE = 0

    name = models.TextField(
        max_length=NAME_MAX_LENGTH,
    )

    start_date = models.DateField(
        null=False,
        blank=False,
    )

    end_date = models.DateField(
        null=False,
        blank=False,
    )

    application_deadline_date = models.DateField(
        null=False,
        blank=False,
    )

    trip_cost = models.DecimalField(
        null=False,
        max_digits=6,
        decimal_places=2,
        validators=(
            MinValueValidator(TRIP_COST_MIN_VALUE),
        )
    )

    trip_description = models.TextField()

    trip_capacity = models.IntegerField(
        null=False,
        blank=False,
        validators=(MinValueValidator(CAPACITY_MIN_VALUE),)
    )

    trip_location = models.ForeignKey(
        'ClimbingLocation', on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )


class ClimbingLocation(models.Model):
    NAME_MAX_LENGTH = 40

    CONGLOMERATE = "Conglomerate"
    GNEISS = "Gneiss"
    GRANITE = "Granite"
    LIMESTONE = "Limestone"
    SANDSTONE = "Sandstone"
    OTHER = "Other"
    ROCK_TYPES = [(x, x) for x in (CONGLOMERATE, GNEISS, GRANITE, LIMESTONE, SANDSTONE, OTHER)]

    BOULDERING = "Bouldering"
    ICE_CLIMBING = "Ice Climbing"
    SPORT_CLIMBING = "Sport Climbing"
    TRAD_CLIMBING = "Trad Climbing"
    OTHER = "Other"

    CLIMBING_TYPES = [(x, x) for x in (BOULDERING, ICE_CLIMBING, SPORT_CLIMBING, TRAD_CLIMBING, OTHER)]

    GRADE_4A_4C = "4a-4c"
    GRADE_5A_5C_plus = "5a-5c+"
    GRADE_6A_6C_plus = "6a-6c+"
    GRADE_7A_7C_plus = "7a-7c+"
    GRADE_8A_8C_plus = "8a-8c+"
    GRADE_9A_plus = ">9a"

    CLIMBING_GRADES = [
        (x, x) for x in
        (GRADE_4A_4C, GRADE_5A_5C_plus, GRADE_6A_6C_plus, GRADE_7A_7C_plus, GRADE_8A_8C_plus, GRADE_9A_plus)
    ]

    name = models.TextField(
        max_length=NAME_MAX_LENGTH,
    )

    rock_type = models.CharField(
        max_length=max(len(x) for (x, _) in ROCK_TYPES),
        choices=ROCK_TYPES,
    )

    climbing_type = models.CharField(
        max_length=max(len(x) for (x, _) in CLIMBING_TYPES),
        choices=CLIMBING_TYPES,
    )

    # TODO Implement climbing grade field
    # Either with separate model and FK or with the help of Arrayfield for PostgreSQL
    # https://docs.djangoproject.com/en/dev/ref/contrib/postgres/fields/#arrayfield
    # climbing_grade=models.Arrayfield

    # TODO Implement country field to depict the destination of the Trip
    # Either use snippet with predefined countries or look for complete module
    # Possible solution - separate model with Countries and FK
    # country = models.CharField(
    #     max_length=2,
    #     choices=pytz.country_names.items())

    def __str__(self):
        return f"{self.name}"


class ClimbingTripApplication(models.Model):

    STATUS_MAX_LENGTH = 50

    PENDING = 'Pending'
    CONFIRMED = 'Confirmed'
    STATUS_OPTIONS = [(x, x) for x in (CONFIRMED, PENDING)]

    date_created = models.DateTimeField(
        auto_now_add=True,
        null=True,
    )

    status = models.CharField(
        max_length=STATUS_MAX_LENGTH,
        null=True,
        choices=STATUS_OPTIONS,
    )

    climbing_trip = models.ForeignKey(
        ClimbingTrip,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
