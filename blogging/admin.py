from django.contrib import admin
from blogging.models import Post, Category

class CategoryInline(admin.TabularInline):
    model = Category.posts.through
    extra = 0

class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInline]

class CategoryAdmin(admin.ModelAdmin):
    exclude = ['posts']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)