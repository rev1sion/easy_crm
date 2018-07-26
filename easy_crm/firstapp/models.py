import os
from os.path import basename
from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from firstapp.validators import validate_file_extension

# Create your models here.

# Company - это класс для создания "Организации", для которой создаются объекты на
# на которых ведутся работы.

class Company(models.Model):
    owner = models.ForeignKey(User)
    name = models.CharField(max_length=300, verbose_name='Организация')
    address = models.CharField(max_length=300, verbose_name='Юридический адрес')
    actual_adress = models.CharField(max_length=300, verbose_name='Фактический адрес')
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message='''Номер телефона должен быть введен в формате:
                «+999999999». Допускается до 15 цифр.'''
        )
    phone_number = models.CharField(
        verbose_name='Телефон',
        validators=[phone_regex],
        max_length=17, blank=True
    )
    url = models.URLField(verbose_name='Сайт')
    email = models.EmailField(verbose_name='Email')

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'

    def __str__(self):
        return self.name

# CommentCompany - комментарии к компаниям

class CommentCompany(models.Model):
    owner = models.ForeignKey(User)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Комментарий')
    created = models.DateTimeField("Добавлен", auto_now_add=True)
    moder = models.BooleanField(default=False)

    class Meta():
        verbose_name = 'Комментарий организации'
        verbose_name_plural = 'Комментарии организаций'
    
    def __str__(self):
        return '{} {} {} {}'.format(self.owner, self.created, self.company, self.text)


# CompanyObject - это класс добавления объекта к компании(class Company)

class CompanyObject(models.Model):
    owner_obj = models.ForeignKey(User)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    address = models.CharField(max_length=300, verbose_name='Адрес объекта')
    comment = models.CharField(max_length=300, verbose_name='Объект')

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'

    def __str__(self):
        return '{} {}'.format(self.company, self.address)


# CommentObject - это класс добавления комментария к объекту (class CompanyObject)

class CommentObject(models.Model):
    owner = models.ForeignKey(User)
    company_object = models.ForeignKey(CompanyObject, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Комментарий')
    created = models.DateTimeField('Добавлен', auto_now_add=True)
    moder = models.BooleanField(default=False)

    class Meta():
        verbose_name = 'Комментарий объекту'
        verbose_name_plural = 'Комментарии объектов'

    def __str__(self):
        return '{} {} {} {}'.format(self.owner, self.created, self.company_object, self.text) 


#CompanyContact - это класс добавления контактных лиц к Company и CompanyObject

class CompanyContact(models.Model):    
    company_contact = models.ForeignKey(Company, on_delete=models.CASCADE)
    fio = models.CharField(max_length=300, verbose_name='Ф.И.О.')
    position = models.CharField(max_length=300, verbose_name='Должность')
    tel = models.CharField(max_length=300, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Email')

    class Meta:
        verbose_name = 'Контактные лица'
        verbose_name_plural = 'Контактные лица'
    
    def __str__(self):
        return '{} {} {}'.format(self.fio, self.tel, self.position)

#ObjectContact - это класс добаления контактных лиц из CompanyContact

class ObjectContact(models.Model):
    object_contact = models.ForeignKey(CompanyContact)
    company_object = models.ForeignKey(CompanyObject, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Контактные лица объекта'
        verbose_name_plural = 'Контактные лица объекта'

    def __str__(self):
        return '{} {}'.format(self.company_object, self.object_contact)    

#CompanyObjectWork - это класс добавление работы по объекту(CompanyObject)

class CompanyObjectWork(models.Model):
    
    CHOICES_FOR_WORK = (
        ('переговоры' , 'переговоры'),
        ('договор' , 'договор'),
        ('аванс' , 'аванс'),
        ('в работе' , 'в работе'),
        ('выполнено' , 'выполнено'),
        ('оплата' , 'оплата'),
        ('завершен' , 'завершен'),
    )
    
    user_work = models.ForeignKey(User, blank=True, verbose_name='Ответственный')
    company_object = models.ForeignKey(CompanyObject, on_delete=models.CASCADE)
    work = models.CharField(max_length=300, verbose_name='Работа')
    status = models.CharField(choices=CHOICES_FOR_WORK, max_length=100, verbose_name='Статус работы')

    class Meta:
        verbose_name = 'Работа'
        verbose_name_plural = 'Работы'

    def __str__(self):
        return '{} {} {} {}'.format(self.work, self.company_object, self.user_work, self.status)

#ContactWork - это класс добавления контактов к "Работе"(СompanyObjectWork)

class ContactWork(models.Model):
    work = models.ForeignKey(CompanyObjectWork, on_delete=models.CASCADE)
    fio = models.CharField(max_length=300, verbose_name='Ф.И.О.')
    position = models.CharField(max_length=300, verbose_name='Должность')
    tel = models.CharField(max_length=300, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Email')

    class Meta:
        verbose_name = 'Контактные лица к работе'
        verbose_name_plural = 'Контактыне лица к работе'

    def __str__(self):
        return '{} {} {}'.format(self.fio, self.tel, self.position)

#CommentWork - это класс добавления комментариев к работе(СompanyObjectWork)

class CommentWork(models.Model):
    owner = models.ForeignKey(User)
    work = models.ForeignKey(CompanyObjectWork, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Комментарий')
    created = models.DateTimeField('Добавлен', auto_now_add=True)
    moder = models.BooleanField(default=False)

    class Meta():
        verbose_name = 'Комментарий работе'
        verbose_name_plural = 'Комментарии объектов'

    def __str__(self):
        return '{} {} {} {}'.format(self.owner, self.created, self.work, self.text)

#DocumentWork - это класс прикрепления документов к работе(CompanyObjectWork)

class DocumentWork(models.Model):
    owner = models.ForeignKey(User)
    work = models.ForeignKey(CompanyObjectWork, on_delete=models.CASCADE)
    file = models.FileField(upload_to='work/documents/%Y/%m/%d', validators=[validate_file_extension])

    class Meta():
        verbose_name = 'Прикрепленный документ'
        verbose_name_plural = 'Прикрепленные документы'
    
    def filename(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return '{} {} {}'.format(self.owner, self.work, self.file)

    
'''
AddFileToWork -
class Account - это можель профиля пользователя, профиль пользователя создаётся
в админке.
'''
class Account(models.Model):
    account_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')
    account_fio = models.CharField(max_length=300, verbose_name='Ф.И.О.')
    position = models.CharField(max_length=300, verbose_name='Должность')
    phone_number = models.CharField(max_length=300, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Email')
    hobby = models.CharField(max_length=300, verbose_name='Хобби')
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='user_avatar/', blank=True)

    def __str__(self):
        return '{} {}'.format(self.account_fio, self.position)

#CommentsForCompany
#Доработать форму комментариев


