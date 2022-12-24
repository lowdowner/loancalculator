from django.db import models
 
class InvestmentForm(models.Model):
    starting_amount = models.FloatField()
    number_of_years = models.FloatField()
    return_rate = models.FloatField()
    annual_additional_contribution = models.FloatField()

# Create your models here.
