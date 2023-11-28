from django import forms
from django.forms import inlineformset_factory, DateInput
from contacts.models import ContactModel, AddressModel, PhoneModel

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ['name', 'last_name', 'photo', 'birthday']
        widgets = {
            'birthday': DateInput(attrs={'type': 'date'}),
        }

class AddressForm(forms.ModelForm):
    class Meta:
        model = AddressModel
        fields = ['street', 'exterior_number', 'internal_number', 'neighborhood', 'city', 'state', 'references']

class PhoneForm(forms.ModelForm):
    class Meta:
        model = PhoneModel
        fields = ['phone_type_options', 'alias', 'code_country', 'number']


PhoneFormSet = inlineformset_factory(ContactModel, PhoneModel, form=PhoneForm, extra=1, can_delete=True)