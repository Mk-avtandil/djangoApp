from django.db import models

GENDER = (('Man', 'Man'), ('Women', 'Women'))


class Marvel(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255)
    ability = models.CharField(max_length=255)
    gender = models.CharField(choices=GENDER, max_length=6)
    about = models.TextField()
    photo = models.ImageField(upload_to="%Y/%m/%d/",)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
