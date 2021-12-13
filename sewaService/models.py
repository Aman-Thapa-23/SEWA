from django.db import models
from PIL import Image

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return f'{self.title} Category'


class Services(models.Model):
    title = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    details = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='service_pics') 

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     super(Services, self).save(*args, **kwargs)
    #     img = Image.open(self.image.path)

    #     if img.height > 400 or img.width >300:
    #         output_size = (400, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)