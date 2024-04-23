from django.urls import path
from . import views
urlpatterns = [
   path('', views.home, name='home'),
   path('cart/', views.show_cart, name='cart'),

   path('signup/',views.signup,name='signup'),
   path('signin/',views.signin,name='signin'),
   path('signout/',views.signout,name='signout'),
   path('<slug:slug_c>/',views.home,name='product_by_category'),

   path('<slug:slug_c>/<slug_p>/',views.prod_details,name='product_details'),
   path('detail_product/<pk>',views.detail_product,name='detail_product'),



]