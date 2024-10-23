from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import News

class NewsList(ListView):
    model = News
    ordering = 'title_news'
    template_name = "flatpages/news.html"
    context_object_name = 'news'

    def get_context_data(self, news=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['next_sale'] = None
        return context

class NewsDetail(DetailView):
    model = News
    template_name = 'flatpages/news_id.html'
    context_object_name = 'news_id'



