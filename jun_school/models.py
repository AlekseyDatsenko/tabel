from django.db import models
from users.models import CustomUser

class Subject(models.Model):

    name = models.CharField(max_length=100, help_text="Введите название предмета:", verbose_name="Предмет")
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("предмет")
        verbose_name_plural = ("Предметы")
        
class TheClass(models.Model):
    
    name = models.CharField(max_length=5, verbose_name="Наименование")
    subject = models.ManyToManyField(Subject, help_text="Выберите предметы для класса:", verbose_name="Предмет")
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("клас")
        verbose_name_plural = ("Классы")

class Student(models.Model):
    student = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True)
    the_class = models.ForeignKey(TheClass, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "{}".format(self.student)

    class Meta:
        verbose_name = ("ученик")
        verbose_name_plural = ("Ученики")
    

