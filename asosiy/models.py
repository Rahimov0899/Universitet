from django.db import models


class Yonalish(models.Model):
    nom = models.CharField(max_length=100)
    aktiv = models.BooleanField(default=True)

    def __str__(self):
        return self.nom


class Fan(models.Model):
    nom = models.CharField(max_length=100)
    yonalish = models.ForeignKey(Yonalish, on_delete=models.CASCADE)
    asosiy = models.BooleanField(default=False)


    def __str__(self):
        return self.nom


class Ustoz(models.Model):
    DARAJALAR = [
        ('Bakalavr', 'Bakalavr'),
        ('Magistr', 'Magistr'),
        ('Doktorant', 'Doktorant'),
        ('Doktor', 'Doktor')
    ]

    ism = models.CharField(max_length=100)
    jins = models.CharField(max_length=10, choices=[('Erkak', 'Erkak'), ('Ayol', 'Ayol')])
    yosh = models.IntegerField()
    daraja = models.CharField(max_length=100, choices=DARAJALAR)
    fan = models.ForeignKey(Fan, on_delete=models.CASCADE)

    def __str__(self):
        return self.ism

class Nashryot(models.Model):
    nom=models.CharField(max_length=100)
    manzil=models.CharField(max_length=200)
    def __str__(self):
        return self.nom

class Kitob(models.Model):
    nom=models.CharField(max_length=100)
    narx=models.FloatField()
    kelgan_sana=models.DateField()
    nashryot=models.ForeignKey(Nashryot,on_delete=models.CASCADE)
    def __str__(self):
        return self.nom

class Sotuvchi(models.Model):
    ism = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)

    def __str__(self):
        return self.ism

class Sotuv(models.Model):
    kitob=models.ForeignKey(Kitob,on_delete=models.CASCADE)
    sotuvchi=models.ForeignKey(Sotuvchi,on_delete=models.CASCADE)
    sana=models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.kitob} {self.sotuvchi}"
