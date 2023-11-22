from django.contrib import admin
from .models import User, CustomUser, Client

#tables
admin.site.register(User)
admin.site.register(CustomUser)
admin.site.register(Client)
