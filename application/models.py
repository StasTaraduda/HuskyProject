from django.db import models
from django.core.exceptions import ValidationError


class Client(models.Model):
    first_name = models.CharField(max_length=50, blank=False, error_messages={"blank": "Введіть значення до поля 'Ім'я власника'"})
    last_name = models.CharField(max_length=50, blank=False, error_messages={"blank": "Введіть значення до поля 'Прізвище власника'"})
    email = models.CharField(max_length=200, blank=False,
                             error_messages={"blank": "Введіть значення до поля 'Електрона почта клієнта'"})
    phone_number = models.CharField(max_length=13, blank=False,
                                    error_messages={"blank": "Введіть значення до поля 'Номер мобільного телефону клієнта'",
                                                    "max_length": "Введено багато символів. Номер телефону має містити 13 символів"})

    class Meta:
        verbose_name = "Клієнти"
        ordering = ['last_name']

    def __str__(self):
        return self.last_name + " " + self.first_name

    # def clean(self):
    #     errors = {}
    #     if not self.first_name:
    #         errors['first_name'] = ValidationError("Укажіть ім'я клієнта")
    #     if not self.last_name:
    #         errors['last_name'] = ValidationError("Укажіть прізвище клієнта")
    #     if not self.email:
    #         errors['email'] = ValidationError("Укажіть електронну почту клієнта")
    #     if not self.phone_number:
    #         errors['phone_number'] = ValidationError("Укажіть номер телефону клієнта")
    #     if errors:
    #         raise ValidationError(errors)


class ClientPet(models.Model):
    Kinds = (
        (None, "Оберіть стать вашої тваринки"),
        ('a', 'Чоловічий'),
        ('b', 'Жіночий'),)
    nickname = models.CharField(max_length=50, blank=False, error_messages={"blank": "Введіть значення до поля Кличка"})
    age = models.IntegerField(blank=False, error_messages={"blank": "Укажіть вік тваринки"})
    sex = models.CharField(max_length=20, choices=Kinds, blank=False, error_messages={"blank": "Укажіть стать тваринки"})
    client = models.ForeignKey(Client, on_delete=models.PROTECT)
    breedOfAnimal = models.ForeignKey('BreedOfAnimal', on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Тваринки клієнтів"
        ordering = ['nickname']

    def __str__(self):
        return self.nickname


class BreedOfAnimal(models.Model):
    name = models.CharField(max_length=100, blank=False, error_messages={"blank": "Укажіть породу тваринки"})
    animal = models.ForeignKey('Animal', on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Породи тварин"
        ordering = ['name']

    def __str__(self):
        return self.name


class Animal(models.Model):
    kindOfAnimal = models.CharField(max_length=100, blank=False, error_messages={"blank": "Укажіть тип тваринки"})

    class Meta:
        verbose_name = "Види тварин"
        ordering = ['kindOfAnimal']

    def __str__(self):
        return self.kindOfAnimal


class Timetable(models.Model):
    dateofAdmission = models.DateField(error_messages={"blank": "Укажіть дату прийому"})
    statusTimetable = models.BooleanField()
    client = models.ForeignKey(Client, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Розклад прийомів"
        ordering = ['dateofAdmission']

    def __str__(self):
        return "Дата прийому" + str(self.dateofAdmission)




