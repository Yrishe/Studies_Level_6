from django.urls import include, path

from . import api
from . import views

urlpatterns = [
    path('', views.GeneList.as_view(), name='index'),
    path('gene/<int:pk>', views.GeneDetail.as_view(), name='gene'), # connect gene to tamplate
    path('list/<str:type>', views.GeneList.as_view(), name='list'), # new path for list view
    path('poslist/', views.GeneList.as_view(), name='poslist'),
    path('delete/<int:pk>', views.GeneDelete.as_view(), name='delete'), # new path for delete view
    path('create_ec/', views.create_ec, name='create_ec'),
    path('create_gene/', views.GeneCreate.as_view(), name='create_gene'),
    path('update/<int:pk>', views.GeneUpdate.as_view(), name='update'),
    # path('list/<str:type>', views.GeneList.as_view(), name='list'),
    path('api/gene/<int:pk>/', api.gene_detail),
]