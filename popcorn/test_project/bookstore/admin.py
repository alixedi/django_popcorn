from django.contrib import admin
from bookstore.models import Publisher, Author, Book

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Author, AuthorAdmin)

class PublisherAdmin(admin.ModelAdmin):
    pass
admin.site.register(Publisher, PublisherAdmin)

class BookAdmin(admin.ModelAdmin):
    pass
admin.site.register(Book, BookAdmin)

