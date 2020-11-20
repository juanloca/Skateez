
from django.contrib import admin
from django.urls import include, path
from skateez import views


app_name = 'skateez'

urlpatterns = [

    path('', views.IndexView.as_view(), name='index.html'),
    path('admin/', admin.site.urls),
    path('skateez/', include('skateez.urls')),
    
]
