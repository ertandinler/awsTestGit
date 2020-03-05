from django.contrib import admin
from .models import Post

#oluşturduğumuz Post modelinin admin panelinde görünmesini sağlar


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'publishing_date', 'slug'] #Yayımlanma Tarihi de görünür.
    list_display_links = ['publishing_date'] # Yayımlanma tarihine link verir.
    list_filter = ['publishing_date'] # tarihe göre filtreleme yapar
    search_fields = ['title', 'content'] # arama çubuğu getirir belirtilen alanlarda arama yapmamızı sağlar.
    list_editable = ['title']

    class Meta:

        model = Post
admin.site.register(Post, PostAdmin)
