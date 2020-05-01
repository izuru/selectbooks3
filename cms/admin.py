from django.contrib import admin
from cms.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'ISBN', 'title', 'creator', 'publisher', 'date', 'NDC')  # 一覧に出したい項目
    list_display_links = ('id', 'title',)  # 修正リンクでクリックできる項目

admin.site.register(Book, BookAdmin)