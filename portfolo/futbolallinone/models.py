from django.db import models

# Create your models here.
class bund(models.Model):
    Rank = models.IntegerField(primary_key=True)
    Team = models.CharField(max_length=50)
    Pl = models.IntegerField()
    W = models.IntegerField()
    D = models.IntegerField()
    L = models.IntegerField()
    F = models.IntegerField()
    A = models.IntegerField()
    GD = models.IntegerField()
    Pts = models.IntegerField()

    class Meta:
        db_table = 'bund'

    def __str__(self):
        return self.Team


class epl(models.Model):
    Rank = models.IntegerField(primary_key=True)
    Team = models.CharField(max_length=50)
    Pl = models.IntegerField()
    W = models.IntegerField()
    D = models.IntegerField()
    L = models.IntegerField()
    F = models.IntegerField()
    A = models.IntegerField()
    GD = models.IntegerField()
    Pts = models.IntegerField()

    class Meta:
        db_table = 'epl'

    def __str__(self):
        return self.Team

class liga(models.Model):
    Rank = models.IntegerField(primary_key=True)
    Team = models.CharField(max_length=50)
    Pl = models.IntegerField()
    W = models.IntegerField()
    D = models.IntegerField()
    L = models.IntegerField()
    F = models.IntegerField()
    A = models.IntegerField()
    GD = models.IntegerField()
    Pts = models.IntegerField()

    class Meta:
        db_table = 'liga'

    def __str__(self):
        return self.Team
        
class ligue(models.Model):
    Rank = models.IntegerField(primary_key=True)
    Team = models.CharField(max_length=50)
    Pl = models.IntegerField()
    W = models.IntegerField()
    D = models.IntegerField()
    L = models.IntegerField()
    F = models.IntegerField()
    A = models.IntegerField()
    GD = models.IntegerField()
    Pts = models.IntegerField()

    class Meta:
        db_table = 'ligue'

    def __str__(self):
        return self.Team

class serie(models.Model):
    Rank = models.IntegerField(primary_key=True)
    Team = models.CharField(max_length=50)
    Pl = models.IntegerField()
    W = models.IntegerField()
    D = models.IntegerField()
    L = models.IntegerField()
    F = models.IntegerField()
    A = models.IntegerField()
    GD = models.IntegerField()
    Pts = models.IntegerField()

    class Meta:
        db_table = 'serie'

    def __str__(self):
        return self.Team
