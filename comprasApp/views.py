from django.shortcuts import redirect, get_object_or_404, render
from django.db.models import Q
from .models import Categoria, Unidad
from .forms import CategoriaForm, UnidadForm,CategoriaFormSinEstado,UnidadFormSinEstado


# Vistas para Categoria
def listarcategoria(request):
    queryset = request.GET.get("buscar")
    categoria = Categoria.objects.filter(estado=True)
    if queryset:
        categoria = Categoria.objects.filter(
            Q(descripcion__icontains=queryset), estado=True).distinct()
    context = {'categoria': categoria}
    return render(request, "comprasApp/listarCategoria.html", context)

def agregarcategoria(request):
    if request.method == "POST":
        form = CategoriaFormSinEstado(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listarcategoria")
    else:
        form = CategoriaFormSinEstado()
    context = {'form': form}
    return render(request, "comprasApp/agregarCategoria.html", context)

def editarcategoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect("listarcategoria")
    else:
        form = CategoriaForm(instance=categoria)
    context = {"form": form}
    return render(request, "comprasApp/editarCategoria.html", context)

def eliminarcategoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria.estado = False
    categoria.save()
    return redirect("listarcategoria")

# Vistas para Unidad
def listarunidad(request):
    queryset = request.GET.get("buscar")
    unidad = Unidad.objects.filter(estado=True)
    if queryset:
        unidad = Unidad.objects.filter(
            Q(descripcion__icontains=queryset), estado=True).distinct()
    context = {'unidad': unidad}
    return render(request, "comprasApp/listarUnidad.html", context)

def agregarunidad(request):
    if request.method == "POST":
        form = UnidadFormSinEstado(request.POST)
        if form.is_valid():
            form.save()
            return redirect("listarunidad")
    else:
        form = UnidadFormSinEstado()
    context = {'form': form}
    return render(request, "comprasApp/agregarUnidad.html", context)

def editarunidad(request, id):
    unidad = get_object_or_404(Unidad, id=id)
    if request.method == "POST":
        form = UnidadForm(request.POST, instance=unidad)
        if form.is_valid():
            form.save()
            return redirect("listarunidad")
    else:
        form = UnidadForm(instance=unidad)
    context = {"form": form}
    return render(request, "comprasApp/editarUnidad.html", context)

def eliminarunidad(request, id):
    unidad = get_object_or_404(Unidad, id=id)
    unidad.estado = False
    unidad.save()
    return redirect("listarunidad")
