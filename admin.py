from django.contrib import admin

# Register your models here.
from app.models import Pincode,Orphanage,Donator,Address,Thing

admin.site.register(Pincode)
admin.site.register(Donator)
admin.site.register(Orphanage)
admin.site.register(Address)
admin.site.register(Thing)

