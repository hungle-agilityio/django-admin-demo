from django.contrib import admin
from core.models import Sauce, Sandwich

class SauceAdmin(admin.ModelAdmin):
    pass

class SandwichAdmin(admin.ModelAdmin):
    pass

admin.site.register(Sauce, SauceAdmin)
admin.site.register(Sandwich, SandwichAdmin)