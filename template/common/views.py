from django.shortcuts import render, redirect
from .forms import SignupForm

# Create your views here.
def index(request):
    print("Render homepage")
    return render(request, 'common/index.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login')

    else:
        form = SignupForm()

    return render(request, 'common/signup.html', { 'form': form } )
