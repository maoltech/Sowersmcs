from django.contrib import admin
from .models import User, Loan, dand, Saving, Share
# Register your models here.

admin.site.register(dand)
admin.site.register(Loan)
admin.site.register(User)
admin.site.register(Saving)
admin.site.register(Share)