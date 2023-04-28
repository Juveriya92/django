from django.db import models
from django_matplotlib import MatplotlibFigureField


# Create your models here.
class Plotting(models.Model):
    figure=MatplotlibFigureField(figure="my_fig")