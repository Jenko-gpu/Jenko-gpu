from django.db import models

class Note(models.Model):
    input_text = models.CharField(max_length=250)
    extracted_time = models.CharField(max_length=250)
    extracted_date = models.CharField(max_length=250)
