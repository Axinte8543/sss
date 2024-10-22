from datetime import date
from django.shortcuts import render #Importă funcția render din modulul django.shortcuts. Render este folosit pentru a afișa șabloane HTML.
from aplicatie.models import Topic, Webpage,AccessRecord #Importă modelul Produs din aplicația ta.
from . import forms 
from aplicatie.forms import NewUserForm, UserProfileInfoForm

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

def index(request):
    return HttpResponse("Primul raspuns")

def pag1(request):
    return HttpResponse(2 + 3)

l = []
def pag2(request):
    global l
    a = request.GET.get("b", 10)
    print(request.GET)
    l.append(a)
    return HttpResponse(f"<b>Am primit</b>: {l}")
ct=0
def pag3(request):
    global ct
    ct+=1
    return HttpResponse(f"<b>Am accesat pagina de {ct} ori</b>")
suma=0
def pag4(request):
    global suma
    c=request.GET.get("a",0)
    b=request.GET.get("b",0)
    c=int(c)
    b=int(b)
    suma=c+b
    return HttpResponse(f"<b>Suma este</b>: {suma}")
l1=[]
def pag5(request):
    global l1
    text=request.GET.get("text")
    if text and text.isalpha():
        l1.append(text)
    response_text = "".join(f"<p>{item}</p>" for item in l1)
    return HttpResponse(response_text)
def pag6(request):
    num_params = len(request.GET)
    response_text = f"Numărul de parametri primiți este: {num_params}"
    return HttpResponse(response_text)
def pag8(request):
    matrice = [
        ["A1", "B1", "C1", "D1"],
        ["A2", "B2", "C2", "D2"],
        ["A3", "B3", "C3", "D3"]
    ]
    tabel_html = "<table border='1'>"
    for rand in matrice:
        tabel_html += "<tr>"
        for celula in rand:
            tabel_html += f"<td>{celula}</td>"
        tabel_html += "</tr>"
    tabel_html += "</table>"
    return HttpResponse(tabel_html)
numarfinal=0
def pag7(request):
    global numarfinal
    try:
        a=int(request.GET.get("a",0))
        b=int(request.GET.get("b",0))
    except ValueError:
        return HttpResponse("Parametrii nu sunt numere întregi.", status=400)    
    calcul=request.GET.get("calcul")
    if calcul=="sum":
        numarfinal=a+b
    elif calcul=="dif":
        numarfinal=a-b
    elif calcul=="mul":
        numarfinal=a*b
    elif calcul=="div":
        if b == 0:
            return HttpResponse("Divizarea prin zero nu este permisă.", status=400)
        numarfinal=a/b
    elif calcul=="mod":
        if b == 0:
            return HttpResponse("Divizarea prin zero nu este permisă.", status=400)
        numarfinal=a%b
    else:
        return HttpResponse("Operația specificată nu este validă.", status=400)    
    return HttpResponse(f"<b>Rezultatul este</b>: {numarfinal}")   
def mesaj(request):
    return HttpResponse("Buna ziua!")
def data(request):
    return HttpResponse("Astazi este " + str(date.today()))

def index1(request):
    my_dict={"insert_me":"Acum sunt în first_app/index.html!"} 
    return render(request, "first_app/index.html",context=my_dict) 

def index2(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':webpages_list} 
    return render(request, 'first_app/index2.html', context=date_dict) 
    
def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("VALIDATION SUCCESS!")
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: "+form.cleaned_data['email'])
            print("TEXT: "+form.cleaned_data['text'])
    return render(request, 'first_app/form_page.html', {'form': form})    

def users1(request):    
    return render(request, 'first_app/users.html')

def users(request):
    form = NewUserForm() #Crează un obiect NewUserForm
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True) #Salvează datele în baza de date a aplicației
            return users1(request) #Redirecționează utilizatorul către pagina users1
        else:
            print('ERROR FORM INVALID')
    return render(request, 'first_app/users.html', {'form': form}) #Returnează șablonul users.html și formularul NewUserForm

def relative(request):
    return render(request, 'first_app/relative_url_templates.html')

def base(request):
    return render(request, 'first_app/baseextension.html')

def ceva(request):
    context_dict={'text':'hello world','number':100}
    return render(request,'first_app/exemplu.html',context=context_dict)

def register(request):
    registered = False 
    
    if request.method == 'POST': 
        user_form = NewUserForm(data=request.POST) 
        profile_form = UserProfileInfoForm(data=request.POST) 
        
        if user_form.is_valid() and profile_form.is_valid(): 
            user = user_form.save() 
            user.set_password(user.password) 
            user.save() 
            
            profile = profile_form.save(commit=False) 
            profile.user = user 
            
            if 'profile_pic' in request.FILES: 
                profile.profile_pic = request.FILES['profile_pic'] 
                
            profile.save() 
            
            registered = True 
        else:
            print(user_form.errors,profile_form.errors) 
            
    else:
        user_form = NewUserForm()
        profile_form = UserProfileInfoForm()
                      
    return render(request,'first_app/registration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered}) 

@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed!")
            print("Username: {} and password {}".format(username, password))
            return HttpResponse("invalid login details supplied!")
    else:
        return render(request, 'first_app/login.html', {})