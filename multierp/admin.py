from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Muser, Order

#----------------- Admin Site --------------
admin.site.site_header = "MultiAdmin"
admin.site.site_title = "MultiAdmin"
admin.site.index_title = "Welcome to MultiAdmin"


#---------------- To Display in Admin Panel -----------
class UserInline(admin.TabularInline):
    model = Muser
    can_delete = False
    verbose_name_plural = 'Muser'
    fk_name = 'user'



#------------------- Dispalying User in Admin -------------------
class MuserAdmin(UserAdmin):
    inlines = [UserInline, ]
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_user_type')
    list_select_related = ('profile', )

    def get_user_type(self, instance):
        return instance.profile.user_type
    get_user_type.short_description = 'Department'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(MuserAdmin, self).get_inline_instances(request, obj)

admin.site.unregister(User)
admin.site.register(User, MuserAdmin)