from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Cash)
admin.site.register(Ishchilar)
admin.site.register(Items)
admin.site.register(Organizationsservice)

class AddClient(admin.ModelAdmin):
    list_display = ('client_name','client_phonenumber','ovner', 'client_reception_time')
admin.site.register(Clientadd,AddClient)

admin.site.register(Organizationscategory)
admin.site.register(AddOrganization)
admin.site.register(OrganizationPament)
admin.site.register(CerviseClient)
admin.site.register(Mahsulottopshirish)
