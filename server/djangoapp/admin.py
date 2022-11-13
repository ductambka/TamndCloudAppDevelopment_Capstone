from django.contrib import admin
from .models import CarMake, CarModel


# Register your models here.

# CarModelInline class

class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 4


# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    # inlines = [CarModelInline]
    list_display = ('name', 'type', 'year')
    list_filter = ['name', 'type', 'year']
    search_fields = ['name', 'type', 'year']


admin.site.register(CarModel, CarModelAdmin)

# CarMakeAdmin class with CarModelInline

admin.site.register(CarMake)
