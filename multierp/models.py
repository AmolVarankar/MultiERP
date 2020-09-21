from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

#------------------(User Model)-----------------

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



#--------------- Order Model -----------------------

class Order(models.Model):

	OPEN = 'O'
	TECHNICALLY_APPROVED = 'TA'
	TECHNICALLY_DISAPPROVED = 'TNA'
	COMMERCIALLY_APPROVED = 'CA'
	COMMERCIALLY_DISAPPROVED = 'CNA'
	SHIPPED = 'S'

	status_choices = [
		(OPEN,'O'),
		(TECHNICALLY_APPROVED,'TA'),
		(TECHNICALLY_DISAPPROVED,'TNA'),
		(COMMERCIALLY_APPROVED,'CA'),
		(COMMERCIALLY_DISAPPROVED,'CNA'),
		(SHIPPED,'S'),]

	
	product = models.CharField(max_length=200)
	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	company = models.CharField(max_length=200)
	status = models.CharField(max_length=3,choices=status_choices,default='OPEN')
	
	user = models.ManyToManyField(Muser)
	sales_registration = models.ForeignKey(Muser, on_delete=models.CASCADE, related_name="sales_reg", null=True)
	operation_handler = models.ForeignKey(Muser, on_delete=models.CASCADE, related_name="oprn_handler", null=True)
	finance_handler = models.ForeignKey(Muser, on_delete=models.CASCADE, related_name="fin_handler", null=True)
	shipping_handler = models.ForeignKey(Muser, on_delete=models.CASCADE, related_name="ship_handler", null=True)

	
	def __str__(self):
		return self.product


class Notification(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="noti_from_user", null=True, blank=True)
	user = models.ForeignKey(Muser, on_delete=models.CASCADE, related_name="noti_to_user")
	text_preview = models.CharField(max_length=90, blank=True)

	def __str__(self):
		return self.text_preview