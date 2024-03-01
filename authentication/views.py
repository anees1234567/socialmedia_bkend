import json
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
# Create your views here.


def login_view(request):
    if request.method == 'POST':

        body_unicode = request.body.decode('utf-8')
        body_data = json.loads(body_unicode)
        username = body_data.username
        password = body_data.get('password')
        user=username
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # login(request, user)
            return JsonResponse({'message': user + ' Login successful'}, status=200)
        else:
            return JsonResponse({'message': 'Invalid username or password'}, status=400)
    else:
        return JsonResponse({'message': 'Only POST requests are allowed'}, status=405)