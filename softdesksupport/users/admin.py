from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import Contributor, User


admin.site.register(User, UserAdmin)
admin.site.register(Contributor)

