from django.db import models


class Profile(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, null=False, blank=False)
    phone = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.full_name
