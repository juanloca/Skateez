#URLS APP

from django.urls import path
from . import views
from django.urls import path
from skateez.views import IndexView, DetailView, ResultsView, ListaTabla, Create, Update, Delete
from django.conf.urls import url, include
from django.conf.urls import url
from django.contrib.auth.decorators import login_required

app_name = 'skateez'


urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
	path('tabla/', login_required(ListaTabla.as_view()), name='tabla'),
	path('author/add/', Create.as_view(), name='author-add'),
    path('author/<int:pk>/', Update.as_view(), name='author-update'),
    path('author/<int:pk>/delete/', Delete.as_view(), name='author-delete'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('welcome/',views.welcome, name='welcome'),

]

