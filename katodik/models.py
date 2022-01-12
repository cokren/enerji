from django.db import models

#Hatlar Modeli
class Hatlar(models.Model):
    HATTIP = [("İÇMESUYU","İÇMESUYU"),
            ("ATIKSU","ATIKSU"),
            ("YAĞMURSUYU","YAĞMURSUYU")]

    USER = models.ForeignKey("auth.User", on_delete=models.PROTECT,verbose_name="Oluşturan ")
    OLUSTURMA_TARIHI = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    HAT_ADI = models.CharField(verbose_name = "Hat Adı: ", max_length=50)
    HAT_TIPI = models.CharField(verbose_name = "Hat Tipi  " , choices = HATTIP, max_length=50)
    CAP = models.IntegerField(verbose_name = "Çapı ", blank=True, null=True)
    UZUNLUK = models.IntegerField(verbose_name = "Uzunluğu ", blank=True, null=True)
    KAPLAMA = models.CharField(verbose_name = "Kaplaması  " , max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = "Hat"
        verbose_name_plural = 'Hatlar'

    def __str__(self):
        return self.HAT_ADI

#Pano Modeli

class Panolar(models.Model):
    PANOTIP = [("PIC","PIC"),("PLC","PLC"),("DSPIC","DSPIC"),("Diğer","Diğer")]

    USER = models.ForeignKey("auth.User", on_delete=models.PROTECT,verbose_name="Oluşturan ")
    OLUSTURMA_TARIHI = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    PANO_ADI = models.CharField(verbose_name = "Pano Adı: ", max_length=50)
    PANO_TIPI = models.CharField(verbose_name = "Pano Tipi  " , choices = PANOTIP, max_length=50)
    PANO_MARKA = models.CharField(verbose_name = "Pano Marka Modeli  ", max_length=50)
    DEVREYE_ALMA_TARIHI = models.DateField(verbose_name="Devreye Alma Tarihi")
    HAT = models.ForeignKey("Hatlar", on_delete=models.PROTECT,verbose_name="Koruduğu Hat ")
    MODEM = models.CharField(verbose_name = "Modem Marka Model: ", max_length=50)
    IP = models.CharField(verbose_name = "IP: ", max_length=50)
    KONUM = models.CharField(verbose_name = "Konumu ", max_length=50)
    ACIKLAMA = models.TextField(verbose_name="Açıklama ",blank=True, null=True)

    class Meta:
        verbose_name = "Pano"
        verbose_name_plural = 'Panolar'

    def __str__(self):
        return self.PANO_ADI



