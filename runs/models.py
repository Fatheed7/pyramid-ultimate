from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField(blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    external_link = models.URLField()
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name

class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PrimaryChallenge(models.Model):
    name = models.CharField(max_length=100)
    additional_info = models.TextField(blank=True)
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name

class SecondaryChallenge(models.Model):
    name = models.CharField(max_length=100)
    additional_info = models.TextField(blank=True)
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return self.name