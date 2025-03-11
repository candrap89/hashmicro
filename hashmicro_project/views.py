import os
import signal
from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import redirect

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import Product
from .forms import ProductForm


def custom_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('product_list')

def index(request):
    return render(request, 'hashmicro_project/index.html')

@login_required
def product_list(request):
    print(request.user.get_all_permissions())
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

@login_required
@permission_required('hashmicro_project.view_product', raise_exception=True)
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})

@login_required
@permission_required('hashmicro_project.add_product', raise_exception=True)
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.updated_by = request.user
            product.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})

@login_required
@permission_required('hashmicro_project.delete_product', raise_exception=True)
def product_bulk_delete(request):
    if request.method == 'POST':
        selected_products = request.POST.getlist('products')
        if selected_products:
            Product.objects.filter(id__in=selected_products).delete()
            messages.success(request, 'Selected products have been deleted successfully.')
        else:
            messages.warning(request, 'No products were selected for deletion.')
    return redirect('product_list')

@login_required
@permission_required('hashmicro_project.change_product', raise_exception=True)
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.updated_by = request.user
            product.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'product_form.html', {'form': form})

@login_required
@permission_required('hashmicro_project.delete_product', raise_exception=True)
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'product_confirm_delete.html', {'product': product})

def index(request):
    return render(request, 'hashmicro_project/index.html')

@csrf_exempt
def uninstall(request):
    if request.method == 'POST':
        # Terminate the Django application
        try:
             os.kill(os.getpid(), signal.SIGTERM)
        except Exception as e:
            print(e)
            return JsonResponse({'status': 'error', 'message': 'Failed to terminate application!'}, status=500)
        return JsonResponse({'status': 'success', 'message': 'Application terminated.'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method!.'}, status=400)