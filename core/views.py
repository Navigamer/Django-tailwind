from django.views.generic import TemplateView, View
from django.shortcuts import redirect, render, get_list_or_404
from django.core.paginator import Paginator

app_name = "core"

class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {

        }
        return render(request, 'pages/index.html', context)