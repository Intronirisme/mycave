from django.urls import path
from showroom import views

from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='mycave'),
    path('ajax/catalog/', views.catalog, name ="catalog"),
    path('ajax/countrylist/', views.countrylist, name ="county"),
]