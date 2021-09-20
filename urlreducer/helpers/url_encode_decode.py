import time
from datetime import datetime
from hashlib import blake2b
import traceback
import json

from django.db.models import Q
from django.core import serializers

from urlreducer.models import URLRegistry


def encode_url(user_id, url):
    try:
        def create_hash(url):
            h = blake2b(digest_size=24, key=str(int(time.time())).encode('utf-8'))
            h.update(str(str(user_id)+url).encode('utf-8'))
            return h.hexdigest()

        enc_url = create_hash(url)
        while(URLRegistry.objects.filter(Q(issued_to=user_id) & Q(encoded_url=enc_url)).exists()):
            enc_url = create_hash(url)
        
        URLRegistry.objects.create(redirect_url=url, encoded_url=enc_url, issued_to=user_id, added_on=datetime.now())
        return enc_url
    except:
        traceback.print_exc()
        return False

def get_redirect_url(user_id, url):
    if URLRegistry.objects.filter(Q(issued_to=user_id) & Q(encoded_url=url)).exists():
        d = URLRegistry.objects.filter(Q(issued_to=user_id) & Q(encoded_url=url))
        d = json.loads(serializers.serialize('json', d))[0]
        return d['fields']['redirect_url']
    else:
        return None