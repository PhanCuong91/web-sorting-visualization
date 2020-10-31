from django import forms
import random
#from django.contrib.postgres.forms import SimpleArrayField


class ArrForm (forms.Form):

    length = forms.IntegerField(max_value=100, min_value=1)
    max_val = forms.IntegerField(max_value=100, min_value=0)
    min_val = forms.IntegerField(max_value=100, min_value=0)
    arr = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'size':70}))

    # initialize initial value of elements
    def __init__(self, *args, **kwargs):
        updated_initial = {}
        length = 5
        max_val = 100
        min_val = 0
        updated_initial['length'] = length
        updated_initial['max_val'] = max_val
        updated_initial['min_val'] = min_val
        arr = []
        for i in range(0, length):
            arr.append(random.randrange(min_val, max_val))
        updated_initial['arr'] = arr
        kwargs.update(initial=updated_initial)
        super(ArrForm, self).__init__(*args, **kwargs)
