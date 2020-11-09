from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



#------------------(User Model)-----------------

inco_terms_choices = [
		("FOB","FOB"),
		("CIF","CIF"),
		("CFR","CFR"),
		("EX WORK","EX WORK"),
		("DAT","DAT"),
		("DAP","DAP"),
		("DDP","DDP"),
		("CPT","CPT"),
		("CIP","CIP"),
		("DAT_F","DAT_F"),
		("EX-MIL","EX-MIL"),
		("CNF","CNF"),
		("DDU","DDU"),
		("FCA" ,"FCA "),
		("FAS" ,"FAS "),
		("DES","DES"),
		("DEQ","DEQ"),
		("FOR","FOR"),
	]

currency_choices = [

		("TWD","TWD"),
		("MDL","MDL"),
		("NPR","NPR"),
		("PGK","PGK"),
		("NOK","NOK"),
		("PEN","PEN"),
		("PHP","PHP"),
		("BRL","BRL"),
		("ZAR","ZAR"),
		("MWK","MWK"),
		("ERN","ERN"),
		("PLN","PLN"),
		("ETB","ETB"),
		("DJF","DJF"),
		("ISK","ISK"),
		("TZS","TZS"),
		("CAD","CAD"),
		("CDF","CDF"),
		("IQD","IQD"),
		("KYD","KYD"),
		("BZD","BZD"),
		("BWP","BWP"),
		("IRR","IRR"),
		("EGP","EGP"),
		("MUR","MUR"),
		("SBD","SBD"),
		("BTN","BTN"),
		("INR","INR"),
		("IDR","IDR"),
		("KHR","KHR"),
		("MNT","MNT"),
		("BAM","BAM"),
		("HNL","HNL"),
		("HTG","HTG"),
		("GYD","GYD"),
		("HKD","HKD"),
		("TOP","TOP"),
		("SGD","SGD"),
		("NZD","NZD"),
		("RON","RON"),
		("QAR","QAR"),
		("DOP","DOP"),
		("CZK","CZK"),
		("LKR","LKR"),
		("SHP","SHP"),
		("HRK","HRK"),
		("LSL","LSL"),
		("TRY","TRY"),
		("AMD","AMD"),
		("MVR","MVR"),
		("CHF","CHF"),
		("MMK","MMK"),
		("AED","AED"),
		("LYD","LYD"),
		("LRD","LRD"),
		("TND","TND"),
		("MKD","MKD"),
		("RWF","RWF"),
		("MAD","MAD"),
		("UGX","UGX"),
		("UAH","UAH"),
		("TMT","TMT"),
		("WST","WST"),
		("MGA","MGA"),
		("HUF","HUF"),
		("SRD","SRD"),
		("RUB","RUB"),
		("SOS","SOS"),
		("UYU","UYU"),
		("GNF","GNF"),
		("FKP","FKP"),
		("AZN","AZN"),
		("KRW","KRW"),
		("OMR","OMR"),
		("FJD","FJD"),
		("KPW","KPW"),
		("AUD","AUD"),
		("SAR","SAR"),
		("LBP","LBP"),
		("AWG","AWG"),
		("MYR","MYR"),
		("PKR","PKR"),
		("RSD","RSD"),
		("ARS","ARS"),
		("SLL","SLL"),
		("GEL","GEL"),
		("TJS","TJS"),
		("KMF","KMF"),
		("XAF","XAF"),
		("KGS","KGS"),
		("CVE","CVE"),
		("BSD","BSD"),
		("GTQ","GTQ"),
		("GBP","GBP"),
		("COP","COP"),
		("BHD","BHD"),
		("KWD","KWD"),
		("SEK","SEK"),
		("NGN","NGN"),
		("SCR","SCR"),
		("SYP","SYP"),
		("CLP","CLP"),
		("BBD","BBD"),
		("UZS","UZS"),
		("DKK","DKK"),
		("JMD","JMD"),
		("XPF","XPF"),
		("LAK","LAK"),
		("VUV","VUV"),
		("THB","THB"),
		("CNY","CNY"),
		("MXN","MXN"),
		("BDT","BDT"),
		("DZD","DZD"),
		("GHS","GHS"),
		("SZL","SZL"),
		("VEF","VEF"),
		("BMD","BMD"),
		("EUR","EUR"),
		("BIF","BIF"),
		("USD","USD"),
		("NIO","NIO"),
		("VND","VND"),
		("XOF","XOF"),
		("GIP","GIP"),
		("TTD","TTD"),
		("JPY","JPY"),
		("ILS","ILS"),
		("GMD","GMD"),
		("YER","YER"),
		("CRC","CRC"),
		("KES","KES"),
		("JOD","JOD"),
		("NAD","NAD"),
		("CUP","CUP"),
		("AOA","AOA"),
		("KZT","KZT"),
		("MZN","MZN"),
		("BND","BND"),
		("BGN","BGN"),
		("SDG","SDG"),
		("PYG","PYG"),
		("XCD","XCD"),
	]

