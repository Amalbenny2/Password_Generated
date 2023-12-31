from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User




def generate_password():
    return User.objects.make_random_password()


class SignUpView(TemplateView):
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CustomUserCreationForm()
        return context

    def post(self, request, *args, **kwargs):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Process the form data, save the user, etc.
            # You might want to redirect to a success page or perform other actions
            return redirect('home')  # Assuming 'home' is the name of your home page URL pattern
        else:
            # If the form is not valid, re-render the template with the form
            context = {'form': form}
            return render(request, self.template_name, context)



def home(request):
    return render(request, 'home.html')