from django.contrib import admin

from .models import Contact,NewsArticle


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["first_name", "email","subjact"]


class NewArticleAdmin(admin.ModelAdmin):
    list_display = ('title','author','published_date','short_content')

    def short_content(self, obj):
        return obj.content[:50]
    short_content.short_description = 'Content'

admin.site.register(NewsArticle, NewArticleAdmin)


    

