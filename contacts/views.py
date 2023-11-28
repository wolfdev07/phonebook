from typing import Any
from django.http import HttpRequest, HttpResponse
from contacts.models import ContactModel, AddressModel
from contacts.forms import ContactForm, AddressForm, PhoneFormSet
#CREATE
from django.views.generic.edit import CreateView, DeleteView
#READ
from django.utils import timezone
from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy

# Create your views here.
class IndexView(ListView):
    model = ContactModel
    paginate_by = 10
    template_name = "list_contacts.html"

    def get_queryset(self):
        return ContactModel.objects.all().order_by("name")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        context["view_name"]="Inicio"
        return context


class CreateContact(CreateView):
    model = ContactModel
    form_class = ContactForm
    template_name = "create_contact.html"

    def get_success_url(self):
        return reverse_lazy('edit', kwargs={'contact_id': self.object.pk})


class ContactDetailView(View):
    template_name = "detail_contact.html"

    def get(self, request, contact_id):
        contact = ContactModel.objects.get(pk=contact_id)
        contact_form = ContactForm(instance=contact)
        
        # Obtiene todas las direcciones asociadas al contacto
        addresses = AddressModel.objects.filter(contact=contact)
        # Si hay alguna dirección asociada, utiliza la primera
        address_form = AddressForm(instance=addresses.first()) if addresses.exists() else AddressForm()
        
        phone_formset = PhoneFormSet(instance=contact)

        context =  {
            'contact_form': contact_form,
            'address_form': address_form,
            'phone_formset': phone_formset,
            'view_name':'Editar',
        }

        return render(request, self.template_name, context)

    def post(self, request, contact_id):

        contact = ContactModel.objects.get(pk=contact_id)
        
        form_type = request.POST.get('form_type')

        if form_type == 'contact':
            contact_form = ContactForm(request.POST, instance=contact)
            if contact_form.is_valid():
                contact_form.save()
                return redirect('edit', contact_id=contact_id)
        
        elif form_type == 'address':
            address_form = AddressForm(request.POST, instance=contact) if address_form.exist() else AddressForm()
            
            if address_form.is_valid():
                address_instance = address_form.save(commit=False)
                address_instance.contact = contact
                address_instance.save()
                return redirect('edit', contact_id=contact_id)
        
        elif form_type == 'phone':
            phone_formset = PhoneFormSet(request.POST, instance=contact)
            if phone_formset.is_valid():
                phone_formset.save()
                return redirect('edit', contact_id=contact_id)


        return redirect('edit', contact_id=contact.pk)


class DeleteContact(DeleteView):
    model = ContactModel
    success_url = reverse_lazy('index')
    template_name = "list_contacts.html"