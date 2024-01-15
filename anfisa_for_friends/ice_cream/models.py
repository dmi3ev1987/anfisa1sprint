from django.db import models
'''
from django.core.validators import MaxValueValidator, MinValueValidator
class Category(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=64, unique=True)
    output_order = models.PositiveIntegerField(
        default=100,
        validators=[MinValueValidator(0), MaxValueValidator(32767)])
    is_published = models.BooleanField(default=True)
'''


# Категории
class Category(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=64, unique=True)
    output_order = models.PositiveSmallIntegerField(default=100)
    is_published = models.BooleanField(default=True)


# Топпинги
class Topping(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=64, unique=True)
    is_published = models.BooleanField(default=True)


# Обёртки
class Wrapper(models.Model):
    title = models.CharField(max_length=256)
    is_published = models.BooleanField(default=True)


# Сорта мороженого
class IceCream(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    is_on_main = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)


# 1
'''
В тренажёр загружен Django-проект «Анфиса для друзей». Ваша задача —
подружить проект с базой данных.
В файле models.py приложения ice_cream создайте три модели:

Wrapper (обёртки и упаковки мороженого)

title — строка (не более 256 символов);
is_published — булев тип (по умолчанию — True).

Topping (топпинги — добавки для мороженого)

title — строка (не более 256 символов);
slug — поле типа slug (не более 64 символов, уникальное в пределах таблицы).
is_published — булев тип (по умолчанию — True);

IceCream (сорта мороженого)

title — строка (не более 256 символов);
description — текстовое поле.
is_on_main — булев тип (по умолчанию — False);
is_published — булев тип (по умолчанию — True);

Поле is_published будет определять, должна ли запись публиковаться на сайте
или надо скрыть её от посетителей. Поле is_on_main указывает,
должна ли запись выводиться на главную страницу проекта.
Как указываются типы полей, как задаются значения по умолчанию,
как ограничивается число символов — найдите в документации Django
или в тематических статьях.
Работа с документацией — это важная часть работы; все разработчики делают это!
'''

# 2
'''
В файле models.py приложения ice_cream
создайте модель Category (категории сортов мороженого).
Поля модели:
title — строка (не более 256 символов)
slug — поле типа slug (не более 64 символов, уникальное в пределах таблицы)
output_order — целочисленное поле с ограничением значений
от 0 до 32767 (значение по умолчанию — 100)
is_published — булев тип (по умолчанию — True)

Поле output_order — это «вес» записи, определяющий порядок её отображения
на странице проекта; в дальнейшем с помощью этого поля, используя ORDER BY,
администратор сможет менять порядок вывода данных на веб-страницу:
чем меньше «вес» записи — тем выше она отобразится («лёгкое — всплывает»).
'''
