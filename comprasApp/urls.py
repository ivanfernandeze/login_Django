from django.urls import path
from comprasApp.views import (
    listarcategoria, agregarcategoria, editarcategoria, eliminarcategoria,
    listarunidad, agregarunidad, editarunidad, eliminarunidad
)

urlpatterns = [
    path('', listarcategoria, name="listarcategoriaa"),
    path('agregarcategoria/', agregarcategoria, name="agregarcategoria"),
    path('editarcategoria/<int:id>/', editarcategoria, name="editarcategoria"),
    path('eliminarcategoria/<int:id>/', eliminarcategoria, name="eliminarcategoria"),

    path('unidad/', listarunidad, name="listarunidad"),
    path('agregarunidad/', agregarunidad, name="agregarunidad"),
    path('editarunidad/<int:id>/', editarunidad, name="editarunidad"),
    path('eliminarunidad/<int:id>/', eliminarunidad, name="eliminarunidad"),
]
