import django_filters
from .models import *



class SalesOrderFilter(django_filters.FilterSet):
	class Meta:
		model = SalesOrder
		fields = ["SO_no","SQ_SSO_DGRN_No","Status","SO_Date","SO_type","Vendor_Code","Vendor_Name"]

class PurchaseOrderFilter(django_filters.FilterSet):
	class Meta:
		model = PurchaseOrder
		fields = ["PO_no","SQ_SPO_DGRN_No","Status","PO_Date","PO_type","Customer_Code","Customer_Name"]

class ItemFilter(django_filters.FilterSet):
	class Meta:
		model = Item
		fields = ["item_code","item_description","item_name","item_type","item_group","item_date","status","alternate_sw_code","site","HSN_code"]

class PartyFilter(django_filters.FilterSet):
	class Meta:
		model = Party
		fields = ["Party_Date","Party_Code","Party_Details_Description","Status","Category"]