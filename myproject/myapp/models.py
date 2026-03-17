from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField()
    rating = models.FloatField()
    cuisine = models.CharField(max_length=100)
    delivery_time = models.IntegerField(default=30)

    def __str__(self):
        return self.name


class Food(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.URLField(blank=True, null=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name