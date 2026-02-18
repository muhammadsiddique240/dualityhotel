from django.db import models

class HotelRoom(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    CATEGORY_CHOICES = [
        ('LUXURY', 'Luxury'),
        ('DELUXE', 'Deluxe'),
        ('BUSINESS', 'Business'),
        ('ECONOMY', 'Economy'),
        ('STANDARD', 'Standard'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='STANDARD')
    inclusions = models.TextField(help_text="Comma-separated list of inclusions (e.g., Breakfast, Wifi)", blank=True)
    food_menu = models.TextField(help_text="JSON or text list of food items and prices", blank=True)
    
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price in PKR")
    image = models.ImageField(upload_to='rooms/', blank=True, null=True)
    image_url = models.URLField(max_length=500, blank=True, null=True)
    max_guests = models.PositiveIntegerField()
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class Booking(models.Model):
    customer_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.PositiveIntegerField()
    room = models.ForeignKey(HotelRoom, on_delete=models.CASCADE)
    
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('CANCELLED', 'Cancelled'),
        ('COMPLETED', 'Completed'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    
    PAYMENT_STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PAID', 'Paid'),
        ('REFUNDED', 'Refunded'),
    ]
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='PENDING')
    
    created_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        delta = self.check_out - self.check_in
        return self.room.price_per_night * delta.days

    def __str__(self):
        return f"Booking {self.id} - {self.customer_name}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"

class FoodItem(models.Model):
    CATEGORY_CHOICES = [
        ('STARTER', 'Starter'),
        ('MAIN_COURSE', 'Main Course'),
        ('DESSERT', 'Dessert'),
        ('BEVERAGE', 'Beverage'),
        ('SNACK', 'Snack'),
    ]
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price in PKR")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='MAIN_COURSE')
    image_url = models.URLField(max_length=500, blank=True, null=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.price} PKR)"

class FoodOrder(models.Model):
    customer_name = models.CharField(max_length=200)
    room_number = models.CharField(max_length=10)
    items = models.ManyToManyField(FoodItem)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    STATUS_CHOICES = [
        ('ORDERED', 'Ordered'),
        ('PREPARING', 'Preparing'),
        ('DELIVERED', 'Delivered'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ORDERED')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order for Room {self.room_number} - {self.status}"
