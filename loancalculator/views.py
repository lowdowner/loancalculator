from django.shortcuts import render
from django.views import View
from .forms import InvestmentForm


class Index(View):
    def get(self, request):
        form = InvestmentForm()
        return render(request, 'loancalculator/index.html', {'form': form})

    def post(self, request):
        pass