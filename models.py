from django.db import models

class FCM(models.Model):
    fcm_file = models.FileField(upload_to='fcmfiles/%Y/%m/%d')