from django.db import models

# Create your models here.

class SingleBoardComputer(models.Model):
  """ Таблица подключавшихся одноплатных компьютеров """
  name = models.CharField(max_length=255, verbose_name="Название")
  description = models.TextField(verbose_name="Описание", blank=True, null=True)

  def __str__(self):
      return self.name
  

class Status(models.Model):
  """ Таблица состояний одноплатных компьютеров """  
  sbc = models.ForeignKey(SingleBoardComputer, on_delete=models.CASCADE)
  # time = models.DateTimeField(verbose_name="Дата и время коннекта")
  connected_since = models.DateTimeField(verbose_name="Дата коннекта")
  last_ref = models.DateTimeField(verbose_name="Дата обновления виртуального адреса")
  real_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Реальный адрес")
  virtual_address = models.GenericIPAddressField(null=True, blank=True, verbose_name="Виртуальный адрес" )
  updated = models.DateTimeField(verbose_name="Дата последнего обновления")

  def __str__(self):
      return F"{self.updated} {self.sbc.name}" 
  
