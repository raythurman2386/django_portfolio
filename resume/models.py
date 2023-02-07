from django.db import models


class Summary(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)

    class Meta:
        verbose_name = 'Summary'
        verbose_name_plural = 'Summary'

    def __str__(self):
        return '{0}'.format(self.title)


class Projects(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)

    class Meta:
        verbose_name = 'Projects'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return '{0}'.format(self.title)


class Employment(models.Model):
    title = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.CharField(max_length=1000)

    class Meta:
        verbose_name = 'Employment'
        verbose_name_plural = 'Employment'

    def __str__(self):
        return '{0}'.format(self.title)


class Education(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        verbose_name = 'Education'
        verbose_name_plural = 'Education'

    def __str__(self):
        return '{0}'.format(self.title)


class Skill(models.Model):
    skill = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.skill


class Contact(models.Model):
    address = models.CharField(max_length=250)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'

    def __str__(self):
        return self.email
