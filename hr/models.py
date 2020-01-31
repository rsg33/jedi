from django.db import models


class Planet(models.Model):
    planet = models.CharField(max_length=25, verbose_name='Планета')

    class Meta:
        verbose_name = 'Планета'
        verbose_name_plural = 'Планеты'
        ordering = ('planet',)

    def __str__(self):
        return self.planet


class Candidate(models.Model):
    name_c = models.CharField(max_length=25, verbose_name='Имя')
    planet = models.ForeignKey(
        Planet, on_delete=models.CASCADE, verbose_name='Планета')
    age = models.IntegerField(verbose_name='Возраст')
    email = models.EmailField(verbose_name='E-mail')
    result = models.CharField(max_length=254, blank=True,
                              verbose_name='Варианты ответов')
    tested = models.BooleanField(default=False, verbose_name='Протестирован?')
    status_padavan = models.BooleanField(default=False, verbose_name='Падаван')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Кандидат'
        verbose_name_plural = 'Кандидаты'
        ordering = ('-created',)

    def __str__(self):
        return self.name_c


class Jedi(models.Model):
    name_j = models.CharField(max_length=20, verbose_name='Имя')
    planet = models.ForeignKey(
        Planet, on_delete=models.CASCADE, verbose_name='Планета')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Джедай'
        verbose_name_plural = 'Джедаи'
        ordering = ('-created',)

    def __str__(self):
        return self.name_j


class Question(models.Model):
    question = models.TextField(max_length=50, verbose_name='Вопрос')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ('created',)
    def __str__(self):
        return self.question
