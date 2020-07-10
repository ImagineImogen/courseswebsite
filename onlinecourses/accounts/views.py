from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .forms import RegistrationForm
from .models import UserRegistrationToken, Profile


def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            site = get_current_site(request)
            user = form.save(commit=False)
            user.is_active = False
            user.profile = Profile(user=user)
            user.profile.bio  = "default description"
            user.save()
            token = UserRegistrationToken.objects.create(user=user)
            username = form.cleaned_data.get('username')
            message = render_to_string('email_activation.html', {
                'user': username,
                'domain': site.domain,
                'token': token
            })
            send_mail("Confirm your email", message, "lieschen.yakov@gmail.com", [user.email, ])
            html = "<html><body>The activation link was sent to  %s. Please confirm your email</body></html>" % user.email
            return HttpResponse(html, content_type='text/html')
        else:
            return render(request, 'signup.html', {'form': form})

    else:
        form = RegistrationForm()
    return render(request, 'signup.html', {'form': form})


def activation(request):
    if request.method == 'GET':
        token = request.GET.get('token')
        try:
            activation = UserRegistrationToken.objects.get(token=token)
        except UserRegistrationToken.DoesNotExist:
            raise Http404 ("Something went wrong")
        user = activation.user #returns the User object
        user.is_active = True
        user.save()
        return HttpResponse('<html><body>You successfully activated your account. You can log in now</body></html>')#TODO separate template
