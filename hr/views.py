from django.shortcuts import render, redirect
from .forms import CandidateForm  # QuestionsForm
from .models import Question, Candidate, Jedi
from django.core.mail import send_mail


def main_list(request):
    return render(request, 'hr/candidate/main.html')


def candidate_create(request):
        # Создание профиля кондидата.
    if request.method == 'POST':
        # Форма отправлена на сохранение
        form = CandidateForm(request.POST)
        if form.is_valid():
            form.save()
            # Перенаправляем учитывая пространство имен в urls
            return redirect('hr:questions')
    else:
        form = CandidateForm()
        return render(request, 'hr/candidate/create.html', {'form': form})


def questions(request):
    # Получаем все вопросы и отправляем в шаблон
    questions = Question.objects.all()
    return render(request, 'hr/candidate/questions.html',
                  {'questions': questions})


def tested(request):
    # Получаем результат теста
    result = request.POST
    # Вырезаем csrf_token
    new_result = result.copy()
    del new_result['csrfmiddlewaretoken']
    # Cловарь для сохранения результата
    list_result = []
    for k, v in new_result.items():
        list_result.append(v)
    # Подсчет правельных ответов
    list_int = [int(item) for item in list_result]
    count = 0
    for i in list_int:
        if i == 1:
            count += 1
    # Делаем из списка строку, чтобы сохранить в БД
    result_str = ''.join(list_result)
    # Если количество правельных ответов больше или равно 2, тест пройден
    if count >= 2:
        qs = Candidate.objects.order_by('-id')[:1][0]
        qs.tested = True
    # Пихаем в новую модель пользователя и его ответы,
    # которые мы будем доставать для джедаев
        qs.result = result_str
        qs.save()
    return render(request, 'hr/candidate/main.html')


def jedi_list(request):
    # Отображаем для выбора всех ДЖЕДАЕВ.
    jedis = Jedi.objects.all()
    return render(request, 'hr/candidate/jedi.html',
                  {'jedis': jedis})


def candidate_list(request):
    result_dict = request.POST
    # Получаем id выбранного ДЖЕДАЯ
    result = int(result_dict['jedi'])
    # Получаем список кандидатов для ДЖЕДАЯ
    real_candidate_obj = Candidate.objects.filter(
        planet=Jedi.objects.get(id=result).planet,
        tested=True).exclude(status_padavan=True)
    # Вытаскиваем ответы кандидатов
    answ = []
    for candidate in real_candidate_obj:
        answ.append(list(candidate.result))

    return render(request, 'hr/candidate/candilist.html',
                  {'candidats': real_candidate_obj, 'answ': answ})


def inpadavan(request):
    # Получаем id кандидатов для зачисление в падаваны
    result = request.POST
    # Вырезаем csrf_token
    new_result = result.copy()
    del new_result['csrfmiddlewaretoken']
    # Установка статуса ПАДАВАН
    for i in new_result:
        qs = Candidate.objects.get(id=i)
        qs.status_padavan = True
        # Результат успешной отправки выводим в консоль
        # через EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
        # в settings.py
        send_mail('You Padavan!', 'This e-mail was sent with Jedi.',
                  'jedi@gmail.com', [qs.email], fail_silently=False)
        qs.save()

    return render(request, 'hr/candidate/main.html')
