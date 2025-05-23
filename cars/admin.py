from django.contrib import admin

from .models import Brand, Car


class BrandAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "brand", "factory_year", "model_year", "value")


admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)
