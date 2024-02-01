from django.contrib import admin
from .models import Category, Product, Subcategory, ProductPhotos

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title']
#     list_display_links = ['title', ]


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'title']
    list_display_links = ['title', ]
    list_filter = ['category', ]
    search_fields = ['title']

class SubcategoryStacked(admin.StackedInline):
    model = Subcategory # дочерний блок
    extra = 0
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubcategoryStacked]
    class Meta:
        model = Category # родитель

@admin.register(ProductPhotos)
class ProductPhotosAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo']
    list_display_links = ['photo',]
    

class ProductPhotosStacked(admin.StackedInline):
    model = ProductPhotos
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductPhotosStacked]
    list_display = ['id', 'subcategory', 'title', 'price']
    list_display_links = ['subcategory', 'title', ]    
    raw_id_fields = ['subcategory',]
    class Meta:
        model = Product