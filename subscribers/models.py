from django.db import models


class Subscribers(models.Model):
    """A subscriber model."""

    email = models.CharField(max_length=100, blank=False, null=False, help_text='Email address')
    full_name = models.CharField(max_length=100, blank=False, null=False, help_text='First and last name')

    def __str__(self):
        """Str repr of this object."""
        return self.full_name

    class Meta:  # noqa
        verbose_name = "Susbcriber"
        verbose_name_plural = "Subscribers"
