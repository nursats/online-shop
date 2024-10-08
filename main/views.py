from typing import Any
from django.http import HttpResponse
from django.shortcuts import render
from goods.models import Categories
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['title'] = 'Home - shop'
        context['content'] = 'Магазин мебели HOME'
        return context

class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['title'] = 'home about us'
        context['content'] = 'О нас'
        context['text_on_page'] = 'Текст почему наш магазин такой хороший'
        return context
 



# def index(request):

#     context = {
#         'title':'Home - Главная',
#         'content':'Магазин мебели HOME',
#     }
#     return render(request, 'main/index.html',context)


# def about(request):
#     context = {
#         'title':'Home - О нас',
#         'content':'О нас',
#         'text_on_page':'Текст почему наш магазин такой хороший '
#     }
#     return render(request, 'main/about.html',context)