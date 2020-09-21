from django.urls import include,path

from . import views

app_name='multierp'
urlpatterns = [
    path('login', views.loginreq, name='login_req'),
    path('logout', views.logoutreq, name='logout_req'),
    #path('register', views.register, name='register'),

    #---------------- Dash Board -------------------
    path('mainpage', views.mainpage, name='mainpage'),

    #------------ Create order ------------
    path('create', views.createOrder, name="create_order"),
   
    #------------ Update order ------------
    path('update/<str:pk>/', views.updateOrder, name="update_order"),

    #------------ Delete order ------------
    path('delete/<str:pk>/', views.deleteOrder, name="delete_order"),

    #------------ Order Details------------
    path('detail/<str:pk>/', views.detailOrder, name="detail_order"),

    path('notifications/', views.notifications, name='notifications'),

]