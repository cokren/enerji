from django.contrib import admin
from .models import Hatlar, Panolar

@admin.register(Hatlar)
class HatlarAdmin(admin.ModelAdmin):
    list_display = ["HAT_ADI","HAT_TIPI", "CAP", "UZUNLUK", "USER"]
    search_fields = ["HAT_ADI","HAT_TIPI", "CAP", "UZUNLUK", "USER"]
    list_filter = ["HAT_ADI", "HAT_TIPI", "CAP", "USER"]
    class Meta:
        model = Hatlar


@admin.register(Panolar)
class PanolarAdmin(admin.ModelAdmin):
    list_display = ["PANO_ADI","PANO_TIPI", "HAT", "MODEM","IP","KONUM", "USER"]
    search_fields = ["PANO_ADI","PANO_TIPI", "HAT", "MODEM","IP","KONUM", "USER"]
    list_filter = ["PANO_TIPI", "HAT", "MODEM", "USER"]
    class Meta:
        model = Panolar