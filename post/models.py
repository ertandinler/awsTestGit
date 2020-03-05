from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Yazar', related_name='posts')
    title = models.CharField(max_length=120, verbose_name='Başlık')
    content = RichTextField(verbose_name='İçerik')
    publishing_date = models.DateTimeField(verbose_name='Yayımlanma Tarihi', auto_now_add=True)
    #image = models.FileField(null=True, blank=True) # hertürlü dosya eklenebilir
    image = models.ImageField(null=True, blank=True) # sadece fotoğraflar eklenebilir
    slug = models.SlugField(unique=True, editable=False, max_length=130)

    def __str__(self):
        return self.title           #oluşturulan modelin başlığını admin panelinde göstermek için bir methot

    def get_absolute_url(self):
        return reverse("post:detay", kwargs={'slug': self.slug})         # url dosyasında post_detail fonksiyonu için kullanılan deyat sözcüğünü çözümler.
        #return "/post/{}".format(self.id)                      # 'id'  url dosyasında tanımlandı. self.id ilgili nesnenin id si (model)

    def get_create_url(self):
        return reverse("post:create")

    def get_update_url(self):
        return reverse("post:guncelle", kwargs={'slug': self.slug})

    def get_delete_url(self):
        return reverse("post:sil", kwargs={'slug': self.slug})

    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        #if not self.slug:                   # başlık değiştiğinde slug alanı da değişsin istiyorsak bu if koşulu kaldırılmalı
        self.slug = self.get_unique_slug()
        return super(Post, self).save(*args, **kwargs)
    class Meta:
        ordering = ['-publishing_date', 'id']

class Comment(models.Model):
    post = models.ForeignKey('post.Post', related_name='comments', on_delete=models.CASCADE)        # on_delete = models.CASCADE ile bir kayıt silindiğinde ona bağlı bütün kayıtlar silinir.
    name = models.CharField(max_length=200, verbose_name='İsim')
    content = models.TextField(verbose_name='Yorum')

    created_date = models.DateTimeField(auto_now_add=True)