from django.db import models
from core.models import PublishedModel


# Категории.
class Category(PublishedModel):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=64, unique=True)
    output_order = models.PositiveSmallIntegerField(default=100)


# Топпинги.
class Topping(PublishedModel):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=64, unique=True)


# Обёртки.
class Wrapper(PublishedModel):
    is_published = models.BooleanField(default=True)
    title = models.CharField(max_length=256)


# Сорта мороженого.
class IceCream(PublishedModel):
    is_on_main = models.BooleanField(default=False)
    title = models.CharField(max_length=256)
    description = models.TextField()
    # Создайте нужные связи между моделями:
    wrapper = models.OneToOneField(
        Wrapper,
        on_delete=models.SET_NULL,
        null=True,
        blank=True  # инструкция - поле не обязательное
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    toppings = models.ManyToManyField(
        Topping
    )


'''
from django.core.validators import MaxValueValidator, MinValueValidator

class Category(models.Model):
    output_order = models.PositiveIntegerField(
        default=100,
        validators=[MinValueValidator(0), MaxValueValidator(32767)])
'''

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

# 3
'''
В файле models.py приложения ice_cream описаны четыре модели:

    Category — категории сортов мороженого; каждое мороженое принадлежит
    лишь одной категории; одной категории может принадлежать несколько сортов;

    Topping — добавки к мороженому;
    к каждому мороженому может прилагаться несколько топпингов;

    Wrapper — обёртки для мороженого;
    у каждого сорта мороженого может быть только одна обёртка;

    IceCream — сорта мороженого.

В модель IceCream добавьте поля, связывающие её с остальными моделями:

С моделью Category:
имя поля: category;
тип связи: N:1;
обязательное поле;
при удалении категории должны быть удалены
все сорта мороженого из этой категории

С моделью Topping:
имя поля: toppings;
тип связи: N:M;
обязательное поле;

С моделью Wrapper:
имя поля: wrapper;
тип связи: 1:1;
необязательное поле;
при удалении связанной записи в этом поле должно быть установлено NULL.
'''
