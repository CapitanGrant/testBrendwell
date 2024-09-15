from django.core.exceptions import ValidationError
from django.db import models

def validate_positive(value):
    if value <= 0:
        raise ValidationError('Цена должна быть положительным числом.')
class Product(models.Model):
    id = models.AutoField(primary_key=True)  # Автоматический  идентификатор
    name = models.CharField(max_length=255, null=True, blank=True)  # Название продукта
    description = models.TextField()  # Описание продукта
    price = models.IntegerField(validators=[validate_positive])  # Цена продукта

    def __str__(self):
        return self.name