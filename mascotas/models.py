from django.db import models

# Create your models here.
class Mascota(models.Model):
    # Django automáticamente crea un campo 'id' (Primary Key) autoincremental
    # id_mascota será el 'id' por defecto de Django, así que no necesitamos definirlo explícitamente

    nombre = models.CharField(max_length=100)
    raza = models.CharField(max_length=50, blank=True, null=True)
    especie = models.CharField(max_length=50, choices=[
        ('Perro', 'Perro'),
        ('Gato', 'Gato'),
        ('Pez', 'Pez'),
        ('Ave', 'Ave'),
        ('Roedor', 'Roedor'),
        ('Reptil', 'Reptil'),
        ('Otro', 'Otro'),
    ], default='Otro')
    fecha_nacimiento = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = "Mascota"
        verbose_name_plural = "Mascotas"

    def __str__(self):
        return f'{self.nombre} ({self.especie} - {self.raza or "Sin Raza"})'