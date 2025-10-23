from django.db import models

# Create your models here.
import uuid


class Caracteristici(models.Model):
    nume = models.CharField(max_length=100)
    descriere = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nume}, {self.descriere}"


class Brand(models.Model):
    nume_brand = models.CharField(max_length=100, unique=True)  # unic
    tara_origine = models.CharField(max_length=50, blank=True)
    an_infiintare = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nume_brand


class Oferta(models.Model):
    nume_oferta = models.CharField(max_length=100, default="Promotie")
    data_inceput = models.DateTimeField(auto_now_add=True)  # datetime
    data_sfarsit = models.DateTimeField()
    cod_reducere = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nume_oferta


class Curea(models.Model):
    material_curea = models.CharField(max_length=100)
    latime_curea = models.IntegerField()
    culoare = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.material_curea} {self.culoare} ({self.latime_curea}mm)"


class Mecanism(models.Model):
    class TipuriMecanism(models.TextChoices):  # choices
        AUTOMATIC = "AUT", "Automatic"
        MECANIC = "MEC", "Mecanic (Manual)"
        QUARTZ = "QRT", "Quartz"
        SOLAR = "SOL", "Solar"
        SPRING_DRIVE = "SPR", "Spring Drive"

    tip_mecanism = models.CharField(
        max_length=3,
        choices=TipuriMecanism.choices,
        default=TipuriMecanism.QUARTZ,  # valoare default
    )
    frecventa = models.CharField(max_length=50, blank=True, null=True)
    precizie = models.CharField(max_length=50, null=True)  # valoare null

    def __str__(self):
        return f"{self.tip_mecanism}"


class Ceasuri(models.Model):
    nume_model = models.CharField(max_length=255)
    stoc = models.IntegerField(default=0)  # valoare default
    tip_geam = models.CharField(max_length=50)
    diametru_carcasa = models.IntegerField()
    pret = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nume}, {self.descriere}"
