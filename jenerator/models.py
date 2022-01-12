from django.db import models
from django import forms





# Tesisler Modeli
class Tesisler(models.Model):
    ILCE = [("İZMİT","İZMİT"),
            ("GEBZE","GEBZE"),
            ("ÇAYIROVA","ÇAYIROVA"),
            ("DİLOVASI","DİLOVASI"),
            ("DARICA","DARICA"),
            ("KÖRFEZ","KÖRFEZ"),
            ("DERİNCE","DERİNCE"),
            ("KANDIRA","KANDIRA"),
            ("BAŞİSKELE","BAŞİSKELE"),
            ("KARTEPE","KARTEPE"),
            ("GÖLCÜK","GÖLCÜK"),
            ("KARAMÜRSEL","KARAMÜRSEL")]
    TIP = [("AAT","AAT"),
            ("İAT","İAT"),
            ("ATM","ATM"),
            ("İTMDP","İTMDP"),
            ("YTM","YTM"),
            ("HES","HES"),
            ("İBS","İBS"),
            ("DİĞER","DİĞER")]
    USER = models.ForeignKey("auth.User", on_delete=models.PROTECT,verbose_name="Oluşturan ")
    SCADA_KODU = models.CharField(verbose_name = "Scada Kodu ", max_length=50, blank=True)
    ILCE = models.CharField(verbose_name = "İlçe ", choices=ILCE, max_length=50)
    TESIS_ADI = models.CharField(verbose_name = "Tesis Adı " , max_length=100)
    TESIS_TIPI = models.CharField(verbose_name = "Tesis Tipi ",choices=TIP, max_length=50)
    KONUM = models.CharField(verbose_name = "Konumu ", max_length=50)
    OLUSTURMA_TARIHI = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    class Meta:
        verbose_name = "Tesis"
        verbose_name_plural = 'Tesisler'

    def __str__(self):
        return self.TESIS_ADI

# Jeneratör Modeli
class Jeneratorler(models.Model):
    USER = models.ForeignKey("auth.User", on_delete=models.PROTECT,verbose_name="Oluşturan ")
    OLUSTURMA_TARIHI = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    TESIS = models.ForeignKey("Tesisler", on_delete=models.PROTECT,verbose_name="Tesis ")
    PLAKA = models.CharField(verbose_name = "Plaka " , max_length=50)
    GUC = models.IntegerField(verbose_name = "Gücü ")
    MARKA = models.CharField(verbose_name = "Marka  " , max_length=50)
    MODEL = models.CharField(verbose_name = "Model  " , max_length=50)
    MOTOR_MARKA = models.CharField(verbose_name = "Motor Markası  " , max_length=50, blank=True)
    MOTOR_MODEL = models.CharField(verbose_name = "Motor Modeli  " , max_length=50, blank=True)
    MOTOR_SERINO = models.CharField(verbose_name = "Motor SeriNo  " , max_length=50, blank=True)
    ALT_MARKA = models.CharField(verbose_name = "Alternatör Markası  " , max_length=50, blank=True)
    ALT_MODEL = models.CharField(verbose_name = "Alternatör Modeli  " , max_length=50, blank=True)
    ALT_SERINO = models.CharField(verbose_name = "Alternatör SeriNo  " , max_length=50, blank=True)
    KABIN = models.CharField(verbose_name = "Kabin Durumu  " , max_length=50, blank=True)
    ALIS_YONTEMI = models.CharField(verbose_name = "Alış Yöntemi  " , max_length=50, blank=True)
    ACIKLAMA = models.TextField(verbose_name = "Açıklama  " , blank=True)

    class Meta:
        verbose_name = "Jeneratör"
        verbose_name_plural = 'Jeneratörler'
        
    
    def __str__(self):
        return self.PLAKA


