from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
	path('', views.index, name='index'),
    path('home/', views.index, name='index'),
	path('portfolio/', views.portfolio, name='portfolio'),
    path('certifications/', views.certifications, name='certifications'),
	path('blog/', views.blog, name='blog'),
	path('contact/', views.contact, name='contact'),
	path('video/', views.intro_video, name='video'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)