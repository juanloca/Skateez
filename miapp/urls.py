
from django.contrib import admin
from django.urls import include, path
from skateez import views
from rest_framework import routers
from skateez.api import views

router = routers.DefaultRouter()
router.register(r'tabla', views.TablaViewSet)
router.register(r'ejes', views.EjesViewSet)



app_name = 'skateez'

urlpatterns = [

    path('', views.IndexView.as_view(), name='index.html'),
    path('admin/', admin.site.urls),
    path('skateez/', include('skateez.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest-framework')),
    
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

