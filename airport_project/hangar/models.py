from django.db import models

class Aircraft(models.Model):
    # Поле aircraft_id (Primary Key) создается автоматически, если не указано явно
    type = models.CharField(max_length=50, verbose_name="Тип")  # Тип (Самолёт, Вертолёт и т.д.)
    model = models.CharField(max_length=100, verbose_name="Модель")  # Модель
    tail_number = models.CharField(max_length=50, unique=True, verbose_name="Бортовой номер")  # Бортовой номер (уникальный)
    status = models.CharField(max_length=50, verbose_name="Статус")  # Статус (исправен, на ТО, списан и т.д.)

    def __str__(self):
        return f"{self.type} {self.model} ({self.tail_number})"

    class Meta:
        verbose_name = "Воздушное судно"
        verbose_name_plural = "Воздушные суда"

class AircraftMaintenance(models.Model):
    # Поле maintenance_id (Primary Key) создается автоматически, если не указано явно
    # Связь с моделью Aircraft
    aircraft = models.ForeignKey('Aircraft', on_delete=models.CASCADE, verbose_name="Воздушное судно")  
    # Связь с моделью User
    mechanic_user = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name="Механик")
    # Связь с моделью Instructor (опционально)
    instructor = models.ForeignKey('Instructor', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Инструктор")  
    # Связь с моделью Parachutist (опционально)
    parachutist = models.ForeignKey('Parachutist', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Парашютист")
    # Связь с моделью Flight (опционально)
    flight = models.ForeignKey('Flight', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Рейс")
    # Дата начала обслуживания
    start_date = models.DateTimeField(verbose_name="Дата начала")
    # Дата окончания обслуживания (опционально)
    end_date = models.DateTimeField(null=True, blank=True, verbose_name="Дата окончания")
    # Описание обслуживания
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return f"Обслуживание {self.aircraft} (начато: {self.start_date})"

    class Meta:
        verbose_name = "Обслуживание воздушного судна"
        verbose_name_plural = "Обслуживания воздушных судов"