# Arıza Modeli
class Arizalar(models.Model):
    ARIZATIPI = [('MOTOR İÇİ ARIZALARI','MOTOR İÇİ ARIZALARI'),
                ('ENJEKTÖR ARIZASI','ENJEKTÖR ARIZASI'),
                ('MOTOR KAYIŞI ARIZALARI','MOTOR KAYIŞI ARIZALARI'),
                ('HARARET ARIZASI','HARARET ARIZASI'),
                ('SU DEVİRDAİM ARIZASI','SU DEVİRDAİM ARIZASI'),
                ('TURBO ARIZASI','TURBO ARIZASI'),
                ('TURBO HORTUMU VE AKSAMI ARIZASI','TURBO HORTUMU VE AKSAMI ARIZASI'),
                ('YAKIT POMPASI ARIZASI','YAKIT POMPASI ARIZASI'),
                ('YAKIT HORTUMU ARIZASI','YAKIT HORTUMU ARIZASI'),
                ('YAKIT FİLTRE ARIZASI','YAKIT FİLTRE ARIZASI'),
                ('YAKIT YOK ARIZASI','YAKIT YOK ARIZASI'),
                ('YAKIT KÖTÜ ARIZASI','YAKIT KÖTÜ ARIZASI'),
                ('YAĞ HORTUMU ARIZASI','YAĞ HORTUMU ARIZASI'),
                ('YAĞ FİLTRE ARIZASI','YAĞ FİLTRE ARIZASI'),
                ('YAĞ SEVİYE ARIZASI','YAĞ SEVİYE ARIZASI'),
                ('HAVA FİLTRE ARIZASI','HAVA FİLTRE ARIZASI'),
                ('HAVA SİRKÜLASYON ARIZASI','HAVA SİRKÜLASYON ARIZASI'),
                ('RADYATÖR ARIZASI','RADYATÖR ARIZASI'),
                ('SU EKSİK ARIZASI','SU EKSİK ARIZASI'),
                ('SU FİLTRE ARIZASI','SU FİLTRE ARIZASI'),
                ('HİDROLİK GOVERNÖR ARIZASI','HİDROLİK GOVERNÖR ARIZASI'),
                ('DİĞER MOTOR ARIZASI','DİĞER MOTOR ARIZASI'),
                ('OTOMATİK KAYIŞ GERGİ TERTİBATI','OTOMATİK KAYIŞ GERGİ TERTİBATI'),
                ('MAGNETİK PİCK-UP ARIZASI','MAGNETİK PİCK-UP ARIZASI'),
                ('AKÜ ARIZASI','AKÜ ARIZASI'),
                ('ATEŞLEME ARIZASI','ATEŞLEME ARIZASI'),
                ('DÜŞÜK - YÜKSEK FREKANS ARIZASI','DÜŞÜK - YÜKSEK FREKANS ARIZASI'),
                ('AŞIRI YÜKLENME ARIZASI','AŞIRI YÜKLENME ARIZASI'),
                ('DÜŞÜK- YÜKSEK GERİLİM ARIZASI','DÜŞÜK- YÜKSEK GERİLİM ARIZASI'),
                ('ŞARJ DİNAMOSU ARIZASI','ŞARJ DİNAMOSU ARIZASI'),
                ('REDRESÖR ARIZASI','REDRESÖR ARIZASI'),
                ('YAKIT SEVİYE SENSÖRÜ ARIZASI','YAKIT SEVİYE SENSÖRÜ ARIZASI'),
                ('ALTERNATÖR SARGI ARIZASI','ALTERNATÖR SARGI ARIZASI'),
                ('ALTERNATÖR ARIZASI DİĞER','ALTERNATÖR ARIZASI DİĞER'),
                ('GOVERNÖR ARIZASI','GOVERNÖR ARIZASI'),
                ('GERİLİM DÜZENLEYİCİ ARIZASI','GERİLİM DÜZENLEYİCİ ARIZASI'),
                ('DÖNER DİYOT ARIZASI','DÖNER DİYOT ARIZASI'),
                ('MARŞ MOTORU ARIZASI','MARŞ MOTORU ARIZASI'),
                ('AKIM TRAFOSU ARIZASI','AKIM TRAFOSU ARIZASI'),
                ('REZİSTANS ARIZASI','REZİSTANS ARIZASI'),
                ('TERMOSTAT ARIZASI','TERMOSTAT ARIZASI'),
                ('MARŞ RÖLESİ ARIZASI','MARŞ RÖLESİ ARIZASI'),
                ('KONJEKTÖR ARIZASI','KONJEKTÖR ARIZASI'),
                ('BLOK SUYU ISITICISI ARIZASI','BLOK SUYU ISITICISI ARIZASI'),
                ('KONTROL KARTI ARIZASI','KONTROL KARTI ARIZASI'),
                ('ECU ARIZASI','ECU ARIZASI'),
                ('KUMANDA RÖLE VE SİGORTA ARIZASI','KUMANDA RÖLE VE SİGORTA ARIZASI'),
                ('KABLO TEMASSIZLIK ARIZASI','KABLO TEMASSIZLIK ARIZASI'),
                ('HARMONİK BOZULUM ARIZASI','HARMONİK BOZULUM ARIZASI'),
                ('ISITICI HORTUMU ARIZASI','ISITICI HORTUMU ARIZASI'),
                ('VOLAN DİŞLİSİ ARIZASI','VOLAN DİŞLİSİ ARIZASI'),
                ('KAYIŞ ARIZASI','KAYIŞ ARIZASI'),
                ('KABİN ARIZASI','KABİN ARIZASI'),
                ('TAHRİBAT ARIZASI','TAHRİBAT ARIZASI'),
                ('ÇALINMA','ÇALINMA'),
                ('SUSTURUCU VE EGZOS ARIZASI','SUSTURUCU VE EGZOS ARIZASI'),
                ('EMME VE EGZOS MANİFOLT ARIZASI','EMME VE EGZOS MANİFOLT ARIZASI'),
                ('YAĞ SOĞUTUCUSU ARIZASI','YAĞ SOĞUTUCUSU ARIZASI'),
                ('JENERATÖR AYLIK RUTİN BAKIM','JENERATÖR AYLIK RUTİN BAKIM'),
                ('JENERATÖR YILLIK RUTİN BAKIM','JENERATÖR YILLIK RUTİN BAKIM'),
                ('ELEKTRİK BİRİMİ İLE İLGİ İLGİLİ ARIZA','ELEKTRİK BİRİMİ İLE İLGİ İLGİLİ ARIZA'),
                ('SCADA KAYNAKLI ARIZA ','SCADA KAYNAKLI ARIZA ')]

    USER = models.ForeignKey("auth.User", on_delete=models.PROTECT,verbose_name="Oluşturan ")
    ARIZA_TARIHI = models.DateTimeField(auto_now_add=True,verbose_name="Arıza Tarihi")
    JENERATOR = models.ForeignKey("Jeneratorler", on_delete=models.PROTECT,verbose_name="Jenerator ")
    ARIZA_TIPI = models.CharField(verbose_name = "Arıza Tipi ", choices=ARIZATIPI, max_length=150)
    DEGISEN_PARCA = models.CharField(verbose_name = "Değişen Parça  " , max_length=100, blank=True)
    PERSONEL = models.ForeignKey("Personel", on_delete=models.PROTECT,verbose_name="Personel ")
    ACIKLAMA = models.TextField(verbose_name = "Açıklama  " , blank=True)
    

    class Meta:
        verbose_name = "Arıza"
        verbose_name_plural = "Arızalar"
    
    def __str__(self):
        return self.ARIZA_TIPI
    
