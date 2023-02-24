from django.db import models
from django.db.models import TextChoices


# Create your models here.
class StatusChoice(TextChoices):
    NEW = 'NEW', 'Новая'
    IN_PROCESS = 'IN_PROCESS', 'В процессе'
    DONE = 'DONE', 'Сделано'


class Task(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Заголовок")
    description = models.CharField(max_length=50, null=False, blank=False, verbose_name="Описание")
    details = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Подробное описание",
                               default="No description")
    deadline = models.DateField(max_length=16, null=True, blank=True, verbose_name="Выполнить до")
    status = models.CharField(
        choices=StatusChoice.choices,
        max_length=20,
        null=False,
        blank=False,
        verbose_name="Статус",
        default=StatusChoice.NEW)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')
    is_deleted = models.BooleanField(verbose_name='удалено', null=False, default=False)
    deleted_at = models.DateTimeField(verbose_name='Дата и время удаления', null=True, default=None)

    def __str__(self):
        return f"{self.description} - {self.status} {self.deadline}"
