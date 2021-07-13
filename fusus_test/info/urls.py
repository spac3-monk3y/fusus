from . import views
from django.urls import path

urlpatterns = [
    path('', view=views.info, name='info')
]
