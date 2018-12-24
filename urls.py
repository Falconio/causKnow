from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'causknow'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('upload/', views.upload, name='upload'),
    path('sparql/', views.SPARQLQuery, name='sparql'),
    path('results/', views.SPARQLQuery, name='results')
] 
urlpatterns += static(settings.MEDIA_URL, 
                          document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
