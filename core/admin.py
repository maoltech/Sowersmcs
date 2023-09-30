from django.contrib import admin
from .models import Loan, dand, Saving, Share, CustomUser
# Register your models here.

admin.site.register(dand)
admin.site.register(Loan)
admin.site.register(CustomUser)
admin.site.register(Saving)
admin.site.register(Share)