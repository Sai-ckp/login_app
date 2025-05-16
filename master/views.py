from django.shortcuts import render

# Create your views here.
from django.forms import inlineformset_factory

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .forms import StoreDetailForm
from .models import StoreDetail
from django.http import JsonResponse
from django.db import connection 
from django.contrib import messages


# Store
def store_list(request):

    """Display all store with options to add, edit, and delete."""

    store = StoreDetail.objects.all()

    return render(request, 'master/store_list.html', {'store': store})
 
from django.contrib import messages

from django.contrib import messages  # import this

def store_add(request):
    if request.method == 'POST':
        form = StoreDetailForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Store added successfully!")  # ✅ set the message
            return redirect('store_list')  # redirect to store_list.html
    else:
        form = StoreDetailForm()

    return render(request, 'master/store_detail_form.html', {
        'form': form,
        'title': 'Add Store',
        "hide_logout": True
    })

 
def store_edit(request, pk):

    """Edit an existing store."""

    store = get_object_or_404(StoreDetail, pk=pk)

    if request.method == 'POST':

        form = StoreDetailForm(request.POST, instance=store)

        if form.is_valid():

            form.save()

            return redirect('store_list')

    else:

        form = StoreDetailForm(instance=store)
 
    return render(request, 'master/store_detail_form.html', {'form': form, 'title': 'Edit Store', "hide_logout": True})
 
def store_delete(request, pk):

    """Delete a store."""

    store = get_object_or_404(StoreDetail, pk=pk)

    if request.method == 'POST':

        store.delete()

        return redirect('store_list')

    return render(request, 'master/store_detail_form.html', {'store': store})
 
def store_view(request, pk):

   """Display a store in view-only mode."""

   store = get_object_or_404(StoreDetail, pk=pk)

   form = StoreDetailForm(instance=store)

   return render(request, 'master/store_detail_form.html', {'form': form, 'title': 'View Store', 'view_mode': True, "hide_logout": True})

