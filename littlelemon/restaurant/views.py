# from django.http import HttpResponse
from django.shortcuts import render
from .forms import BookingForm
from .models import Menu



# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

# views.py


def menu(request):
    menus = Menu.objects.all()  # Assuming Menu is your model for storing menu items
    context = {'menus': menus}
    return render(request, 'menu.html', context)


def menu_detail(request, item_id):
    menu_item = get_object_or_404(Menu, id=item_id)
    context = {'menu_item': menu_item}
    return render(request, 'menu_detail.html', context)


def display_menu_items(request, pk=None):
    if pk:
        menu_item = Menu.objects.get(pk=pk)
    else:
        menu_item = ''

    return render(request, 'menu_item.html', {'menu_item': menu_item})

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

