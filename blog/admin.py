from django.contrib import admin # type: ignore

from blog.models import Product, Attribute, Image,Customer

# Register your models here.


admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Attribute)
admin.site.register(Customer)

