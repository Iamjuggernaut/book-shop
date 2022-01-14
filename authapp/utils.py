from django.urls import reverse
from django.conf import settings
from django.core.mail import send_mail

def send_verify_mail():
    verify_link = reverse('auth:verify',args=[user.email, user.activation_key])

    title = f'Cofirmation of {user.username}'

    message = f"to confirm {user.username}'s account click here: \n{settings.DOMAIN_NAME}{verify_link}"

    return send_email(title, message, settings.EMAIL_HOST_USER, [user_email], fail_silently=False)