class Muser(models.Model):

	USER_TYPE_CHOICES = ( 
		('Sal', 'Sales'),
		('Opn', 'Operations'),
		('Fin', 'Finance'),
		('Adm', 'Admin'),)

	user_type = models.CharField(max_length=3, choices=USER_TYPE_CHOICES, default='Sal')
	user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
	
	def __str__(self):
		return self.user.username

#----------------- Signal to create or update profile ---------

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
		if created:
			Muser.objects.create(user=instance)
		instance.profile.save()


class Party(models.Model):
	status_choices = [
		("Open","Open"),
		("Closed","Closed"),
		("Approved","Approved"),
		("Rejected","Rejected"),
		("Released","Released"),
		("Cancelled","Cancelled"),
	]

	category_choices = [
		("Assoc. Memb fees-Association Membership fees","Assoc. Memb fees-Association Membership fees"),
		("Pump-Pump","Pump-Pump"),
		("Trader-Trader","Trader-Trader"),
		("Power Trans-Power Transmission","Power Trans-Power Transmission"),
		("SP- Training-SP- Training","SP- Training-SP- Training"),
		("SP- HR-SP- HR","SP- HR-SP- HR"),
		("SP- Sales-SP- Sales","SP- Sales-SP- Sales"),
		("Capex-Capex","Capex-Capex"),
		("Exhibition-Exhibition","Exhibition-Exhibition"),
		("Transporter-Transporter","Transporter-Transporter"),
		("Importer- Trader-Importer- Trader","Importer- Trader-Importer- Trader"),
		("Courier-Courier","Courier-Courier"),
		("Forwarder-Forwarder","Forwarder-Forwarder"),
		("SP- Printing-SP- Printing","SP- Printing-SP- Printing"),
		("Freight-Freight","Freight-Freight"),
		("SP- Air Ticket-SP- Air Ticket","SP- Air Ticket-SP- Air Ticket"),
		("Paper-Paper","Paper-Paper"),
		("Traders-Traders","Traders-Traders"),
		("Automobile-Automobile","Automobile-Automobile"),
		("Miscellaneous-Miscellaneous","Miscellaneous-Miscellaneous"),
		("SP- Interpretor-SP- Interpretor","SP- Interpretor-SP- Interpretor"),
		("SP- Commun.-SP- Communication","SP- Commun.-SP- Communication"),
		("Material Handl.-Material Handling","Material Handl.-Material Handling"),
		("Job Worker-Job Worker","Job Worker-Job Worker"),
		("SP- 3D Printing-SP- 3D Printing","SP- 3D Printing-SP- 3D Printing"),
		("Clearing Agent-Clearing Agent","Clearing Agent-Clearing Agent"),
		("Back Office-Back Office","Back Office-Back Office"),
		("Oil And Gas-Oil Gas","Oil And Gas-Oil Gas"),
		("Cement-Cement","Cement-Cement"),
		("Irrigation-Irrigation","Irrigation-Irrigation"),
		("Textile-Textile","Textile-Textile"),
		("Machine tools-Machine tools","Machine tools-Machine tools"),
		("Principal Supp.-Principal Supplier","Principal Supp.-Principal Supplier"),
		("Trader- Cons.-Trader- Consumables","Trader- Cons.-Trader- Consumables"),
		("Automation-Automation","Automation-Automation"),
		("Aluminum-Aluminum","Aluminum-Aluminum"),
		("Semi- Conductor-Semi- Conductor","Semi- Conductor-Semi- Conductor"),
		("SP- Fire service-SP- Fire service","SP- Fire service-SP- Fire service"),
		("SP- Electricity-SP- Electricity","SP- Electricity-SP- Electricity"),
		("Packaging Mach.-Packaging Machine","Packaging Mach.-Packaging Machine"),
		("SP- Offc Maint-SP- Offc Maintainance","SP- Offc Maint-SP- Offc Maintainance"),
		("Trader- 3D-Trader- 3D","Trader- 3D-Trader- 3D"),
		("Advertisment- HR-Advertisment- HR","Advertisment- HR-Advertisment- HR"),
		("SP- Hotel-SP- Hotel","SP- Hotel-SP- Hotel"),
		("SP- Telephone-SP- Telephone","SP- Telephone-SP- Telephone"),
		("SP- Insurance-SP- Insurance","SP- Insurance-SP- Insurance"),
		("SP- Mahape-SP- Mahape","SP- Mahape-SP- Mahape"),
		("Consumbales-Consumbales","Consumbales-Consumbales"),
		("Steel-Steel","Steel-Steel"),
		("Import- Supplier-Import- Supplier","Import- Supplier-Import- Supplier"),
		("Sales Team-Sales Team","Sales Team-Sales Team"),
		("SP- Advertising-SP- Advertising","SP- Advertising-SP- Advertising"),
		("Power Plant-Power Plant","Power Plant-Power Plant"),
		("tyre-tyre","tyre-tyre"),
		("HR Training- SP-HR Training- SP","HR Training- SP-HR Training- SP"),
		("SP- Computer-SP- Computer","SP- Computer-SP- Computer"),
		("Pharmacutical-Pharmacutical","Pharmacutical-Pharmacutical"),
		("SP- Advertisment-SP- Advertisment","SP- Advertisment-SP- Advertisment"),
		("Polyfilm-Polyfilm","Polyfilm-Polyfilm"),
		("SP- Consultant-SP- Consultant","SP- Consultant-SP- Consultant"),
	]

	party_type_choices = [
		("Supplier/Creditors","Supplier/Creditors"),
		("Customer/Debtors","Customer/Debtors"),
		("Subcontractor","Subcontractor"),
		("Dealer/Distributor","Dealer/Distributor"),
		("Supplier/Customer","Supplier/Customer"),
		("Transporter","Transporter"),
		("Manufacturer","Manufacturer"),
		("Consignee","Consignee"),
		("Dealer","Dealer"),
		("Distributor","Distributor"),
		("Employee","Employee"),
		("First Stage Dealer","First Stage Dealer"),
		("Second Stage Dealer","Second Stage Dealer"),
	]
	
	GST_party_type_choices = [

		("Registered","Registered"),
		("Unregistered","Unregistered"),
		("Compounding","Compounding"),
		("Consumer","Consumer"),
		("Import","Import"),
		("Export","Export"),
		("Farmer","Farmer"),
	]

	form_name_choices = [

		("C Form","C Form"),
		("F Form","F Form"),
		("H Form","H Form"),
		("I Form","I Form"),
		("E1 Form","E1 Form"),
		("E2 Form","E2 Form"),
		("W","W"),
		("N/A","N/A"),
		("Sale with C form, against receipt of E1","Sale with C form, against receipt of E1"),
		("Sale with C form, against receipt of E2","Sale with C form, against receipt of E2"),
		("CT 1 Form","CT 1 Form"),
		("VAT Form D1","VAT Form D1"),
		("J-VAT","J-VAT"),
		("E1 Form - Purchase ","E1 Form - Purchase "),
		("E2 Form - Purchase ","E2 Form - Purchase "),
		("E1 Form - Sales ","E1 Form - Sales "),
		("E2 Form - Sales ","E2 Form - Sales "),
		("Form 11","Form 11"),
		("CT 3 Form","CT 3 Form"),
		("C4 Form","C4 Form"),
		("D2 Form","D2 Form"),
		("Vat C-4","Vat C-4"),

	]

	shelf_type_choices =[
		("Based on Value","Based on Value"),
		("Based on Value","Based on Value"),
	]
	dealer_site_choices = [
		("1","Multidimensions"),
		("2","TechPioneer"),
	]

	party_group_choices =[
		("North","North"),
		("South","South"),
		("East","East"),
		("West","West"),
	]

	Party_Date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	Party_Code = models.CharField(max_length=200,blank=True)
	Party_Details_Description = models.CharField(max_length=200,blank=True)
	Status = models.CharField(max_length=100,choices=status_choices,default='OPEN')
	Currency = models.CharField(max_length=3,choices=currency_choices,default='INR')
	Category = models.CharField(max_length=100,choices=category_choices, default="Assoc. Memb fees-Association Membership fees") 
	Beneficiary_Details = models.CharField(max_length=200, blank=True)
	Party_Type = models.CharField(max_length=100,choices=party_type_choices,default='Supplier/Creditors') 
	Remarks = models.TextField(max_length=500, blank=True)
	Comments = models.TextField(max_length=500,blank=True)
	Narration = models.TextField(max_length=500,blank=True)

	GST_Party_Type= models.CharField(max_length=100, choices=GST_party_type_choices, default="Unregistered")
	GTA_Applicable = models.BooleanField(default=False)

	#TDS/TCS_Applicable_Flag (cbox_conditional)
	#eductee_type
	#company
	#non_company (radio)
	#resident
	#non_Resident (radio)
	#Pan Number

	Party_Group = models.CharField(max_length=200, choices=party_group_choices, default="North" )
	Credit_Limit = models.CharField(max_length=200,blank=True) 
	Credit_Days = models.CharField(max_length=200,blank=True)
	Inco_Terms = models.CharField(max_length=200, choices=inco_terms_choices, default="FOB")
	Form_Name = models.CharField(max_length=200, choices=form_name_choices, default="C Form") 
	Contact_Name=models.CharField(max_length=200,blank=True)
	Cheque_Clearing_days=models.CharField(max_length=200, blank=True)
	Shelf_Type= models.CharField(max_length=200, choices=shelf_type_choices,default="Based on Value")
	Shelf_Value = models.CharField(max_length=200,blank=True)
	Price_Value_Flag = models.CharField(max_length=200, choices=shelf_type_choices,default="Based on Value")
	Price_Value = models.CharField(max_length=200,blank=True)
	Rating = models.CharField(max_length=200,blank=True)
	Party_Tax_Class_Code = models.CharField(max_length=200,blank=True)
	Party_Tax_Class_Desc = models.CharField(max_length=200,blank=True)
	Email_Id = models.CharField(max_length=100, blank=True)
	Transporter_Id = models.CharField(max_length=200,choices=dealer_site_choices, default="1")

	AutoDx_XML_Format= models.BooleanField(default=False)
	AutoDx_CSV_Format  = models.BooleanField(default=False)

	Sender_ID = models.CharField(max_length=200,blank=True)
	Receiver_ID = models.CharField(max_length=200,blank=True)

	Dealer_Site_Code = models.CharField(max_length=200, choices=dealer_site_choices, default="1")
	Dealer_Parent_Site_Code = models.CharField(max_length=200,blank=True)

	Supplier_Login_Id = models.CharField(max_length=200,blank=True)
	Customer_Login_Id = models.CharField(max_length=200,blank=True)

	class Meta:
		verbose_name= "Item	Parties"

	def __str__(self):
		return self.Party_Code


