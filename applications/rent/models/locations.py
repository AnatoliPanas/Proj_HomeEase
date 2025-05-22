from django.db import models


class Address(models.Model):
    country = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    street = models.CharField(max_length=128)
    house_number = models.CharField(max_length=16, blank=True, null=True)
    apartment_number = models.CharField(max_length=16, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'address'
        constraints = [
            models.UniqueConstraint(fields=[
                'country',
                'city',
                'street',
                'apartment_number'
            ],
                name='unique_address_with_apartment')
        ]

    def __str__(self):
        parts = [self.city, self.street, self.house_number]
        return ', '.join(filter(None, parts))
