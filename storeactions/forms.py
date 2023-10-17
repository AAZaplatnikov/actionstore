from django import forms
from .models import ActionStore
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class ActionsStoreForm(forms.Form):
    # class Meta:
    #     model = ActionStore
    #     fields = ['actionSt_dt', 'action_zone','Action_tipe', 'numbers_clips','cost']

    action_zone = forms.CharField(max_length=100, label='Зона')
    Action_tipe = forms.CharField(max_length=100,label='Тип активности' )
    numbers_clips = forms.CharField(max_length=100,label='Количество клипс' )
    cost = forms.CharField(max_length=100,label='Сумма, руб', required = False)
#    storenumber = forms.CharField(max_length=100)


# actionSt_dt = models.DateTimeField(auto_now=True)
# action_zone = models.CharField(max_length=100)
# Action_tipe = models.CharField(max_length=100)
# numbers_clips = models.CharField(max_length=100)
# cost= models.CharField(max_length=100)




class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label=" Номер ", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Пароль ", max_length=30,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))
