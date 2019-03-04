from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm

# Create your views here.
def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account has now been created! Please login to verify.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'user/registration.html', {'form': form})
