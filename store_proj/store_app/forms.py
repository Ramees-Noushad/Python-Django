from django import forms
from .models import Department, Course

class StoreForm(forms.Form):
    name = forms.CharField(max_length=100)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    phone_number = forms.CharField(max_length=15)
    mail_id = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea)
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    course = forms.ModelChoiceField(queryset=Course.objects.none())
    purpose = forms.ChoiceField(choices=[('Enquiry', 'Enquiry'), ('Place Order', 'Place Order'), ('Return', 'Return')])
    materials_provide = forms.MultipleChoiceField(
        choices=[('Notebook', 'Notebook'), ('Pen', 'Pen'), ('Exam Papers', 'Exam Papers')],
        widget=forms.CheckboxSelectMultiple()
    )

