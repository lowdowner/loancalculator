from django import forms
from .models import StateTax

STATES = (
    ('', 'Choose...'),
    ('AL','Alabama'),
('AK','Alaska'),
('AZ','Arizona'),
('AR','Arkansas'),
('AS','American Samoa'),
('CA','California'),
('CO','Colorado'),
('CT','Connecticut'),
('DE','Delaware'),
('DC','District of Columbia'),
('FL','Florida'),
('GA','Georgia'),
('GU','Guam'),
('HI','Hawaii'),
('ID','Idaho'),
('IL','Illinois'),
('IN','Indiana'),
('IA','Iowa'),
('KS','Kansas'),
('KY','Kentucky'),
('LA','Louisiana'),
('ME','Maine'),
('MD','Maryland'),
('MA','Massachusetts'),
('MI','Michigan'),
('MN','Minnesota'),
('MS','Mississippi'),
('MO','Missouri'),
('MT','Montana'),
('NE','Nebraska'),
('NV','Nevada'),
('NH','New Hampshire'),
('NJ','New Jersey'),
('NM','New Mexico'),
('NY','New York'),
('NC','North Carolina'),
('ND','North Dakota'),
('MP','Northern Mariana Islands'),
('OH','Ohio'),
('OK','Oklahoma'),
('OR','Oregon'),
('PA','Pennsylvania'),
('PR','Puerto Rico'),
('RI','Rhode Island'),
('SC','South Carolina'),
('SD','South Dakota'),
('TN','Tennessee'),
('TX','Texas'),
('TT','Trust Territories'),
('UT','Utah'),
('VT','Vermont'),
('VA','Virginia'),
('VI','Virgin Islands'),
('WA','Washington'),
('WV','West Virginia'),
('WI','Wisconsin'),
('WY','Wyoming')
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


CREDIT_SCORE = (
    ('', 'SELECT A VALUE'),
    (15000, 'Super Prime (781-850)'),
    (15000, 'Prime (661-780)'),
    (15000, 'Nonprime (601-660)'),
    (15000, 'Subprime (501-600)'),
    (15000, 'Deep Subprime (300-500)'),
   
)

class InvestmentForm(forms.Form):
    #starting_amount = forms.FloatField()
    starting_amount = forms.ChoiceField(choices=STARTING_AMOUNT)
    deposit_amount = forms.FloatField()
    trade_in_value = forms.FloatField()
    number_of_years = forms.FloatField()
    credit_score = forms.ChoiceField(choices=CREDIT_SCORE)
    #state = forms.ChoiceField(choices=STATES)
    #state = forms.ModelChoiceField(queryset=StateTax.zipcode(), empty_label=None)
    #state = forms.ChoiceField(queryset=StateTax.objects.values_list('zipcode', flat=True).distinct())
    state = forms.ChoiceField(
        label='State',
        choices=[(zipcode, zipcode) for zipcode in StateTax.objects.values_list('zipcode', flat=True).distinct()]
    )



    #return_rate = forms.FloatField()
    #length_of_loan = forms.FloatField()
    #annual_additional_contribution = forms.FloatField()