class FiltreliBakim(models.Model):
    USER = models.ForeignKey("auth.User", on_delete=models.PROTECT,verbose_name="Oluşturan ")
    FBAKIM_TARIHI = models.DateTimeField(auto_now_add=True,verbose_name="Bakım Tarihi")
    JENERATOR = models.ForeignKey("Jeneratorler", on_delete=models.PROTECT,verbose_name="Jenerator ")
    MOTORYAG = models.IntegerField(verbose_name = "Motor Yağı Miktarı ",blank=True)
    SOGSIVI = models.IntegerField(verbose_name = "Soğutma Sıvısı Miktarı ",blank=True)
    HAVAFILTRE = models.IntegerField(verbose_name = "Hava Filtresi ",blank=True)
    YAKITFILTRE = models.IntegerField(verbose_name = "Yakıt Filtresi ",blank=True)
    YAGFILTRE = models.IntegerField(verbose_name = "Yağ Filtresi ",blank=True)
    SUFILTRE = models.IntegerField(verbose_name = "Su Filtresi ",blank=True)
    PERSONEL = models.ForeignKey("Personel", on_delete=models.PROTECT,verbose_name="Personel ")
    ACIKLAMA = models.TextField(verbose_name = "Açıklama  " , blank=True)

    class Meta:
        verbose_name = "Filtreli Bakım"
        verbose_name_plural = "Filtreli Bakımlar"
    
    def __str__(self):
        return str(self.JENERATOR)

class Periyodik(models.Model):
    USER = models.ForeignKey("auth.User", on_delete=models.PROTECT,verbose_name="Oluşturan ")
    PERIYODIK_TARIHI = models.DateTimeField(auto_now_add=True,verbose_name="Bakım Tarihi")
    JENERATOR = models.ForeignKey("Jeneratorler", on_delete=models.PROTECT,verbose_name="Jenerator ")
    PERSONEL = models.ForeignKey("Personel", on_delete=models.PROTECT,verbose_name="Personel ")
    ACIKLAMA = models.TextField(verbose_name = "Açıklama  " , blank=True)

    class Meta:
        verbose_name = "Periyodik Bakım"
        verbose_name_plural = "Periyodik Bakımlar"
    
    def __str__(self):
        return str(self.JENERATOR)

class Personel(models.Model):
    MSLK=[("Elektrik","Elektrik"),("Motor","Motor"),("İdari","İdari"),("Diğer","Diğer")]

    USER = models.ForeignKey("auth.User", on_delete=models.PROTECT,verbose_name="Oluşturan ")
    PERIYODIK_TARIHI = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturma Tarihi")
    PERSONEL_ADI = models.CharField(verbose_name="Personel Tam Adı", max_length=50)
    FIRMA = models.CharField(verbose_name="Firma ", max_length=100)
    MESLEK = models.CharField(verbose_name="Meslek ",choices=MSLK, max_length=50)
    TELEFON = models.CharField(verbose_name="Telefon No ", max_length=100)
    TCKIMLIK = models.CharField(verbose_name = "TC Kimlik No ", blank=True,null=True,max_length=50)
    ACIKLAMA = models.TextField(verbose_name = "Açıklama  " , blank=True)
    

    class Meta:
        verbose_name = "Personel"
        verbose_name_plural = "Personeller"
    
    def __str__(self):
        return self.PERSONEL_ADI
    
            