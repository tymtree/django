from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

app_name = 'prac1'
urlpatterns = [
		path('', views.IndexView.as_view(), name='index'),
		path('<int:pk>/details', views.DetailView.as_view(), name='details'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
