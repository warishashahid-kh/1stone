# signup/loginapp/views.py



from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt # Still useful for API-like endpoints, but less critical here
import json
import re
from django.shortcuts import render

def login_view(request):
    """
    Handles login requests.
    - If POST, processes form data, validates email, and prepares messages.
    - If GET, renders the login form.
    """
    message = None
    message_type = None # 'success' or 'danger'

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        print(f"Received login attempt (from form submission):")
        print(f"  Email: {email}")
        print(f"  Password: {password}") # WARNING: In a real app, never print passwords!

        # Basic email validation
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not email or not re.match(email_regex, email):
            message = 'Invalid email format.pease check your email address.'
            message_type = 'danger'
        else:
            message = 'Login data received and email format is valid.'
            message_type = 'success'

        return render(request, 'loginapp/login.html', {
            'message': message,
            'message_type': message_type
        })

    else:
        return render(request, 'loginapp/login.html')

