from django.db import models

# Create your models here.

import datetime


class Country(models.Model):
    name = models.CharField('название', max_length=25)

    class Meta:
        verbose_name = 'страна'
        verbose_name_plural = 'страны'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField('название', max_length=25)
    country = models.ForeignKey(
        'Country',
        on_delete=models.CASCADE,
        verbose_name='страна производитель',
        related_name='manufacturer_set',
        )

    class Meta:
        verbose_name='производитель'
        verbose_name_plural='производители'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    name = models.CharField('наименование', max_length=20)
    manufacturer = models.ForeignKey(
        'Manufacturer',
        on_delete=models.CASCADE,
        verbose_name='производитель'
        )
    start_year = models.IntegerField('год начала выпуска')
    end_year = models.IntegerField('год окончания выпуска')

    class Meta:
        verbose_name='автомобиль'
        verbose_name_plural='автомобили'

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Comment(models.Model):
    author_email = models.CharField('e-mail автора', max_length=20)
    vehicle = models.ForeignKey(
        'Vehicle',
        on_delete=models.CASCADE,
        verbose_name='автомобиль'
        )
    post_date = models.DateField('дата создания', default=datetime.date.today)
    text = models.CharField('текст комментария', max_length=255)

    class Meta:
        verbose_name='комментарий'
        verbose_name_plural='комментарии'

    def __unicode__(self):
        return ' | '.join((self.name, post_date))

    def __str__(self):
        return ' | '.join((self.name, post_date))