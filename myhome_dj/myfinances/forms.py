from myfinances.models import Expenses, Files
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class ExpenseForm(forms.ModelForm):

    bill = forms.FileField()

    class Meta:
        model = Expenses
        widgets = {
            'date_of_expense': DateInput,
            'details': forms.Textarea(attrs={'rows':3})
        }
        fields = ['name', 'type', 'amount', 'details', 'date_of_expense']