from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'login.html')

def login(request):
    # if(request.Method=="POST")
    # check if user has entered with correct credentials
    return render(request, 'Login.html')

def logout(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'Signup.html')

def user(request):
    return render(request, 'WhoAmI.html')

def ngoform(request):
    return render(request, 'NGOform.html')

def hospitalform(request):
    return render(request, 'Hospitalform.html')

def userform(request):
    return render(request, 'Userform.html')

def bloodbankform(request):
    return render(request, 'Bloodbankform.html')

def hospitalInterface(request):
    return render(request, 'HospitalInterface.html')

