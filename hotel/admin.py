from django.contrib import admin
from .models import HotelRoom, Booking, ContactMessage

@admin.register(HotelRoom)
class HotelRoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price_per_night', 'max_guests', 'is_available')
    search_fields = ('name', 'description')
    list_filter = ('is_available', 'category')
    ordering = ('price_per_night',)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'room', 'check_in', 'check_out', 'status', 'payment_status', 'created_at')
    list_filter = ('status', 'payment_status', 'room', 'check_in')
    search_fields = ('customer_name', 'email', 'phone')
    date_hierarchy = 'check_in'
    actions = ['mark_as_paid', 'mark_as_confirmed']

    @admin.action(description='Mark selected bookings as Paid')
    def mark_as_paid(self, request, queryset):
        queryset.update(payment_status='PAID')

    @admin.action(description='Mark selected bookings as Confirmed')
    def mark_as_confirmed(self, request, queryset):
        queryset.update(status='CONFIRMED')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email', 'message')

from .models import FoodItem, FoodOrder

@admin.register(FoodItem)
class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_available')
    list_filter = ('category', 'is_available')
    search_fields = ('name',)

@admin.register(FoodOrder)
class FoodOrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'room_number', 'total_price', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('customer_name', 'room_number')
