from django.db import models

# Create your models here.

class FoundMovie(models.Model):
    movie_name = models.CharField(max_length=24,unique=True)
    movie_overview = models.CharField(max_length=264,unique=True)
    movie_id = models.IntegerField(unique=True)
    movie_release_date = models.IntegerField(unique=True)

    def __str__(self):
        return self.movie_name, self.movie_overview, self.movie_release_date, self.movie_id
