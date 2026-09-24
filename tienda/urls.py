from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalogo, name='catalogo'),
    path('producto/nuevo/', views.producto_nuevo, name='producto_nuevo'),
    path('producto/<int:id>/editar/', views.producto_editar, name='producto_editar'),
    path('producto/<int:id>/eliminar/', views.producto_eliminar, name='producto_eliminar'),
]