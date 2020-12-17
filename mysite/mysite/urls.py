from django.contrib import admin
from django.urls import path, include


# Это - маршрутизатор. Мы в корне проекта. Что мы здесь делаем = создаем таблицу маршрутизации
# это если по-человечески выражаться. Представим абстрактно - мы сейчас программа с доступом уровня
# ядра, которая созданна для удобства. Что такого удобного, и полезного мы делаем - у нас есть
# список урлов (по-идее, так было задуманно) всех мастей и областей, каждый урл -
# ведет нас к подключенному application. Допустим урл из списка - дальше никуда не ссылаеться,
# он endpoint (т.е. ссылаеться на объекты в рамках своего layer). Зачем нам этот endpoint -
# грубо говоря он тянет все что реализованно на его layer, результаты выполнения функций вьюшек,
# статику, модели итд... А мы тянем с него всё что он собрал. Мы имён этих функций не знаем,
# мы пользуемся их результатом. В общем тянем patterns.
# Как мы это реализуем:
# функция = include(), функция вытянутая из ядра Джанго.

# *Ремарка - реализует не include() !!!

# admin.site.urls - отдельный случай когда include() не задействуем. Это наша админка.


urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]


# Функция path():     |это не тот PATH который системная переменная $PATH|
# Аргументы - route , view.
# Если коротко - эти два аргумента обязательны, а само описание
# функции с использованием этой пары, где route - это pattern ('polls/') а view - это результат
# выполнения функций, описано выше...

# !!! НО как раз таки аргумент view, функции path() и реализует получение собранных объектов,
# по адресу route. Реализация интересная, как-раз таки наш endpoint импортирует из модуля
# wiev (на своем layere) функцию, которая являеться результатом выполнения специфического
# Класса, импортированного из ядра django = HttpResponse(), который или очень умный или
# немного туповат, он просто возвращает свои аттрибуты, как бы отвечая на вызов.

# Аргументы - функции path() kwargs и name - не обязательны.
# kwargs - чёто здесь не понял, но вроди тоже что и name, а пример с name описан мной в
# application hello/ . В общем
# И последнее - когда приходит запрос, HTTP - он попадает сюда, в таблицу маршрутизации перебирая
# routes (patterns) урлы, при совпадении срабатывает сценарий view...



"""
mysite URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
