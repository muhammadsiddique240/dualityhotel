from django.shortcuts import render, get_object_or_404, redirect
from .models import HotelRoom, Booking
from .forms import BookingForm, ContactForm
from django.contrib import messages

def home(request):
    featured_rooms = HotelRoom.objects.filter(is_available=True)[:3]
    return render(request, 'hotel/home.html', {'featured_rooms': featured_rooms})

def room_list(request):
    rooms = HotelRoom.objects.filter(is_available=True)
    return render(request, 'hotel/room_list.html', {'rooms': rooms})

def room_detail(request, room_id):
    room = get_object_or_404(HotelRoom, id=room_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.room = room
            booking.save()
            return redirect('booking_success')
    else:
        form = BookingForm(initial={'room': room})
    
    return render(request, 'hotel/room_detail.html', {'room': room, 'form': form})

def booking_success(request):
    return render(request, 'hotel/booking_success.html')

def about(request):
    return render(request, 'hotel/about.html')

def gallery(request):
    return render(request, 'hotel/gallery.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'hotel/contact.html', {'form': form})

from .models import FoodItem, FoodOrder

def menu_view(request):
    categories = [
        ('Starters', FoodItem.objects.filter(category='STARTER', is_available=True)),
        ('Main Courses', FoodItem.objects.filter(category='MAIN_COURSE', is_available=True)),
        ('Desserts', FoodItem.objects.filter(category='DESSERT', is_available=True)),
        ('Beverages', FoodItem.objects.filter(category='BEVERAGE', is_available=True)),
        ('Snacks', FoodItem.objects.filter(category='SNACK', is_available=True)),
    ]
    
    context = {
        'categories': categories,
    }
    return render(request, 'hotel/menu.html', context)

def order_food(request):
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        room_number = request.POST.get('room_number')
        item_ids = request.POST.getlist('items')
        
        if customer_name and room_number and item_ids:
            order = FoodOrder.objects.create(
                customer_name=customer_name,
                room_number=room_number
            )
            total = 0
            for item_id in item_ids:
                item = FoodItem.objects.get(id=item_id)
                order.items.add(item)
                total += item.price
            
            order.total_price = total
            order.save()
            return redirect('order_confirmation')
            
    return redirect('menu')

def order_confirmation(request):
    return render(request, 'hotel/order_confirmation.html')

from django.contrib.auth import login
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'hotel/signup.html', {'form': form})
