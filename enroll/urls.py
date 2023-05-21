from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('save/', views.SaveData, name='save-data'),
    path('delete/', views.DeleteData, name='delete-data'),
    path('edit/', views.EditData, name='edit-data'),
]
