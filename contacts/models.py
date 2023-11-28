from django.db import models

# Create your models here.

#STATE MODEL
class States(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


#CONTACT MODEL
class ContactModel(models.Model):
    name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=120)
    photo = photo = models.ImageField(upload_to='contact_photos/', blank=True, null=True)
    birthday = models.DateField()
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.last_name}'


#ADDRESS MODEL
class AddressModel(models.Model):
    contact = models.ForeignKey(ContactModel, null=False, on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    exterior_number = models.CharField(max_length=10)
    internal_number = models.CharField(max_length=10)
    neighborhood = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.OneToOneField(States, on_delete=models.CASCADE)
    references = models.TextField()

    def __str__(self):
        return f'{self.contact.name} - {self.neighborhood} | {self.city} | {self.state.name}'


#PHONE MODEL
class PhoneModel(models.Model):
    contact = models.ForeignKey(ContactModel, null=False, on_delete=models.CASCADE)
    phone_type_options = models.CharField(max_length=60)
    alias = models.CharField(max_length=255)
    code_country = models.CharField(max_length=10)
    number = models.CharField(max_length=60)

    def __str__(self):
        return f'{self.code_country} - {self.number}'