#---------------Sales Order Model -----------------------

class SalesOrder(models.Model):
	so_type_choices = [
		("Domestic","Domestic"),
		("Export","Export"),
		("Tender","Tender"),
		("Scrap","Scrap"),
		("Service","Service"),
		("Schedule","Schedule"),
		("Stockist","Stockist"),
		("Free Sales" ,"Free Sales "),
		("Demo Sales","Demo Sales"),
		("Captive Consumption" ,"Captive Consumption "),
		("Job Work","Job Work"),
		("Trading","Trading"),
		("Deemed Export","Deemed Export"),
		("Export Warehousing","Export Warehousing"),
		("Contract","Contract"),
		("Sales In Transit","Sales In Transit"),
	]

	so_site_choices = [
		('1', 'Multidimensions'),
		('2', 'Tech-Pioneer'),
	]

	so_site_address_choices = [
		('Bill to Address', 'Multi (B)-Multidimensions-Bill To Address'),
		('Ship to Address', 'Multi (S)-Multidimensions-Ship To Address'),
	]

	accounting_site_choices = [
		('1', 'Multidimensions'),
		('2', 'Tech-Pioneer'),
	]

	delivery_mode_choices = [
		("DM0001-Air","DM0001-Air"),
		("DM0002-Road","DM0002-Road"),
		("DM0003-Rail","DM0003-Rail"),
		("DM0004-Ship","DM0004-Ship"),
	]

	delivery_term_choices = [
		("CFR","CFR-Cost and Freight"),
		("CIF","CIF-Cost Insurance Freight"),
		("CIP","CIP-Carriage and Insurance"),
		("CPT","CPT-Carriage Paid To"),
		("DAP","DAP-Delivered At Place"),
		("DAT","DAT-Delivered At Terminal"),
		("DDP","DDP-Delivered Duty Paid"),
		("EXW","EXW-Ex Works"),
		("FAS","FAS-Free Alongside Ship"),
		("FCA","FCA-Free Carrier"),
		("FOB","FOB-Free On Board"),
	]
	
	status_choices = [
		("Open","Open"),
		("Closed","Closed"),
		("Approved","Approved"),
		("Rejected","Rejected"),
		("Amended","Amended"),
		("Released","Released"),
		("Cancelled","Cancelled"),
		("ApproveAmended","ApproveAmended"),
		("ApproveConverted","ApproveConverted"),
	]

	SO_no = models.CharField(max_length=200)
	SQ_SSO_DGRN_No = models.CharField(max_length=200)
	Status = models.CharField(max_length=100,choices=status_choices,default='OPEN')
	SO_Date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	SO_Description = models.CharField(max_length=500)
	SO_type = models.CharField(max_length=100,choices=so_type_choices)
	Transaction_category = models.CharField(max_length=200)
	Site = models.CharField(max_length=100,choices=so_site_choices)
	Vendor_Code = models.ForeignKey(Party, related_name = "Vendor_Code", on_delete=models.PROTECT)
	Vendor_Name = models.ForeignKey(Party, related_name = "Vendor_Name", on_delete=models.PROTECT)
	Vendor_Address = models.ForeignKey(Party, related_name = "Vendor_Add", on_delete=models.PROTECT)
	Site_address = models.CharField(max_length=100,choices=so_site_address_choices)
	Accounting_Site = models.CharField(max_length=100,choices=accounting_site_choices)
	Ac_code = models.CharField(max_length=200)
	Currency = models.CharField(max_length=3,choices=currency_choices,default='INR')
	Exchange_Rates = models.CharField(max_length=200)
	Credit_Terms = models.CharField(max_length=100)
	Delivery_Terms = models.CharField(max_length=100,choices=delivery_term_choices)
	Delivery_Mode = models.CharField(max_length=100,choices=delivery_mode_choices)
	Reference = models.CharField(max_length=200)
	Inco_Terms = models.CharField(max_length=100,choices=inco_terms_choices, default="FOB")
	Remarks = models.TextField(max_length=500,blank=True)
	Comments = models.TextField(max_length=500,blank=True)

	def __str__(self):
		return self.SO_Description

