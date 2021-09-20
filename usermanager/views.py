import traceback
from datetime import datetime

from django.shortcuts import render
from django.db.models import Q

from rest_framework.decorators import api_view
from rest_framework.response import Response

from usermanager.models import UserRegistry

@api_view(['GET'])
def homepage(request):
    try:
        return render(request, 'register-login.html', content_type='text/html')
    except:
        traceback.print_exc()
        return Response({'message': 'Something went wrong'})


@api_view(['POST'])
def register_user(request):
    try:
        if('email' not in request.data.keys()):
            resp = {'message': 'User Email is required'}
            return Response(resp, 422)

        if('password' not in request.data.keys()):
            resp = {'message': 'Password is required'}
            return Response(resp, 422)

        if UserRegistry.objects.filter(email=request.data['email']).exists():
            resp = {'message': 'User already exists'}
            return Response(resp, 422)

        UserRegistry.objects.create(email=request.data['email'], password=request.data['password'], created_on=datetime.now())
        resp = {'message': 'User registered successfully'}
        return Response(resp, 200)
    except:
        traceback.print_exc()
        return Response({'message': 'Something went wrong'})

@api_view(['POST'])
def login_user(request):
    try:
        if('email' not in request.data.keys()):
            resp = {'message': 'User Email is required'}
            return Response(resp, 422)

        if('password' not in request.data.keys()):
            resp = {'message': 'Password is required'}
            return Response(resp, 422)

        if not UserRegistry.objects.filter(email=request.data['email']).exists():
            resp = {'message': 'User does not exist'}
            return Response(resp, 422)

        if not UserRegistry.objects.filter(Q(email=request.data['email']) & Q(password=request.data['password'])).exists():
            resp = {'message': 'Invalid credentials'}
        else:
            user_id = UserRegistry.objects.get(email=request.data['email']).pk
            resp = {'message': 'Login successful', 'userId': user_id}
        
        return Response(resp, 200)
    except:
        traceback.print_exc()
        return Response({'message': 'Something went wrong'})

