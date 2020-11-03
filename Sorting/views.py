from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import View
import random
from .forms import ArrForm
from .models import ArrModel
from .sortings import Sortings
import time
from .tasks import update_arr, schedule
from django.forms.models import model_to_dict

# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        form = ArrForm()
        arr = []
        return render(request, 'chart2.html', {'form':form, 'arr': arr})

    def post(self, request, *args, **kwargs):
        form = ArrForm(request.POST)
        if form.is_valid():
            # get the value of element in form
            # must use clean data because form is an object
            length = form.cleaned_data.get('length')
            print("length: ",length)
            max_val = form.cleaned_data.get('max_val')
            min_val = form.cleaned_data.get('min_val')
            sorted_arr = form.cleaned_data.get('sorted_arr')
            print("sort arr: ",sorted_arr)
            # create dictionary which contain the updated value of form
            data = {
                'length': length,
                'max_val': max_val,
                'min_val': min_val,
            }
            arr = Support.randomArr(length, max_val, min_val)
            step_arr = Sortings.selection_sort(arr)
            f = ArrForm(data)
            return JsonResponse({ 'arr': step_arr}, status=200)
            
class SelectionView(View):
    def post(self, request, *args, **kwargs):
        form = ArrForm(request.POST)
        if form.is_valid():
            # get the value of element in form
            # must use clean data because form is an object
            length = form.cleaned_data.get('length')
            print("length: ",length)
            max_val = form.cleaned_data.get('max_val')
            min_val = form.cleaned_data.get('min_val')
            sorted_arr = form.cleaned_data.get('sorted_arr')
            print("sort arr: ",sorted_arr)
            # create dictionary which contain the updated value of form
            data = {
                'length': length,
                'max_val': max_val,
                'min_val': min_val,
            }
            arr = Support.randomArr(length, max_val, min_val)
            step_arr = Sortings.selection_sort(arr)
            f = ArrForm(data)
            return JsonResponse({ 'arr': step_arr}, status=200)

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


class Support:

    def convertStr2Arr( s):
        s = s.lstrip("[")
        s = s.rstrip("]")
        s = s.split(", ")
        arr = []
        for i in range(0,len(s)):
            arr.append(int(s[i]))
        return arr

    def randomArr(length, max_val, min_val):
        arr = []
        for i in range(0, length):
            arr.append(random.randrange(min_val, max_val))
        return arr
    
    def convertArr2Str(arr):
        if (len(arr) == 0):
            return 'None'
        s =''
        for i in range(len(arr)):
            if(i>0):
                s+='|'
            for j in range(len(arr[0])):
                s += str(arr[i][j])
                if j<len(arr[0])-1:
                    s+=','
        return s
    


# test celery
def update(request):
    schedule.delay(3)
    return render(request, 'test.html')
