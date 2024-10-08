from django.shortcuts import render
from django.views import View
from .forms import InvestmentForm
from .models import StateTax


class Index(View):
    def get(self, request):

        '''
        form = InvestmentForm()
        return render(request, 'loancalculator/index.html', {'form': form})
        '''
        # Fill in the initial values on the unbound form:
        initial = {
            'starting_amount': request.session.get('starting_amount'),
            'number_of_years': request.session.get('number_of_years'),
            'return_rate': request.session.get('return_rate'),
            'annual_additional_contribution': request.session.get('annual_additional_contribution'),
        }

        form = InvestmentForm(initial=initial)
        return render(request, 'loancalculator/index.html', {'form': form})

    def post(self, request):
        form = InvestmentForm(request.POST)

        if form.is_valid():
                
                # After getting the cleaned_data, set a session variable to hold it
                total_result = form.cleaned_data['starting_amount']
                request.session['starting_amount'] = total_result

                number_of_years = int(form.cleaned_data['number_of_years'])
                request.session['number_of_years'] = number_of_years

                #return_rate = form.cleaned_data['return_rate']
                #request.session['return_rate'] = return_rate

                #annual_additional_contribution = form.cleaned_data['annual_additional_contribution']
                #request.session['annual_additional_contribution'] = annual_additional_contribution
                total_interest = 0
                yearly_results = {}

                state = form.cleaned_data['state']

                #sales_tax = StateTax.objects.filter(zipcode=state).values_list('combinedrate', flat=True).distinct().first()

                ### WORKING ###
                #sales_tax = StateTax.objects.filter(zipcode=state).values('combinedrate').distinct()

                sales_tax = StateTax.objects.filter(zipcode=state).values('combinedrate')[0]
                tax_rate = float(sales_tax['combinedrate'])
                tax_amount = int(int(total_result) * (tax_rate/100))
                
                credit_score_apr = float(form.cleaned_data['credit_score'])

                credit_score_apr_perc = credit_score_apr*100

                #sales_tax_amount = [int(form.cleaned_data['starting_amount']) * sales_tax for sales_tax in sales_tax] 

                #state_tax = StateTax.objects.filter(zipcode=state).values('combinedrate').distinct().first()
                #sales_tax = float(state_tax['combinedrate'])

                #sales_tax_perc = float(sales_tax)

                #sales_tax_amount =  (sales_tax_perc/100) * int(form.cleaned_data['starting_amount'])

                #monthly_repay = int((form.cleaned_data['starting_amount'] / (int(form.cleaned_data['number_of_years'])*12)) + (form.cleaned_data['starting_amount'] / (int(form.cleaned_data['number_of_years'])*12) * 0.07))

                monthly_repay = int((((int(form.cleaned_data['starting_amount']) - form.cleaned_data['deposit_amount'] - form.cleaned_data['trade_in_value'] +tax_amount) * credit_score_apr) / 12) / (1 - (1 + (credit_score_apr / 12))**(- int(form.cleaned_data['number_of_years']*12))))

                total_loan = int(int(form.cleaned_data['starting_amount']) - form.cleaned_data['deposit_amount'] - form.cleaned_data['trade_in_value'] + tax_amount)

                #total_loan_plus_interest = int((((form.cleaned_data['starting_amount'] - form.cleaned_data['deposit_amount'] - form.cleaned_data['trade_in_value']) * 0.07) / 12) / (1 - (1 + (0.07 / 12))**(- int(form.cleaned_data['number_of_years']))))

                total_interest_and_loan = monthly_repay * int(form.cleaned_data['number_of_years']*12)

                total_interest = total_interest_and_loan - total_loan

                number_of_payments = int(form.cleaned_data['number_of_years'])*12

                #sales_tax = StateTax.objects.filter(id=90001, specialrate=36200.0).values('combinedrate')  
 
                

                #sales_tax = StateTax.objects.filter(zipcode=state).distinct().get()

                #sales_tax = StateTax.objects.filter(zipcode=state)
                #if sales_tax:
                #    state_tax = StateTax.combinedrate
                #else:
                #    'no_rate'

                

                context2 = {
                        'form':form,
                        'number_of_payments': number_of_payments,
                        'monthly_repay': monthly_repay,
                        'starting_amount': int(form.cleaned_data['starting_amount']),
                        'deposit_amount': int(form.cleaned_data['deposit_amount']),
                        'trade_in_value': int(form.cleaned_data['trade_in_value']),
                        'total_loan': total_loan,
                        #'total_loan_plus_interest': total_loan_plus_interest,
                        'total_interest_and_loan': total_interest_and_loan,
                        'total_interest': total_interest,
                        'state': state,
                        'sales_tax': sales_tax,
                        #'sales_tax_perc' : sales_tax_perc,
                        #'sales_tax_amount' :sales_tax_amount
                        'tax_amount': tax_amount,
                        'credit_score': credit_score_apr,
                        'credit_score_perc': credit_score_apr_perc,

                        
                    }
                return render(request, 'loancalculator/index.html', context2)
        else:
            form = InvestmentForm()
            return render(request, 'loancalculator/index.html', {'form':form})  
'''             
                for i in range(1, int(form.cleaned_data['number_of_years'] +1)):
                    yearly_results[i] = {}

                    # CALCULATE THE INTEREST 
                    interest = total_result * (form.cleaned_data['return_rate'] / 100)
                    total_result += interest 
                    total_interest += interest

                    # ADDITIONAL CONTRIBUTION 
                    total_result += form.cleaned_data['annual_additional_contribution']

                    # SET YEARLY RESULTS 
                    yearly_results[i]['interest']  = round(total_interest, 2)
                    yearly_results[i]['total'] = round(total_result,2)

                    # MONTHLY COST
                    monthly_repay = (form.cleaned_data['starting_amount'] / int(form.cleaned_data['number_of_years'])) + (form.cleaned_data['starting_amount'] * 0.07)

                    # CREATE CONTEXT 
                    context = {
                        'form':form,
                        'total_result': round(total_result,2),
                        'yearly_results': yearly_results,
                        'number_of_years': int(form.cleaned_data['number_of_years'])
                    }

                 
            
                # RENDER THE TEMPLATE

                return render(request, 'loancalculator/index.html', context)

        # MONTHLY COST
                

        
        else:
            form = InvestmentForm()
            return render(request, 'loancalculator/index.html', {'form':form})

'''
         
        
