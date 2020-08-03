from django.db import models

# Create your models here.

class Project(models.Model):
    image = models.ImageField(upload_to='photos/site_images', null=True)
    name = models.CharField(max_length=10)
    projLink = models.URLField(max_length=128, db_index=True, unique=True, blank=False)
    repoLink = models.URLField(max_length=128, unique=True, blank=False)


    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
    
    def __str__(self):
        return self.name

    
    @classmethod
    def get_images(cls):
        images = Image.objects.all()
        return images

        return Image.objects.all()