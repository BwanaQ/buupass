# api/urls.py
from django.urls import path, include
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    path('organisations/', cache_page(60*5)(views.ListBusOrganisation.as_view())),
    path('organisation/<int:pk>/', cache_page(60*5)(views.DetailBusOrganisation.as_view())),

    path('routes/', cache_page(60*5)(views.ListRoute.as_view())),
    path('route/<int:pk>/', cache_page(60*5)(views.DetailRoute.as_view())),

    path('buses/',cache_page(60*5)( views.ListBus.as_view())),
    path('bus/<int:pk>/', cache_page(60*5)(views.DetailBus.as_view())),

    path('schedules/', cache_page(60*5)(views.ListSchedule.as_view())),
    path('schedule/<int:pk>/', cache_page(60*5)(views.DetailSchedule.as_view())),

    # path('rest-auth/', include('rest_auth.urls')),
]
