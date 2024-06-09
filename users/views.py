from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.views import LoginView, PasswordResetView

"""class CustomLoginView(LoginView):
    def get(self, request, *args, **kwargs):
        link_clicked = request.session.get('forgot-link')
        if link_clicked == "true_forgot":
            request.session['reset_clicked'] = True
            print("Reset link clicked!")
        else:
            pass
        return super().get(request, *args, **kwargs) 
class CustomPasswordResetView(PasswordResetView):
     def get(self, request, *args, **kwargs):
        if request.session.get('reset_clicked') == True:
            request.session['reset_clicked'] = False
        else:
            return redirect('login')"""

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Your account has been created!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)



    context = {
        'u_form': u_form,
        'p_form': p_form
  
    }

    return render(request, 'users/profile.html', context)
