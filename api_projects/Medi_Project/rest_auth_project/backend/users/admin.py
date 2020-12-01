from django.contrib import admin
from users.models import Paitent,Doctor,User
# Register your models here.

admin.site.register(User)
admin.site.register(Paitent)
admin.site.register(Doctor)