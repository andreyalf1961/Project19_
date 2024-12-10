from django.shortcuts import render
from .forms import UserRegister
from .models import *
from django.core.paginator import Paginator


def news(request):
    pagename = 'Новости'
    news_ = News.objects.all().order_by('-date')
    print(news_)
    paginator = Paginator(news_, 3)
    print(paginator)
    page_number = request.GET.get('page')
    print(page_number)
    page_obj = paginator.get_page(page_number)
    print(page_obj)
    return render(request, 'news.html',
                  {'pagename': pagename, 'page_obj': page_obj})


def platform(request):
    pagename = 'Главная страница'
    context = {'pagename': pagename}
    return render(request, 'platform.html', context)


def shop(request):
    pagename = 'Игры'
    games = Game.objects.all()
    context = {'pagename': pagename, 'games': games}
    return render(request, 'games.html', context)


def cart(request):
    pagename = 'Корзина'
    context = {'pagename': pagename}
    return render(request, 'cart.html', context)


# Регистрация
def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if Buyer.objects.filter(name=username).exists():
                info['error'] = 'Пользователь уже существует'
                return render(request, 'registration_page.html', {'error': info['error']})
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return render(request, 'registration_page.html', {'error': info['error']})
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
                return render(request, 'registration_page.html', {'error': info['error']})
            else:
                info['welcome'] = f'Приветствуем, {username}!'
                Buyer.objects.create(name=username, balance=10000, age=age)
                return render(request, 'registration_page.html', {'welcome': info['welcome']})

    else:
        form = UserRegister()
    return render(request, 'registration_page.html', {'form': form})


def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if Buyer.objects.filter(name=username).exists():
            info['error'] = 'Пользователь уже существует'
            return render(request, 'registration_page.html', {'error': info['error']})
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
            return render(request, 'registration_page.html', {'error': info['error']})
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
            return render(request, 'registration_page.html', {'error': info['error']})
        else:
            info['welcome'] = f'Приветствуем, {username}!'
            Buyer.objects.create(name=username, balance=10000, age=age)
            return render(request, 'registration_page.html', {'welcome': info['welcome']})

    return render(request, 'registration_page.html')


from django.shortcuts import render
