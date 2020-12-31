from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse
from django.http import HttpResponse

from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator

from notifications.signals import notify

from .models import Account
from .forms import RegistrationForm

UserModel = Account

def registrationView(request):
    form = RegistrationForm()

    '''if request.method == 'GET':
        return render(request, 'registration/register.html')'''
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('registration/acc_activate_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = RegistrationForm()
        return render(request, 'registration/register.html', {'form': form})
    '''else:
        return render(request, 'registration/register.html')'''


def approve(request, id):
    user = Account.objects.get(id = id)
    print(user.email_confirmed, user.email)
    user.is_active = True
    user.save()
    return render(request, 'index.html')

def accountNotApproved():
    not_active = Account.objects.filter(is_active=False, email_confirmed=True)
    return not_active

'''def notify(user):
    users = Account.objects.all()
    for usr in users:
        if usr.is_staff or usr.is_batchCoordinator:
            notify.send(user, recipient=usr, verb='waiting for approval')'''


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.email_confirmed = True
        user.save()

        if user.email_confirmed and user.is_active == False:
            #notify(request.user)
            '''for usr in users:
                if usr.is_staff or usr.is_batchCoordinator :
                    notify.send(request.user, recipient=usr, verb='waiting for approval' )'''
        return HttpResponse('Thank you for your email confirmation. W8 for the account approval.')
    else:
        return HttpResponse('Activation link is invalid!')

class RegistrationView(CreateView):
    template_name = 'registration/register.html'
    form_class = RegistrationForm

    def get_context_data(self, *args, **kwargs):
        context = super(RegistrationView, self).get_context_data(*args, **kwargs)
        context['next'] = self.request.GET.get('next')
        return context

    def get_success_url(self):
        next_url = self.request.POST.get('next')
        success_url = reverse('login')
        if next_url:
            success_url += '?next={}'.format(next_url)

        return success_url


@login_required(login_url= '/accounts/login/')
def home(request):
    not_active = accountNotApproved()
    return render(request, 'index.html', {'not_approve': not_active})


class ProfileView(UpdateView):
    model = Account
    fields = ['name', 'phone', 'date_of_birth', 'picture']
    template_name = 'registration/profile.html'

    def get_success_url(self):
        return reverse('index')

    def get_object(self):
        return self.request.user

