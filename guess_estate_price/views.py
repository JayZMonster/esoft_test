from django.shortcuts import render
from django.views import View

from .forms import HandForm, ImportForm
from .services.ml_predict import predict, predict_csv

# Create your views here.


class MainView(View):

    @staticmethod
    def get(request):
        context = {}
        return render(request, "guess_estate_price/base.html", context=context)


class HandInput(View):

    @staticmethod
    def get(request):
        context = {'form': HandForm()}
        return render(request, "guess_estate_price/hand.html", context=context)

    @staticmethod
    def post(request):
        predicts = predict(request.POST)
        print(predicts)
        context = {'answer': round(predicts[0], 2)}
        return render(request, "guess_estate_price/hand.html", context=context)


class ImportInput(View):

    @staticmethod
    def get(request):
        context = {'form': ImportForm()}
        return render(request, "guess_estate_price/import.html", context=context)

    @staticmethod
    def post(request):
        file = request.FILES['file']
        predicts = predict_csv(file)

        context = {'answer': [round(pred, 2) for pred in predicts[0]]}
        return render(request, "guess_estate_price/hand.html", context=context)
