from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from django.template import loader
from django.urls import reverse
from django import forms
from .form import *
from django.db.models import Q
from django.contrib import messages
from .filters import *
from django.contrib.auth.decorators import permission_required

from .models import *

# ===================================== HomePage =========================

def homepage(request):
	return render(request,'multierp/homepage.html')

#---------------------- welcome page --------------------

def index(request):
	return render(request = request,
				  template_name = "multierp/index.html",)

# ==================================== Order ===========================

# ============================== Purchase Order =====================================

def purchaseorderpage(request):
	orders = PurchaseOrder.objects.all()
	total_orders = PurchaseOrder.objects.all().count()
	delivered = PurchaseOrder.objects.filter(Status='Closed').count()
	pending = PurchaseOrder.objects.filter(~Q(Status ='Closed')).count()

	orderFilter = PurchaseOrderFilter(request.GET, queryset=orders) 
	searchpurchaseorders = orderFilter.qs

	context = {'orders':orders,'total_orders':total_orders, 'delivered':delivered, 'pending':pending, 'filter':orderFilter,'searchpurchaseorders':searchpurchaseorders}
	return render(request, 'multierp/purchaseorderpage.html', context)

#-------------------- create purchase order -------------------
def createPurchaseOrder(request):
	action='Create'
	form = CreatePurchaseOrderForm()
	if request.method == 'POST':
		form = CreatePurchaseOrderForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('purchaseorderpage')
	context =  {'form':form,'action':action}
	return render(request, 'multierp/createpurchaseorder.html', context)


#------------------ Delete Purchase Order --------------------
def deletePurchaseOrder(request, pk):
	order = PurchaseOrder.objects.get(id=pk)
	if request.method == 'POST':
		order.delete()
		return redirect('multierp:purchaseorderpage')
		
	return render(request, 'multierp/delete_item.html', {'item':order})	

#------------------- Update Purchase Order ------------------
def updatePurchaseOrder(request,pk):
	action='Update'
	order = PurchaseOrder.objects.get(id=pk)
	form = UpdatePurchaseOrderForm(instance=order)	
	if request.method == "POST":
		form = UpdatePurchaseOrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('multierp:purchaseorderpage')
	return render(request, 'multierp/createpurchaseorder.html',{"form":form,"action":action})

#-------------------------- Purchase Order Details ---------------------
def purchaseorderDetails(request,pk):
	order = PurchaseOrder.objects.get(pk=pk)
	context = {'order':order}
	return render(request, 'multierp/purchaseorderdetails.html',context)


#==================================================================================================

#-------------------- sales order Page --------------------

def salesorderpage(request):
	orders = SalesOrder.objects.all()
	total_orders = SalesOrder.objects.all().count()
	delivered = SalesOrder.objects.filter(Status='Closed').count()
	pending = SalesOrder.objects.filter(~Q(Status ='Closed')).count()

	orderFilter = SalesOrderFilter(request.GET, queryset=orders) 
	searchorders = orderFilter.qs

	context = {'orders':orders,'total_orders':total_orders, 'delivered':delivered, 'pending':pending, 'filter':orderFilter, 'searchorders':searchorders}
	return render(request, 'multierp/salesorderpage.html', context)


#------------------ Create Order --------------------

def createSalesOrder(request):
	action='Create'
	form = CreateSalesOrderForm()
	if request.method == 'POST':
		form = CreateSalesOrderForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('salesorderpage')

	context =  {'form':form,"action":action}
	return render(request, 'multierp/createsalesorder.html', context)



#------------------ Delete Order --------------------
def deleteSalesOrder(request, pk):
	order = SalesOrder.objects.get(id=pk)
	if request.method == 'POST':
		order.delete()
		return redirect('multierp:salesorderpage')
		
	return render(request, 'multierp/delete_item.html', {'item':order})	


#--------------------- Update Sales Order ------------------
def updateSalesOrder(request,pk):
	action='Update'
	order = SalesOrder.objects.get(id=pk)
	form = UpdateSalesOrderForm(instance=order)
	if request.method == "POST":
		form = UpdateSalesOrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('multierp:salesorderpage')
	return render(request, 'multierp/createsalesorder.html',{"form":form,"action":action})

