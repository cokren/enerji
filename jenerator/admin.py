from django.contrib import admin
from .models import Arizalar, FiltreliBakim, Jeneratorler, Tesisler, Periyodik, Personel

# Register your models here.
@admin.register(Tesisler)
class TesislerAdmin(admin.ModelAdmin):
    list_display = ["TESIS_ADI","TESIS_TIPI", "ILCE", "SCADA_KODU","USER"]
    search_fields = ["TESIS_ADI","TESIS_TIPI", "ILCE", "SCADA_KODU"]
    list_filter = ["TESIS_TIPI", "ILCE", "USER"]
    class Meta:
        model = Tesisler
    


@admin.register(Jeneratorler)
class JeneratorlerAdmin(admin.ModelAdmin):
    list_display = ["PLAKA","TESIS","MARKA","MODEL","USER"]
    search_fields = ["PLAKA","TESIS","MARKA","MODEL","USER"]
    list_filter = ["MARKA"]
    class Meta:
        model = Jeneratorler


@admin.register(Arizalar)
class ArizalarAdmin(admin.ModelAdmin):
    list_display = ["ARIZA_TIPI","JENERATOR","ARIZA_TARIHI","DEGISEN_PARCA","PERSONEL","USER"]
    search_fields = ["ARIZA_TIPI","JENERATOR","ARIZA_TARIHI","DEGISEN_PARCA","PERSONEL","USER"]
    list_filter = ["ARIZA_TIPI"]
    class Meta:
        model = Arizalar

@admin.register(FiltreliBakim)
class FiltreliBakimAdmin(admin.ModelAdmin):
    list_display = ["JENERATOR","FBAKIM_TARIHI","MOTORYAG","SOGSIVI","HAVAFILTRE","YAKITFILTRE","YAGFILTRE","SUFILTRE","PERSONEL","USER"]
    search_fields = ["JENERATOR","FBAKIM_TARIHI","PERSONEL","USER"]
    list_filter = ["JENERATOR","FBAKIM_TARIHI"]
    class Meta:
        model = FiltreliBakim


@admin.register(Periyodik)
class PeriyodikAdmin(admin.ModelAdmin):
    list_display = ["JENERATOR","PERIYODIK_TARIHI","PERSONEL","USER"]
    search_fields = ["PERIYODIK_TARIHI","PERSONEL","USER"]
    list_filter = ["PERIYODIK_TARIHI","PERSONEL","USER"]
    class Meta:
        model = Periyodik

@admin.register(Personel)
class PersonelAdmin(admin.ModelAdmin):
    list_display = ["PERSONEL_ADI","FIRMA","MESLEK","TELEFON","TCKIMLIK"]
    search_fields = ["PERSONEL_ADI","FIRMA","MESLEK","TELEFON","USER"]
    list_filter = ["PERSONEL_ADI","FIRMA","MESLEK","USER"]
    class Meta:
        model = Personel