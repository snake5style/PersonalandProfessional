from django.db import models

# Create your models here.
# Model called Professional with fields
class Professional(models.Model):
    proid = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    proemail = models.EmailField()
    procontact = models.CharField(max_length=15)

    # create meta class
    class Meta:
        db_table = "professional"
