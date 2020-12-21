from django.contrib import admin

from .models import Question
from .models import Choice

admin.site.register(Question)
admin.site.register(Choice)






# Register your models here.
# Здесь тупим... зарегестрировали только класс (модель) Question, а объявили в models.py,
# что есть еще и класс (модель) Choice, регестрируем её тоже...