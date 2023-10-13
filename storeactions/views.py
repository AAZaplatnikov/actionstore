from django.shortcuts import render,redirect
from .models import ActionStore
from .forms import ActionsStoreForm
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm

# Create your views here.
def first_page(request):
    object_list=ActionStore.objects.all()
    form = ActionsStoreForm()

    return render(request, './index.html', { 'object_list': object_list,
                                            'form': form })
class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
def report(request):
    object_list=ActionStore.objects.all()
    return render(request, './report.html', { 'object_list': object_list})

def thanks(request):
    action_zone = request.POST['action_zone']
    Action_tipe= request.POST['Action_tipe']
    numbers_clips= request.POST['numbers_clips']
    cost= request.POST['cost']

    element = ActionStore(action_zone = action_zone , Action_tipe=Action_tipe, numbers_clips=numbers_clips, cost=cost)
    element.save()
    return render(request, './Thanks.html',{ 'action_zone': action_zone,
                                             'Action_tipe': Action_tipe,
                                             'numbers_clips': numbers_clips,
                                             'cost': cost})


# def my_view(request):
#     username = None
#     if request.user.is_authenticated:
#         username = request.user.username
#     return render( {'username': username})

# def feedback_view(request):
#     if request.method == 'POST':
#         form = ActionsStoreForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('report.html')
#     else:
#         form = ActionsStoreForm()
#     return render(request, 'report.html', {'form': form})