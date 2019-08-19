"""graphweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import url, include
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from datanalyse import views as views1
# from django.contrib.auth import views as views2
from datanalyse.forms import LoginForm
# from django.contrib.auth.decorators import login_required
from datanalyse.forms import RegistrationForm


app_name = "datanalyse"
urlpatterns = [

    #path('$',  views.homeview, name='home'),
    #path('(?P<username>[\w.@+-]+)/$',  views.UserPortsListView.as_view(), name='index'),
    path('home/$',  views1.UserPortsListView.as_view(), name='index'),
    path('$', views1.login, name='login'),
    path('logout/$', views1.logout, {'next_page': '/'}, name='logout'),
    path('register/$', views1.RegisterUser.as_view(), name='register'),
    path('(?P<pk>[0-9]+)/$',views1.DetailView.as_view(), name='detail'),
    path('sell/(?P<pk>\d+)$',views1.SellStock.as_view(), name='sell-detail'),
    path('ss/(?P<pk>\d+)$', views1.Sell.as_view(), name='ss'),
    path('howto/$',  views1.howtoview.as_view(), name='howto'),
    path('buy/$', views1.buyview.as_view(), name='buystock'),
    # path('autocomplete/$',views1.AutoCompleteView.as_view(), name='autocomplete'),
    path('news/$', views1.newsView.as_view(), name='news'),
    path('buys/$', views1.buy_category, name='buy_category'),
    path('finalbuy/$', views1.FinalBuy.as_view(), name='finalbuy'),
    path('learn/$',  views1.learnview.as_view(), name='learn'),
]
