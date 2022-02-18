from django.db import models

# Create your models here.
class Address(models.Model):
    address = models.CharField(max_length=100)
    balance = models.IntegerField()
    final_balance = models.IntegerField()
    final_n_tx = models.IntegerField()
    n_tx = models.IntegerField()
    total_received = models.IntegerField()
    total_sent = models.IntegerField()
    unconfirmed_balance = models.IntegerField()
    unconfirmed_n_tx = models.IntegerField()
    last_updated = models.DateTimeField()
