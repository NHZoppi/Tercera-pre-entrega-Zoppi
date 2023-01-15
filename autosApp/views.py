from django.shortcuts import render, redirect
from .forms import AutoForm, VentaForm, SucursalForm, AutoFilter
from .models import Sucursal, Auto, Venta

# Create your views here.

    # Pagina Home.
def inicio(request):
    return render(request, 'paginas/index.html')

    #Agregar Auto
def auto_create(request):
    sucursales = Sucursal.objects.all()
    if not sucursales:
        return redirect('SucursalNueva') # No se pueden agregar Autos, sin Sucursales.
    if request.method == "POST":
        form = AutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ListarAutos')
    else:
        form = AutoForm()
    return render(request, 'paginas/auto_create.html', {'form': form})

    # Agregar Sucursal
def sucursal_create(request):
    if request.method == "POST":
        form = SucursalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('paginas/listas/sucursal_list')
    else:
        form = SucursalForm()
    return render(request, 'paginas/sucursal_form.html', {'form': form})

    # Agregar una venta
def venta_create(request):
    if request.method == "POST":
        form = VentaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ListarVentas')
    else:
        form = VentaForm()
    return render(request, 'paginas/venta.html', {'form': form})


    # Filtro x Auto (TIENE QUE SER EXACTO LO QUE SE BUSCA)
def buscar_auto(request):
    f = AutoFilter(request.GET, queryset=Auto.objects.all())
    return render(request, 'paginas/buscar_auto.html', {'filter': f})


    # Vista de listas
def lista_autos(request):
    autos = Auto.objects.all()
    return render(request, 'paginas/listas/auto_list.html', {'autos': autos})

def lista_ventas(request):
    ventas = Venta.objects.all()
    return render(request, "paginas/listas/venta_list.html", {"ventas":ventas})

def lista_sucursal(request):
    sucursales = Sucursal.objects.all()
    return render(request, "paginas/listas/sucursal_list.html", {"sucursales":sucursales})