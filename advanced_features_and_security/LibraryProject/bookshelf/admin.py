from django.contrib import admin
from .models import Book
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class BookAdmin(admin.ModelAdmin):
    class BookAdmin(admin.ModelAdmin):
        list_display = ('title', 'author', 'publication_year')
        search_fields = ('title', 'author')
        list_filter = ('author', 'publication_year')

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)