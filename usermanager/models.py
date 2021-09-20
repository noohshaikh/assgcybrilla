from django.db import models

# Create your models here.
class UserRegistry(models.Model):
    class Meta:
        app_label = 'urlreducer'
        db_table = 'user_registry'
    
    email = models.TextField(null=False)
    password = models.TextField(null=False)
    created_on = models.DateTimeField(null=False, auto_now_add=True)