from django.db import models

# Create your models here.


class Summary(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)

    class Meta:
        verbose_name = "Summary"
        verbose_name_plural = "Summary"

    def __str__(self):
        return "{0}".format(self.title)


class Contact(models.Model):
    address = models.CharField(max_length=250)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contact"

    def __str__(self):
        return self.email
