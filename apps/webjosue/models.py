from django.db import models

# Create your models here.
class cliente(models.Model):
    pk_cliente = models.AutoField(primary_key=True, blank=False,null=False,)
    name_cliente = models.CharField(max_length=80, default="n/a", null=False, blank=False)
    Dpi = models.BigIntegerField(null=False, blank=False)
    Edad= models.BigIntegerField(null=False, blank=False)
    sexo = models.CharField(max_length=20, null=False, blank=False)
    imagen = models.URLField( blank=False, null=False,default='https://i.postimg.cc/RZzf39xm/undraw-male-avatar-323b.png')



class servicio(models.Model):
    pk_servicio = models.AutoField(primary_key=True, blank=False, null=False,)
    chequeo_medico= models.CharField(max_length=200, null=False, blank=False)
    precio = models.BigIntegerField(null=False, blank=False)

class cita(models.Model):
    pk_cita = models.AutoField(primary_key=True, blank=False,null=False,)
    fk_cliente = models.ForeignKey(cliente, on_delete=models.CASCADE, null=False, blank=False)
    fk_servicio = models.ForeignKey(servicio, on_delete=models.CASCADE, null=False, blank=False)
    fecha_y_hora = models.DecimalField(null=False, max_digits=4, decimal_places=2)


class medico(models.Model):
    pk_medico = models.AutoField(primary_key=True,blank=False, null=False,)
    name_medico = models.CharField(max_length=80, default="n/a", null=False, blank=False)
    especialidad = models.CharField(max_length=100, null=False, blank=False )
    turno = models.BigIntegerField(null=False, blank=False)
