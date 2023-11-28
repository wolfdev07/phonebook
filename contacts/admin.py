from django.contrib import admin
from contacts.models import *

# Register your models here.
admin.site.register(States)
admin.site.register(ContactModel)
admin.site.register(AddressModel)
admin.site.register(PhoneModel)