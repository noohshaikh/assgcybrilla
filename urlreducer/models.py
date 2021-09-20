from django.db import models

# Create your models here.
class URLRegistry(models.Model):
    class Meta:
        app_label = 'urlreducer'
        db_table = 'url_registry'

    redirect_url = models.TextField(null=False)
    encoded_url = models.TextField(null=False)
    issued_to = models.TextField(null=False)
    added_on = models.DateTimeField(null=False)

