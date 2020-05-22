from django.conf import settings
from django.db import models


class UserMixin(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        null=False, blank=False,
        verbose_name="User",
        help_text="",
    )

    class Meta:
        abstract = True


class Category(UserMixin, models.Model):
    name = models.CharField(
        max_length=50,
        null=False, blank=False,
        verbose_name="Name",
        help_text="",
    )
    slug = models.SlugField()
    description = models.CharField(
        max_lenght=150,
        null=False, blank=True, default="",
        verbose_name="Description",
        help_text="",
    )
    image_url = models.URLField(
        verbose_name="Image URL",
        help_text="",
    )


class Plant(UserMixin, models.Model):
    name = models.CharField(
        max_length=50,
        null=False, blank=False,
        verbose_name="Name",
        help_text="",
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        null=False, blank=False,
        verbose_name="Category",
        help_text="",
    )

    watering_interval = models.PositiveIntegerField(
        null=False, blank=False,
        verbose_name="Watering interval",
        help_text="In seconds",
    )

    fertilizing_interval = models.PositiveIntegerField(
        null=False, blank=False,
        verbose_name="Fertilizing interval",
        help_text="In seconds",
    )

    EXPOSURE_CHOICES = [
        ("dark", "Dark"),
        ("shade", "Shade"),
        ("partsun", "Part sun"),
        ("fullsun", "Full sun"),
    ]

    required_exposure = models.CharField(
        max_length=10, choices=EXPOSURE_CHOICES,
        null=False, blank=False,
        verbose_name="Amount of sun",
        help_text="",
    )
    HUMIDITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    ]

    required_humidity = models.CharField(
        max_length=10, choices=HUMIDITY_CHOICES,
        null=False, blank=False,
        verbose_name="Humidity",
        help_text="",
    )
    TEMPERATURE_CHOICES = [
        ("cold", "Cold"),
        ("medium", "Medium"),
        ("warm", "Warm"),
    ]
    required_temperature = models.CharField(
        max_length=10, choices=TEMPERATURE_CHOICES,
        null=False, blank=False,
        verbose_name="Temperature",
        help_text="",
    )

    blooming = models.BooleanField(
        default=False,
        null=False, blank=True,
        verbose_name="Blooming?",
    )
    DIFFICULTY_CHOICES = [
        (1, "Low"),
        (2, "Medium-low"),
        (3, "Medium"),
        (4, "Medium-high"),
        (5, "high"),
    ]
    difficulty = models.PositiveIntegerField(
        choices=DIFFICULTY_CHOICES,
        null=False, blank=False, default=1,
        verbose_name="Cultivation difficulty level",
        help_text="",
    )


class Room(UserMixin, models.Model):
    name = models.CharField(
        max_length=50,
        null=False, blank=False,
        verbose_name="Room Name",
        help_text="",
    )


INSOLATION_CHOICES = [
    ("dark", "Dark"),
    ("shade", "Shade"),
    ("partsun", "Part sun"),
    ("fullsun", "Full sun"),
]

required_exposure = models.CharField(
    max_length=10, choices=INSOLATION_CHOICES,
    null=False, blank=False,
    verbose_name="Room insolation",
    help_text="",
)
ROOM_HUMIDITY_CHOICES = [
    ("low", "Low"),
    ("medium", "Medium"),
    ("high", "High"),
]

required_humidity = models.CharField(
    max_length=10, choices=ROOM_HUMIDITY_CHOICES,
    null=False, blank=False,
    verbose_name="Room humidity",
    help_text="",
)

ROOM_TEMPERATURE_CHOICES = [
    ("cold", "Cold"),
    ("medium", "Medium"),
    ("warm", "Warm"),
]

required_temperature = models.CharField(
    max_length=10, choices=ROOM_TEMPERATURE_CHOICES,
    null=False, blank=False,
    verbose_name="Room temperature",
    help_text="",
)

draft = models.BooleanField(
    default=False,
    null=False, blank=True,
    verbose_name="Blooming?",
)


class UserPlant(UserMixin, models.Model):
    name = models.CharField(
        max_length=50,
        null=False, blank=False,
        verbose_name="Name",
        help_text="",
    )

    description = models.ForeignKey(
        max_length=200,
        null=False, blank=False,
        verbose_name="Description",
        help_text="",
    )

    room = models.ForeignKey(
        Room,
        on_delete=models.PROTECT
    )

    plant = models.ForeignKey(
        Plant,
        on_delete=models.PROTECT
    )
    watering = models.DateTimeField(

    )
    fertilizing = models.DateTimeField(

    )
