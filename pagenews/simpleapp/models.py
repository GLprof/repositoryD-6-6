from django.db import models
from django.core.validators import MinValueValidator
from datetime import datetime


class News(models.Model):
    title_news = models.CharField(max_length=64, unique=True, )
    description_news = models.TextField()
    text_news = models.TextField()
    quantity = models.IntegerField(validators=[MinValueValidator(0)], )
    category_news = models.ForeignKey(to='Category', on_delete=models.CASCADE,
                                      related_name='news', )
    cost_news = models.FloatField(validators=[MinValueValidator(0.0)], )
    datetime_news = models.DateTimeField(auto_now_add=True, )


    def __str__(self):
        return f'{self.title_news.title()}: {self.description_news[:64]}: {self.text_news}'


class Category(models.Model):
    category_name = models.CharField(max_length=64, unique=True, )

    def __str__(self):
        return self.category_name.title()
