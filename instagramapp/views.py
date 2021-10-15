from django.shortcuts import render,redirect
from django.forms.widgets import DateTimeInput
from django.http.response import HttpResponse, HttpResponseRedirect
from instagramapp.models import Comment, Image, Profile
from instagramapp.forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def homepage(request):
    """
    View function to display homepage content
    """
    posts = Image.objects.all()
    profile = Profile.objects.all()
    comment = Comment.objects.all()

    return render(request, 'all-templates/home.html',{"posts":posts,"profile":profile,"comment":comment})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
            user = User.objects.create_user(username=username, email=email,password=password)
            return HttpResponse('Thank you for registering with us')
    else:
        form = SignUpForm()
    return render(request, 'registration_form.html', {'form': form})

@login_required(login_url='/accounts/login/')
def search(request): 
    if 'profile' in request.GET and request.GET['profile']:
        user = request.GET.get("profile")

        print(user)
        results = Profile.search_profile(user)
        message = f'profile'
        return render(request, 'all-templates/search.html',{'profiles': results,'message': message})
    else:
        message = "You haven't entered anything to search. Please enter a user profile to search."
    return render(request, 'all-templates/search.html', {'message': message})