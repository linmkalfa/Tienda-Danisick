from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import ProtectedError
from .models import Producto, Categoria


def catalogo(request):
    productos = Producto.objects.all()
    return render(request, "tienda/catalogo.html", {"productos": productos})


@login_required
def producto_nuevo(request):
    if request.method == "POST":
        Producto.objects.create(
            nombre=request.POST["nombre"],
            precio=request.POST["precio"],
            stock=request.POST["stock"],
            categoria_id=request.POST["categoria"],
        )
        messages.success(request, "Producto creado.")
        return redirect("catalogo")

    categorias = Categoria.objects.all()
    return render(request, "tienda/producto_form.html", {"categorias": categorias})


@login_required
def producto_editar(request, id):
    producto = Producto.objects.get(id=id)

    if request.method == "POST":
        producto.nombre = request.POST["nombre"]
        producto.precio = request.POST["precio"]
        producto.stock = request.POST["stock"]
        producto.categoria_id = request.POST["categoria"]
        producto.save()
        messages.success(request, "Producto actualizado.")
        return redirect("catalogo")

    categorias = Categoria.objects.all()
    return render(request, "tienda/producto_form.html",
        {"producto": producto, "categorias": categorias})


@login_required
def producto_eliminar(request, id):
    producto = Producto.objects.get(id=id)
    if request.method == "POST":
        try:
            producto.delete()
            messages.success(request, "Producto eliminado.")
        except ProtectedError:
            messages.warning(request, "No se puede eliminar: está en un pedido.")
    return redirect("catalogo")