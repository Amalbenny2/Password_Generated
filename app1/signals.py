from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
import random
import string

@receiver(post_save, sender=get_user_model())
def send_password(sender, instance, created, **kwargs):
    if created:
        # Generate a strong and secure password
        generated_password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))

        # Set the generated password for the user
        instance.set_password(generated_password)
        instance.save()

        # Send the generated password via email
        subject = 'Your Account Information'
        message = f'Hello {instance.username},\n\nYour password is: {generated_password}\n\nThank you for registering!'
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = [instance.email]
        send_mail(subject, message, from_email, to_email)
