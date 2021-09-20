import traceback
import traceback

from django.shortcuts import render, redirect

from rest_framework.decorators import api_view
from rest_framework.response import Response

from urlreducer.helpers.url_encode_decode import encode_url, get_redirect_url

@api_view(['GET'])
def get_encoder_page(request):
    try:
        return render(request, 'encode-url.html', context={'hostname': request.META['HTTP_HOST']}, content_type='text/html')
    except:
        traceback.print_exc()
        resp = {'message': 'Something went wrong!'}
        return Response(resp, 500)

@api_view(['POST'])
def get_encoded_url(request):
    try:
        if('url' not in request.data.keys()):
            resp = {'message': 'No url found to encode'}
            return Response(resp, 422)
        
        encoded_url = request.META['HTTP_HOST']+'/redurl/decode/'+str(request.data['userId'])+'/'+encode_url(int(request.data['userId']), str(request.data['url']))
        print(encoded_url)
        return Response({'urlEncoded': encoded_url}, 200)
    except:
        traceback.print_exc()
        resp = {'message': 'Something went wrong!'}
        return Response(resp, 500)

@api_view(['GET'])
def decode_url_and_redirect(request, userId, encodedUrl):
    try:
        red_url = get_redirect_url(userId, encodedUrl)
        print(red_url)
        return redirect(red_url)
    except:
        traceback.print_exc()
        resp = {'message': 'Something went wrong!'}
        return Response(resp, 500)