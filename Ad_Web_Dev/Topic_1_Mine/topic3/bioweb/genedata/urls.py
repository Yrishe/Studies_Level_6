from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gene/<int:pk>', views.gene, name='gene'), # connect gene to tamplate
    path('list/<str:type>', views.list, name='list'), # new path for list view
    path('poslist/', views.poslist, name='poslist'),
    path('delete/<int:pk>', views.delete, name='delete'), # new path for delete view
    path('create_ec/', views.create_ec, name='create_ec'),
    path('create_gene/', views.create_gene, name='create_gene'),
    path('', views.GeneList.as_view(), name='index'),
    path('gene/<int:pk>', views.GeneDetail.as_view(), name='gene'),
    path('create_gene/', views.GeneCreate.as_view(), name='create_gene'),
    path('delete/<int:pk>', views.GeneDelete.as_views(), name='delete'),
]