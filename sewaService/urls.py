from django.urls import path
from . import views
from .views import ServiceCreateView, ServiceListView, ServiceDetailView, ServiceUpdateView, ServiceDeleteView

urlpatterns = [
    path('', views.index, name='sewa-home'),
    path('service/', ServiceListView.as_view(), name='service-list'),
    path('service/new/', ServiceCreateView.as_view(), name='service-create'),
    path('service/<int:pk>/', ServiceDetailView.as_view(), name='service-detail'),
    path('service/<int:pk>/update', ServiceUpdateView.as_view(), name='service-update'),
    path('service/<int:pk>/delete', ServiceDeleteView.as_view(), name='service-delete'),
]