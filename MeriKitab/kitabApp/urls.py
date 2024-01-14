
from django.urls import path
from .import views

urlpatterns = [

    path("", views.home, name="home"),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('buybook/', views.buybook, name='buybook'),
    path('sellbook/', views.sellbook, name='sellbook'),
    path('sellbook/<int:pk>', views.bookDetail, name='bookDetail'),
]