#-------------------------- Sales Order Details ---------------------
def salesorderDetails(request,pk):
	order = SalesOrder.objects.get(pk=pk)
	context = {'order':order}
	return render(request, 'multierp/salesorderdetails.html',context)


# --------------------- Logout --------------------------
def logoutreq(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect("multierp:login_req")



#-------------------- Login ------------------------
def loginreq(request):
	form = AuthenticationForm()
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)

		if user is not None:
			 login(request, user) 
			 return HttpResponseRedirect('homepage')
	return render(request = request,
				  template_name = "multierp/login.html",
				  context={'form':form})

#------------------------ Register ---------------------

def register(request):
	form = SignUpForm()
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
	return render(request = request,
					template_name = "multierp/register.html",
					context={"form":form})

	#----------------- Notification ------------------

"""def notifications(request):
	action="create"
	notifications = Notification.objects.all()
	context = {'notifications': notifications,'action':action}

	return render(request, 'multierp/notifications.html', context)"""

#=============================== Item ======================================

# ----------------------- ItemPage --------------------------

def itemPage(request):
	items = Item.objects.all()
	total_items = items.count()
	latest_items = items.order_by('-item_date')[0:5]

	itemFilter = ItemFilter(request.GET, queryset=items)
	searchitems = itemFilter.qs

	context = {"total_items":total_items,"latest_items":latest_items,"filter":itemFilter,"items":items,"searchitems":searchitems}
	return render(request, 'multierp/itempage.html', context)

#------------------------- Create Item ------------------

#@permission_required('multierp:add_item')
def createItem(request):
	action= "Create"
	form = CreateItemForm()
	if request.method == "POST":
		form=CreateItemForm(request.POST)
		if form.is_valid:
			form.save()
		return HttpResponseRedirect('itempage')
	
	context = {'form':form,"action":action}
	return render(request, 'multierp/create_item.html', context)

def deleteItem(request,pk):
	item = Item.objects.get(pk=pk)
	if request.method == 'POST':
		item.delete()
		return redirect('multierp:itempage')
	return render(request, 'multierp/delete_item.html',{"item":item})	

def updateItem(request,pk):
	action= "Update"
	item = Item.objects.get(pk=pk)
	form = UpdateItemForm(instance=item)
	if request.method == "POST":
		form = UpdateItemForm(request.POST, instance=item)
		if form.is_valid():
			form.save()
			return redirect('multierp:itempage')
	return render(request, 'multierp/create_item.html',{"form":form,"action":action})
	
def itemDetails(request,pk):
	item = Item.objects.get(pk=pk)
	context = {'item':item}
	return render(request, 'multierp/itemdetails.html',context)

#=================================== PARTY ================================

#------------------- Create Party -------------------------

def createParty(request):
	action='Create'
	form = CreatePartyForm()
	if request.method == "POST":
		form=CreatePartyForm(request.POST)
		if form.is_valid:
			form.save()
		return HttpResponseRedirect('partypage')
	
	context = {'form':form,"action":action}
	return render(request, 'multierp/create_party.html',context)

def partypage(request):
	if request.method == 'GET':
		party= Party.objects.all()
	else:
		party= Party.objects.none()
	partycount = party.count()
	latest_party = Party.objects.all().order_by('-Party_Date')[0:5]

	itemParty=PartyFilter(request.GET, queryset=party)
	searchparty = itemParty.qs

	context={"partycount":partycount,"party":party,"filter":itemParty,"searchparty":searchparty,'latest_party':latest_party}
	return render(request, 'multierp/partypage.html',context)

def deleteParty(request, pk):
	party = Party.objects.get(id=pk)
	if request.method == 'POST':
		party.delete()
		return redirect('multierp:partypage')
	return render(request, 'multierp/delete_item.html',{"item":party})	

def updateParty(request,pk):
	action='Update'
	party = Party.objects.get(id=pk)
	form = UpdatePartyForm(instance=party)
	if request.method == "POST":
		form = UpdatePartyForm(request.POST, instance=party)
		if form.is_valid():
			form.save()
			return redirect('multierp:partypage')
	return render(request, 'multierp/create_party.html',{"form":form,"action":action})

def partyDetails(request,pk):
	party = Party.objects.get(pk=pk)
	context = {'party':party}
	return render(request, 'multierp/partydetails.html',context)