#---------------------------- Purchase Order ---------------------

class PurchaseOrder(models.Model):

	po_type_choices = [
		("Domestic","Domestic"),
		("Import","Import"),
		("Sub_Contract","Sub Contract"),
		("Job","Job"),
		("Service","Service"),
		("Schedule","Schedule"),
		("Planned","Planned"),
		("SubContract_MT","SubContract MT"),
		("Trading","Trading"),
		("Plant_Maintenance_Consumption" ,"Plant Maintenance"),
		("Non_Inventory","Non Inventory"),
		("Sales_In_Transit","Sales In Transit"),
	]

	po_site_choices = [
		('1', 'Multidimensions'),
		('2', 'Tech-Pioneer'),
	]

	po_site_address_choices = [
		('Bill to Address', 'Multi (B)-Multidimensions-Bill To Address'),
		('Ship to Address', 'Multi (S)-Multidimensions-Ship To Address'),
	]

	status_choices = [
		("Open","Open"),
		("Closed","Closed"),
		("Approved","Approved"),
		("Rejected","Rejected"),
		("Amended","Amended"),
		("Released","Released"),
		("Cancelled","Cancelled"),
		("ApproveAmended","ApproveAmended"),
		("ApproveConverted","ApproveConverted"),
	]
		
	accounting_site_choices = [
		('1', 'Multidimensions'),
		('2', 'Tech-Pioneer'),
	]

	delivery_mode_choices = [
		("DM0001-Air","DM0001-Air"),
		("DM0002-Road","DM0002-Road"),
		("DM0003-Rail","DM0003-Rail"),
		("DM0004-Ship","DM0004-Ship"),
	]

	delivery_term_choices = [
		("CFR","CFR-Cost and Freight"),
		("CIF","CIF-Cost Insurance Freight"),
		("CIP","CIP-Carriage and Insurance"),
		("CPT","CPT-Carriage Paid To"),
		("DAP","DAP-Delivered At Place"),
		("DAT","DAT-Delivered At Terminal"),
		("DDP","DDP-Delivered Duty Paid"),
		("EXW","EXW-Ex Works"),
		("FAS","FAS-Free Alongside Ship"),
		("FCA","FCA-Free Carrier"),
		("FOB","FOB-Free On Board"),
	]
	inco_terms_choices = [
		("FOB","FOB"),
		("CIF","CIF"),
		("CFR","CFR"),
		("EX_WORK","EX WORK"),
		("DAT","DAT"),
		("DAP","DAP"),
		("DDP","DDP"),
		("CPT","CPT"),
		("CIP","CIP"),
		("DAT_F","DAT_F"),
		("EX-MIL","EX-MIL"),
		("CNF","CNF"),
		("DDU","DDU"),
		("FCA" ,"FCA "),
		("FAS" ,"FAS "),
		("DES","DES"),
		("DEQ","DEQ"),
		("FOR","FOR"),
	]

	PO_no = models.CharField(max_length=200)
	SQ_SPO_DGRN_No = models.CharField(max_length=200)
	Status = models.CharField(max_length=100,choices=status_choices,default='OPEN')
	PO_Date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	PO_Description = models.CharField(max_length=500)
	PO_type = models.CharField(max_length=100,choices=po_type_choices)
	Transaction_category = models.CharField(max_length=200)
	Site = models.CharField(max_length=100,choices=po_site_choices)
	Customer_Code = models.ForeignKey(Party, related_name="Customer_Code", on_delete=models.PROTECT)
	Customer_Name = models.ForeignKey(Party, related_name="Customer_Name", on_delete=models.PROTECT)
	Site_address = models.CharField(max_length=100,choices=po_site_address_choices)
	Accounting_Site = models.CharField(max_length=100,choices=accounting_site_choices)
	Ac_code = models.CharField(max_length=200)
	Currency = models.CharField(max_length=3,choices=currency_choices,default='INR')
	Exchange_Rates = models.CharField(max_length=200)
	Credit_Terms = models.CharField(max_length=100)
	Delivery_Terms = models.CharField(max_length=100,choices=delivery_term_choices)
	Delivery_Mode = models.CharField(max_length=100,choices=delivery_mode_choices)
	Reference = models.CharField(max_length=200,blank=True)
	Inco_Terms = models.CharField(max_length=100,choices=inco_terms_choices, default="FOB")
	Remarks = models.TextField(max_length=500,blank=True)
	Comments = models.TextField(max_length=500,blank=True)

	def __str__(self):
		return self.PO_Description


