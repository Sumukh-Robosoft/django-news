from django.core.mail import send_mail
from django.conf import settings

def send_login_credentails(email,username,password):
    try:
        subject = 'Djnago email sending'
        message = f'Your Login credentails are\n username = {username} ,\n password = {password} \nplease click here to login http://127.0.0.1:8000/'
        email_from = settings.EMAIL_HOST
        send_mail(subject, message, email_from, [email])
        
        
    except Exception as e:
        return e