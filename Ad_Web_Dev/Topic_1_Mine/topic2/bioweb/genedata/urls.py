from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gene/<int:pk>', views.gene, name='gene'), # connect gene to tamplate
    path('list/<str:type>', views.list, name='list'), # new path for list view
    path('poslist/', views.poslist, name='poslist'),
    path('delete/<int:pk>', views.delete, name='delete'), # new path for delete view
]