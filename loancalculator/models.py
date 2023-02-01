from django.db import models

class StateTax(models.Model):
    zipcode = models.CharField(("zipcode"), max_length=255)
    state = models.CharField(("state"), max_length=255)
    county = models.CharField(("county"), max_length=255)
    normalizedcounty = models.CharField(("normalizedcounty"), max_length=255)
    city = models.CharField(("city"), max_length=255)
    normalizedcity = models.CharField(("normalizedcity"), max_length=255)
    taxregionname = models.CharField(("taxregionname"), max_length=255)
    normalizedtaxregionname = models.CharField(("normalizedtaxregionname"), max_length=255)
    combinedrate = models.IntegerField(("combinedrate"))
    staterate = models.FloatField(("staterate"))
    countyrate = models.FloatField(("countyrate"))
    cityrate = models.IntegerField(("cityrate"))
    specialrate = models.FloatField(("specialrate"))
    estimatedpopulation = models.IntegerField(("estimatedpopulation"))
    year = models.IntegerField(("year"))
   # month = models.IntegerField(("month"))
 
class InvestmentForm(models.Model):
    starting_amount = models.FloatField()
    number_of_years = models.FloatField()
    return_rate = models.FloatField()
    annual_additional_contribution = models.FloatField()

# Create your models here.
