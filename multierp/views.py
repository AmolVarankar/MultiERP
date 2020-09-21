from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login,authenticate,logout
from django.template import loader
from django.urls import reverse
from django import forms
from .form import CreateOrderForm, UpdateOrderForm1, UpdateOrderForm2, UpdateOrderForm3, SignUpForm
from django.db.models import Q
from django.contrib import messages
from .filters import OrderFilter

from .models import Muser, Order, Notification

#---------------------- Homepage --------------------

def index(request):
	return render(request = request,
				  template_name = "multierp/index.html",)


#-------------------- Accounts Page --------------------

def mainpage(request):
	orders = Order.objects.all().order_by('-date_created')
	total_orders = Order.objects.all().count()
	delivered = Order.objects.filter(status='S').count()
	pending = Order.objects.filter(~Q(status ='S')).count()

	uid = request.user.id
	get_muser = Muser.objects.get(id=uid)
	get_usertype = get_muser.user_type

	orderFilter = OrderFilter(request.GET, queryset=orders) 
	orders = orderFilter.qs

	context = {'orders':orders,'total_orders':total_orders, 'delivered':delivered, 'pending':pending, 'get_usertype':get_usertype, 'filter':orderFilter}
	return render(request, 'multierp/mainpage.html', context)


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
			 return HttpResponseRedirect('mainpage')
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


#------------------ Create Order --------------------

def createOrder(request):
	action = 'create'

		
	user = request.user
	uid = request.user.id
	get_muser = Muser.objects.get(id=uid)
	get_usertype = get_muser.user_type

	if get_usertype == 'Sal':
		form = CreateOrderForm()
		if request.method == 'POST':
			form = CreateOrderForm(request.POST)
			if form.is_valid():
				form.save()
				return HttpResponseRedirect('mainpage')

		context =  {'action':action, 'form':form, 'get_muser':get_muser}
		return render(request, 'multierp/order_form.html', context)
	else :

		return HttpResponseRedirect('mainpage')




#------------------ Delete Order --------------------
def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == 'POST':
		order.delete()
		return redirect('multierp:mainpage')
		
	return render(request, 'multierp/delete_item.html', {'item':order})	



#------------------ Update Order --------------------
def updateOrder(request, pk):
	action = 'update'
	order = Order.objects.get(id=pk)	
	uid = request.user.id
	user = Muser.objects.get(id=uid)


	if order.status == "O":
		form = UpdateOrderForm1(instance=order)
	elif order.status == "TA" or order.status == "TNA":
		form = UpdateOrderForm2(instance=order)
	else :
		form = UpdateOrderForm3(instance=order)

	if request.method == 'POST':
		if order.status == "O":
			form = UpdateOrderForm1(request.POST, instance=order)
		elif order.status == "TA" or order.status == "TNA":
			form = UpdateOrderForm2(request.POST, instance=order)
		else :
			form = UpdateOrderForm3(request.POST, instance=order)
		#form = UpdateOrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			N = Notification(user=user, order=order,text_preview="Order Updated!!!")
			N.save()
			return redirect('multierp:mainpage')

	context =  {'action':action, 'form':form}
	return render(request, 'multierp/order_form.html', context)



	#--------------- Order Details --------------------

def detailOrder(request, pk):
	action = "details"
	order = Order.objects.get(id=pk)
	prod = order.product
	company = order.company
	current_status = order.status
	sales_registration = order.sales_registration
	operation_handler = order.operation_handler
	finance_handler = order.finance_handler
	shipping_handler = order.shipping_handler
	context = {'order':order,
	'current_status' : current_status,
	'sales_registration' : sales_registration,
	'operation_handler' : operation_handler,
	'finance_handler' : finance_handler,
	'shipping_handler' : shipping_handler,}

	return render(request, 'multierp/detail.html', context)



	#----------------- Notification ------------------

def notifications(request):
	action="create"
	notifications = Notification.objects.all()
	context = {'notifications': notifications,'action':action}

	return render(request, 'multierp/notifications.html', context)

def onlysales(request):
	users = Muser.objects.all()
	#for user in users:
	#	if user.user_type=="Sal"
	#		saleslist=saleslist+user

	usertype = Muser.objects.get(users.user_type == "sales")

	context = {'user':user.username, 'usertype':usertype}
	return render(request, 'multierp/onlysales.html', context)
