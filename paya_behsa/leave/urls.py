from django.urls import path

from . import views

urlpatterns=[
    path('', views.index, name='leaves'),
    # path('state/', views.get_all_states_city, name='state'),
    # path('set_state/', views.set_state_and_city, name='state'),
    path('excel/', views.get_excel, name='excel'),
    path('confirm/', views.confirm, name='confirm'),
    path('map/', views.get_map, name='map'),
]