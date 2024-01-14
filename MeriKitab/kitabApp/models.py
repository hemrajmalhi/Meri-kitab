from django.db import models


# from django.utils.text import slugify


# Create your models here


class SellBook1(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    category = models.CharField(max_length=50)
    authorName = models.CharField(max_length=50, default="", blank=True)
    setprice = models.IntegerField(blank=True, null=True)
    image1 = models.ImageField(upload_to='book_images/', blank=True)
    image2 = models.ImageField(upload_to='book_images/', blank=True)
    image3 = models.ImageField(upload_to='book_images/', blank=True)
    image4 = models.ImageField(upload_to='book_images/', blank=True)
    name = models.TextField(max_length=50, blank=True)
    phone = models.CharField(max_length=500, blank=True)
    address = models.CharField(max_length=255, blank=True)

    # slug = models.CharField(max_length=100)

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         # Generate the slug from the title
    #         self.slug = slugify(self.title)
    #     super(SellBook1, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