"""class Notification(models.Model):
	order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE, related_name="noti_from_user", null=True, blank=True)
	user = models.ForeignKey(Muser, on_delete=models.CASCADE, related_name="noti_to_user")
	text_preview = models.CharField(max_length=90, blank=True)

	def __str__(self):
		return self.text_preview"""

class ItemCategory(models.Model):
	item_category_status = [
		('Open', 'Open'),
		('Rejected', 'Rejected'),
		('Released', 'Released'),
		('Approved', 'Approved'),
		('Closed', 'Closed'),
		('Cancelled', 'Cancelled'),
	]
	
	category_code = models.AutoField(primary_key=True,default=1)
	category_description = models.CharField(max_length=500, default="Category 1")
	item_category_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	status = models.CharField(max_length=20, choices=item_category_status, default='Open' )

	def __str__(self):
		return self.category_description
	class Meta:
		verbose_name= "Item	Categories"


class ItemGroup(models.Model):
	item_group_status = [
		('Open', 'Open'),
		('Rejected', 'Rejected'),
		('Released', 'Released'),
		('Approved', 'Approved'),
		('Closed', 'Closed'),
		('Cancelled', 'Cancelled'),
	]

	group_code = models.AutoField(primary_key=True, default=1)
	group_description = models.CharField(max_length=500,default="NIL")
	group_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	status = models.CharField(max_length=20, choices=item_group_status, default='Open' )

	def __str__(self):
		return self.group_description

class Item(models.Model):
	item_status = [
		('Open', 'Open'),
		('Rejected', 'Rejected'),
		('Released', 'Released'),
		('Approved', 'Approved'),
		('Closed', 'Closed'),
		('Cancelled', 'Cancelled'),
	]

	item_site = [
		('1', 'Multidimensions'),
		('2', 'Tech-Pioneer'),
	]

	item_code = models.CharField(max_length=500,primary_key=True)
	item_description = models.TextField(max_length=500)
	item_name = models.TextField(max_length=200)
	item_type = models.CharField(max_length=200)
	item_category = models.ForeignKey(ItemCategory, related_name='item_category', on_delete=models.PROTECT)
	item_group = models.ForeignKey(ItemGroup, related_name='item_group', on_delete=models.PROTECT)
	item_date = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=20, choices=item_status, default='Open',)
	alternate_sw_code = models.CharField(max_length=200)
	site = models.CharField(max_length=25, choices=item_site, default="Multidimensions")
	HSN_code = models.CharField(max_length=200)
	#is_approved =  models.BooleanField(default=False)

	def __str__(self):
		return self.item_code
		