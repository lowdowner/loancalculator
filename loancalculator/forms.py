from django import forms

STATES = (
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
)

STARTING_AMOUNT = (
    ('', 'SELECT A VALUE'),
    (15000, '$15,000'),
    (20000, '$20,000'),
    (25000, '$25,000'),
    (30000, '$30,000'),
    (35000, '$35,000'),
    (40000, '$40,000'),
    (45000, '$45,000'),
    (50000, '$50,000'),
    (55000, '$55,000'),
    (60000, '$60,000'),
    (65000, '$65,000'),
    (70000, '$70,000'),
    (70000, '$70,000'),
    (80000, '$80,000'),
    (90000, '$90,000'),
    (95000, '$95,000'),
    (100000, '$100,000'),
    (105000, '$105,000'),
    (110000, '$110,000'),
    (115000, '$115,000'),
    (120000, '$120,000'),
    (125000, '$125,000'),
    (130000, '$130,000'),
    (135000, '$135,000'),
    (140000, '$140,000'),
    (145000, '$145,000'),
    (150000, '$150,000'),

)

class InvestmentForm(forms.Form):
    #starting_amount = forms.FloatField()
    starting_amount = forms.ChoiceField(choices=STARTING_AMOUNT)
    deposit_amount = forms.FloatField()
    trade_in_value = forms.FloatField()
    number_of_years = forms.FloatField()
    state = forms.ChoiceField(choices=STATES)
    #return_rate = forms.FloatField()
    #length_of_loan = forms.FloatField()
    #annual_additional_contribution = forms.FloatField()

