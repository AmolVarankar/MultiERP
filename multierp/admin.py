from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.fields import Field
from .models import *

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
    #inlines = [UserInline, ]
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_user_type')
    list_select_related = ('profile', )

    def get_user_type(self, instance):
        return instance.profile.user_type
    get_user_type.short_description = 'Department'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(MuserAdmin, self).get_inline_instances(request, obj)


class ItemResource(resources.ModelResource):
    import_id_fields = ('item_code')
    item_code= Field(attribute="item_code", column_name="Item Code")
    item_description= Field(attribute="item_description", column_name="Item Description")
    item_name= Field(attribute="item_name", column_name="Item Name")
    item_type= Field(attribute="item_type", column_name="Item Type")
    item_category= Field(attribute="item_category", column_name="Item Category")
    item_group= Field(attribute="item_group", column_name="Item Group")
    item_date= Field(attribute="item_date", column_name="Item Date")
    status= Field(attribute="status", column_name="Status")
    alternate_sw_code= Field(attribute="alternate_sw_code", column_name="Alternate S/W Code")
    site= Field(attribute="site", column_name="Site")
    HSN_code= Field(attribute="HSN_code", column_name="HSN Code")
    class Meta:
        model = Item


class ItemAdmin(ImportExportModelAdmin):
    resource_class = ItemResource

class ItemCategoryResource(resources.ModelResource):
    category_description = Field(attribute="item_category", column_name="Item Category")
    class Meta:
        model = ItemCategory


class ItemCategoryAdmin(ImportExportModelAdmin):
    resource_class = ItemCategoryResource



#--------------- USER -------------------
admin.site.unregister(User)
admin.site.register(User, MuserAdmin)

#--------------- ITEM -------------------
admin.site.register(Item, ItemAdmin)
admin.site.register(ItemCategory, ItemCategoryAdmin)
admin.site.register(ItemGroup)

#--------------- PARTY ------------------
admin.site.register(Party)

#--------------- ORDER ------------------
admin.site.register(SalesOrder)
admin.site.register(PurchaseOrder)
