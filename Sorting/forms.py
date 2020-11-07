from django import forms
import random
from django.contrib.postgres.forms import SimpleArrayField
#from django.contrib.postgres.forms import SimpleArrayField
from .models import ArrModel

class ArrForm(forms.ModelForm):
    class Meta:
        model = ArrModel
        fields = [
            'length',
            'max_val',
            'min_val',
            'arr',
        ]
        labels = {
            'length' : 'Length array',
            'max_val' :'Max value',
            'min_val': 'Min value',
            'arr': 'Array',
        }
        widget = {
            'length': forms.TextInput(attrs={'class': 'form-control'}),
            'max_val': forms.TextInput(attrs={'class': 'form-control'}),
            'min_val': forms.TextInput(attrs={'class': 'form-control'}),
            'arr': forms.TextInput(attrs={'class': 'form-control'})
        }


# intialize form which is not link to any modle
# class ArrForm (forms.Form):

#     length = forms.IntegerField(max_value=100, min_value=1)
#     max_val = forms.IntegerField(max_value=100, min_value=0)
#     min_val = forms.IntegerField(max_value=100, min_value=0)
#     arr = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={'size':70}))
#     sorted_arr = SimpleArrayField(SimpleArrayField(forms.IntegerField(required=False), required=False), delimiter='|', required=False)
#     # initialize initial value of elements
#     def __init__(self, *args, **kwargs):
#         updated_initial = {}
#         length = 5
#         max_val = 100
#         min_val = 0
#         updated_initial['length'] = length
#         updated_initial['max_val'] = max_val
#         updated_initial['min_val'] = min_val
#         arr = []
#         for i in range(0, length):
#             arr.append(random.randrange(min_val, max_val))
#         updated_initial['arr'] = arr
#         # initialize sorted_arr
#         # ar = []
#         # ar.append(arr)
#         # ar.append(arr)
#         # print("init arr",ar)
#         # s = self.convertArr2Str(ar)
#         # print( "s is",s)
#         # updated_initial['sorted_arr'] = s
#         kwargs.update(initial=updated_initial)
#         super(ArrForm, self).__init__(*args, **kwargs)


