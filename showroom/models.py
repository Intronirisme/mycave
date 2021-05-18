from django.db import models
from .validators import noFuture #import validation function
from .countries import COUNTRY #a country list

# Create your models here.
class Wine(models.Model):
    id = models.AutoField(primary_key=True, serialize=False, auto_created=True, unique=True)
    name = models.CharField(max_length=255, null=False, unique=True)
    year = models.PositiveSmallIntegerField(validators=[noFuture])
    grapes = models.CharField(max_length=255, null=False)
    country = models.CharField(max_length=100, choices=COUNTRY)
    region = models.CharField(max_length=255, null=False)
    description = models.TextField(null=False)
    image = models.ImageField(upload_to='wines/')
    objects = models.Manager() #useless, just avoid VSCode warning

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Wine'
        verbose_name_plural = 'Wines'