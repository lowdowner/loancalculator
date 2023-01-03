from django import forms

class InvestmentForm(forms.Form):
    starting_amount = forms.FloatField()
    deposit_amount = forms.FloatField()
    trade_in_value = forms.FloatField()
    number_of_years = forms.FloatField()
    return_rate = forms.FloatField()
    length_of_loan = forms.FloatField()
    annual_additional_contribution = forms.FloatField()

