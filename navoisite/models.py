from django.db import models
# from ckeditor_uploader.fields import RichTextUploadingField



class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    description = models.TextField()
    subjact = models.TextField()

    def __str__(self):
        return self.first_name
    

# from django.db import models
from ckeditor.fields import RichTextField

class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)  # Uniqlikni ta'minlash uchun
    content = RichTextField()  # RichTextField yoki qaysi ma'lumotlar turini ishlatmoqchisiz
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
    main_image = models.ImageField(upload_to="Articles/photo")

    def __str__(self):
        return self.title
    

class Elon(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = RichTextField() 
    # hozir_vaqt = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="Elons/photo")
    description =  models.TextField()




