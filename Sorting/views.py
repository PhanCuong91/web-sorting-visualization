from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import View
import random
from .forms import ArrForm

# Create your views here.


class HomeView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        context['form'] = ArrForm()
        return render(request, 'chart.html', context)

    def post(self, request, *args, **kwargs):
        form = ArrForm(request.POST or None)
        if form.is_valid():
            # get the value of element in form
            # must use clean data because form is an object
            length = form.cleaned_data.get('length')
            max_val = form.cleaned_data.get('max_val')
            min_val = form.cleaned_data.get('min_val')
            arr = []
            for i in range(0, length):
                arr.append(random.randrange(min_val, max_val))
            # create dictionary which contain the updated value of form
            data = {
                'length': length,
                'max_val': max_val,
                'min_val': min_val,
                'arr': arr
            }
            # updated elements of form to chart.html
            f = ArrForm(data)
            return render(request, 'chart.html', {"form": f})

# using for ajax in chart.html
def get_data(request, *args, **kwargs):
    i = 0
    d = [random.randrange(0, 20)]
    while i < 4:
        d.append(random.randrange(0, 20))
        i += 1
    labels = ["Blue", "Yellow", "Green", "Purple", "Orange"]
    default_items = d

    print(default_items)
    d = request.POST.get('out')
    print(d)
    data = {
        "labels": labels,
        "default": default_items,
    }
    return JsonResponse(data)

