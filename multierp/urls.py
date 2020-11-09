from django.urls import include,path

from . import views

app_name='multierp'
urlpatterns = [
    path('login', views.loginreq, name='login_req'),
    path('logout', views.logoutreq, name='logout_req'),
    #path('register', views.register, name='register'),


    #------------------ HOMEPAGE -----------------
    path('homepage',views.homepage,name='homepage'),

    #====================== SALES ORDER ============================

    #------------ SALES ORDER PAGE------------------
    path('salesorderpage', views.salesorderpage, name='salesorderpage'),
    
    #------------ Create order ------------
    path('createsalesorder', views.createSalesOrder, name="createsalesorder"),
   
    #------------ Update order ------------
    path('updatesalesorder/<str:pk>/', views.updateSalesOrder, name="updatesalesorder"),

    #------------ Delete order ------------
    path('deletesalesorder/<str:pk>/', views.deleteSalesOrder, name="deletesalesorder"),

    #------------------------ Sales Order Details -------------------------
    path('salesorderdetails/<str:pk>', views.salesorderDetails, name="salesorderdetails"),

    #====================== PURCHASE ORDER ============================

    #------------ Purchase order page ------------------
    path('purchaseorderpage', views.purchaseorderpage, name='purchaseorderpage'),
    
    #------------ Create order ------------
    path('createpurchaseorder', views.createPurchaseOrder, name="createpurchaseorder"),
   
    #------------ Update order ------------
    path('updatepurchaseorder/<str:pk>/', views.updatePurchaseOrder, name="updatepurchaseorder"),

    #------------ Delete order ------------
    path('deletepurchaseorder/<str:pk>/', views.deletePurchaseOrder, name="deletepurchaseorder"),

    #------------------------ Purchase Order Details -------------------------
    path('purchaseorderdetails/<str:pk>', views.purchaseorderDetails, name="purchaseorderdetails"),

    #==================================================================

    #======================= Items =================================

    #----------------------- Item Page -------------------------------
    path('itempage', views.itemPage, name='itempage'),   
    
    #----------------------- Create Item -----------------------------
    path('createitem', views.createItem, name='createitem'),

    #----------------------- Delete Item -----------------------------
    path('deleteitem/<str:pk>/', views.deleteItem, name="deleteitem"),

    #----------------------- Update Item -----------------------------
    path('updateitem/<str:pk>/', views.updateItem, name="updateitem"),

    #----------------------- Details Item -----------------------------
    path('itemdetails/<str:pk>/', views.itemDetails, name="itemdetails"),

    #================================================================

    #========================== Party ==============================
    
    #------------------------ Party Page ------------------------
    path("partypage",views.partypage,name="partypage"),
    
    #------------------------ Create Party ----------------------
    path('create_party', views.createParty, name='createparty'),

    #------------------------ Update Party ----------------------
    path('updateparty/<str:pk>/', views.updateParty, name="updateparty"),

    #------------------------ Delete Party ----------------------
    path('deleteparty/<str:pk>/', views.deleteParty, name="deleteparty"),
    
    #------------------------ Party Details ----------------------
    path('partydetails/<str:pk>', views.partyDetails, name="partydetails")
    #=========================================================================

]