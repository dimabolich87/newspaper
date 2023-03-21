# Импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from django.views.generic import ListView, DetailView
from django_filters.views import FilterView

from .filters import NewsFilter
from .models import Post


class Postlist(ListView):
    # модель, объекты которой мы будем выводить
    model = Post
    # Поле, которое будет использоваться для сортировки объектов
    ordering = '-date_time_post'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'news.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'news'
    paginate_by = 10 #  количество записей на странице

class PostDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Post
    # Используем другой шаблон — onenews.html
    template_name = 'onenews.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'onenews'

class SearchNews(FilterView):
    model = Post
    filterset_class = NewsFilter
    template_name = 'search.html'
    paginate_by = 10
    context_object_name = 'search'