from django.contrib import admin

# Register your models here.
from wash.models import Car, Location,washingPlace,washing

admin.site.register([Car],admin.ModelAdmin)
admin.site.register([Location],admin.ModelAdmin)
admin.site.register([washingPlace],admin.ModelAdmin)
admin.site.register([washing],admin.ModelAdmin)