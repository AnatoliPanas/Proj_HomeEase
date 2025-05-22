from django.db import models
from django.utils import timezone

from applications.rent.choices.room_type import RoomType
from applications.rent.managers.rent import SoftDeleteManager
from applications.rent.models.locations import Address
from applications.users.models.user import User


class Rent(models.Model):
    title = models.CharField(max_length=90)
    description = models.TextField()
    address = models.ForeignKey(
        Address,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='rents'
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rooms_count = models.PositiveSmallIntegerField(default=0)
    room_type = models.CharField(max_length=34, choices=RoomType.choices())
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    owner = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='rents'
    )

    objects = SoftDeleteManager()

    def delete(self, *arg, **kwargs):
        self.is_deleted = True
        self.deleted_at = timezone.now()

        self.save()

    class Meta:
        db_table = "rent"

    def __str__(self):
        return self.title
