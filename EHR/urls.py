from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'', views.patient_list, name="patient_list"),
    url(r'^list/', views.patient_list, name="patient_list"),
    url(r'^update/', views.patient_update, name="patient_update"),
    url(r'^visit', views.visit_update, name="visit_update"),
]