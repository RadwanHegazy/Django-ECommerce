from django.core.mail import EmailMessage
from django.shortcuts import render
from django.conf import settings

def send_reset_password_email (otp_code, to_user_email) : 

    # Construct the email message
    subject = 'Your OTP Code'
    body = f"""
        <h1>Your OTP Code</h1>
        <p>Your one-time password (OTP) code is:</p>
        <h2 style="font-size: 36px; font-weight: bold; color: #0077b6;">{otp_code}</h2>
        <p>Please enter this code to verify your identity.</p>
    
    """
    email_message = EmailMessage(
        subject=subject,
        body=body,
        from_email=settings.EMAIL_HOST_USER,
        to=[to_user_email],
    )
    email_message.content_subtype = 'html'
    email_message.send()
