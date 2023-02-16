from django.db import models

# Create your models here.


CHOICES = [
    ('new', "Новая"),
    ('in process', "В процессе"),
    ('done', "Сделано")
]


class Task(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Заголовок")
    description = models.CharField(max_length=50, null=False, blank=False, verbose_name="Описание")
    details = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Подробное описание",
                               default="No description")
    deadline = models.DateField(max_length=16, null=True, blank=True, verbose_name="Выполнить до")
    status = models.CharField(choices=CHOICES, max_length=15, null=False, blank=False, verbose_name="Статус",
                              default=CHOICES[0][0])

    def __str__(self):
        return f"{self.description} - {self.status}"

    def get_choice(self, choice):
        return [c[0] for c in CHOICES if c == choice]
