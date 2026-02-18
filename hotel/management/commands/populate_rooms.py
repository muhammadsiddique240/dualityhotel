from django.core.management.base import BaseCommand
from hotel.models import HotelRoom, FoodItem
from django.core.files.base import ContentFile
import requests

class Command(BaseCommand):
    help = 'Populates the database with initial room and food data'

    def handle(self, *args, **kwargs):
        # Room Data
        rooms_data = [
            # LUXURY
            {
                'name': 'The Royal Suite',
                'description': 'Experience the ultimate in luxury with our Royal Suite. Featuring a king-sized bed, private balcony with panoramic city views, a spacious living area, and a marble bathroom with a jacuzzi. Includes 24/7 butler service.',
                'price': 300000.00,
                'guests': 2,
                'category': 'LUXURY',
                'inclusions': 'Breakfast, Wifi, Spa Access, Airport Transfer, Butler Service',
                'food_menu': 'Club Sandwich: 1500 PKR\nCaesar Salad: 1200 PKR\nSteak: 5000 PKR',
                'image_url': 'https://images.unsplash.com/photo-1590490360182-c33d57733427?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80'
            },
            {
                'name': 'Presidential Penthouse',
                'description': 'The pinnacle of opulence. Our Presidential Penthouse spans the entire top floor, offering 360-degree views, a private infinity pool, personal gym, and exclusive access to the lounge.',
                'price': 1500000.00,
                'guests': 6,
                'category': 'LUXURY',
                'inclusions': 'All-inclusive, Private Chef, Chauffeur',
                'food_menu': 'Caviar: 50000 PKR\nLobster: 25000 PKR\nChampagne: 15000 PKR',
                'image_url': 'https://images.unsplash.com/photo-1631049307264-da0ec9d70304?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80'
            },
            {
                'name': 'Romantic Honeymoon Suite',
                'description': 'Create unforgettable memories in our Honeymoon Suite. Features rose petal turndown service, champagne on arrival, a heart-shaped bathtub, and a private terrace for romantic dinners.',
                'price': 200000.00,
                'guests': 2,
                'category': 'LUXURY',
                'inclusions': 'Breakfast, Wifi, Champagne, Romantic Dinner',
                'food_menu': 'Chocolate Strawberries: 2000 PKR\nWine: 5000 PKR\nCheese Platter: 3000 PKR',
                'image_url': 'https://images.unsplash.com/photo-1578683010236-d716f9a3f461?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80'
            },
            # DELUXE
            {
                'name': 'Ocean View Deluxe',
                'description': 'Wake up to the sound of waves in our Ocean View Deluxe room. Offers a stunning view of the ocean, a comfortable queen-sized bed, and modern amenities including a smart TV and high-speed wifi.',
                'price': 120000.00,
                'guests': 2,
                'category': 'DELUXE',
                'inclusions': 'Breakfast, Wifi, Gym Access',
                'food_menu': 'Fish & Chips: 2500 PKR\nBurger: 1800 PKR\nSoft Drink: 300 PKR',
                'image_url': 'https://images.unsplash.com/photo-1566073771259-6a8506099945?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80'
            },
            {
                'name': 'Family Garden Suite',
                'description': 'Perfect for families, this suite overlooks our lush gardens. Features two bedrooms, a kitchenette, and a cozy dining area. Direct access to the garden and pool area.',
                'price': 180000.00,
                'guests': 4,
                'category': 'DELUXE',
                'inclusions': 'Breakfast, Wifi, Pool Access, Kitchenette',
                'food_menu': 'Family Pizza: 3500 PKR\nPasta: 2000 PKR\nIce Cream: 500 PKR',
                'image_url': 'https://images.unsplash.com/photo-1582719508461-905c673771fd?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80'
            },
            {
                'name': 'Junior Suite',
                'description': 'A spacious suite with a separate sitting area, ideal for longer stays. Includes a mini-bar, large workspace, and a luxurious bathroom with a rain shower.',
                'price': 100000.00,
                'guests': 3,
                'category': 'DELUXE',
                'inclusions': 'Breakfast, Wifi, Lounge Access',
                'image_url': 'https://images.unsplash.com/photo-1618773928121-c32242e63f39?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80'
            },
             # BUSINESS
            {
                'name': 'Executive Business Room',
                'description': 'Designed for the modern business traveler. Includes a large workspace, ergonomic chair, high-speed internet, and access to meeting rooms. Relax after work in the comfortable king-sized bed.',
                'price': 85000.00,
                'guests': 1,
                'category': 'BUSINESS',
                'inclusions': 'Breakfast, Wifi, Meeting Room Access',
                'food_menu': 'Coffee: 500 PKR\nSandwich: 800 PKR\nSalad: 900 PKR',
                'image_url': 'https://images.unsplash.com/photo-1611892440504-42a792e24d32?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80'
            },
            {
                'name': 'Corporate Suite',
                'description': 'Premium suite for corporate guests. Features a private meeting area, printer/scanner, and complimentary laundry service.',
                'price': 95000.00,
                'guests': 2,
                'category': 'BUSINESS',
                'inclusions': 'Breakfast, Wifi, Laundry, Lounge Access',
                'image_url': 'https://images.unsplash.com/photo-1497366216548-37526070297c?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80'
            },
             # STANDARD
             {
                'name': 'Standard City Room',
                'description': 'A comfortable and affordable option for travelers who want to explore the city. Features a queen bed, en-suite bathroom, and essential amenities.',
                'price': 45000.00,
                'guests': 2,
                'category': 'STANDARD',
                'inclusions': 'Wifi',
                'food_menu': 'Burger: 800 PKR\nFires: 400 PKR\nSoda: 200 PKR',
                'image_url': 'https://images.unsplash.com/photo-1566665797739-1674de7a421a?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80'
            },
            {
                'name': 'Twin Standard',
                'description': 'Ideal for friends or colleagues sharing a room. Features two twin beds, a work desk, and a modern bathroom.',
                'price': 48000.00,
                'guests': 2,
                'category': 'STANDARD',
                'inclusions': 'Wifi',
                'image_url': 'https://images.unsplash.com/photo-1595576508898-0ad5c879a063?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80'
            },
             # ECONOMY
             {
                'name': 'Economy Single',
                'description': 'Compact and cozy room for the solo traveler on a budget. Includes a single bed, work desk, and shared bathroom facilities.',
                'price': 25000.00,
                'guests': 1,
                'category': 'ECONOMY',
                'inclusions': 'Wifi',
                'food_menu': 'Sandwich: 500 PKR\nJuice: 300 PKR',
                'image_url': 'https://images.unsplash.com/photo-1505693416388-b03463121229?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80'
            },
             {
                'name': 'Budget Double',
                'description': 'Affordable double room with basic amenities. Perfect for backpackers or budget-conscious couples.',
                'price': 30000.00,
                'guests': 2,
                'category': 'ECONOMY',
                'inclusions': 'Wifi',
                'image_url': 'https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80'
            }
        ]

        for data in rooms_data:
            room, created = HotelRoom.objects.update_or_create(
                name=data['name'],
                defaults={
                    'description': data['description'],
                    'price_per_night': data['price'],
                    'max_guests': data['guests'],
                    'image_url': data['image_url'],
                    'category': data['category'],
                    'inclusions': data['inclusions'],
                    'food_menu': data.get('food_menu', '')
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created room: {room.name}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Updated room: {room.name}'))

        # Food Data
        food_data = [
            # STARTERS
            {'name': 'Caesar Salad', 'price': 1200, 'category': 'STARTER', 'description': 'Fresh romaine lettuce with parmesan, croutons, and caesar dressing.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1550304943-4f24f54ddde9?auto=format&fit=crop&w=800&q=80'},
            {'name': 'Spring Rolls', 'price': 800, 'category': 'STARTER', 'description': 'Crispy vegetable spring rolls with sweet chili sauce.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1623341214825-9f4f963727da?auto=format&fit=crop&w=800&q=80'},
            {'name': 'Seekh Kabab', 'price': 1500, 'category': 'STARTER', 'description': 'Minced meat kababs grilled on skewers with traditional spices.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1599487488170-d11ec9c172f0?auto=format&fit=crop&w=800&q=80'},
            {'name': 'Prawn Tempura', 'price': 2200, 'category': 'STARTER', 'description': 'Crispy golden fried prawns served with soy dipping sauce.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1517093602195-b40af9688b46?auto=format&fit=crop&w=800&q=80'},
            {'name': 'Lentil Soup', 'price': 900, 'category': 'STARTER', 'description': 'Slow-cooked red lentils with Mediterranean herbs and lemon.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=800&q=80'},
            {'name': 'Bruschetta', 'price': 1100, 'category': 'STARTER', 'description': 'Toasted bread topped with fresh tomatoes, garlic, and basil oil.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1572656631137-7935297eff55?auto=format&fit=crop&w=800&q=80'},
            {'name': 'Beef Tikka', 'price': 1800, 'category': 'STARTER', 'description': 'Marinated beef cubes grilled to perfection with local spices.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1599487488170-d11ec9c172f0?auto=format&fit=crop&w=800&q=80'},
            {'name': 'Cream of Mushroom', 'price': 950, 'category': 'STARTER', 'description': 'Rich and velvety soup made with fresh portobello mushrooms.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1547592166-23ac45744acd?auto=format&fit=crop&w=800&q=80'},
            
            # MAIN COURSES
            {'name': 'Grilled Steak', 'price': 5000, 'category': 'MAIN_COURSE', 'description': 'Premium beef steak cooked to perfection, served with mashed potatoes.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1600891964092-4316c288032e?auto=format&fit=crop&w=800&q=80'},
            {'name': 'Fish & Chips', 'price': 2500, 'category': 'MAIN_COURSE', 'description': 'Crispy battered fish with golden fries and tartar sauce.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1519708227418-c8fd9a32b7a2?auto=format&fit=crop&w=800&q=80'},
            {'name': 'Pasta Alfredo', 'price': 2200, 'category': 'MAIN_COURSE', 'description': 'Fettuccine pasta in a rich creamy parmesan sauce.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1645112411341-6c4fd023714a?auto=format&fit=crop&w=800&q=80'},
            {'name': 'Chicken Karahi', 'price': 2800, 'category': 'MAIN_COURSE', 'description': 'Traditional rich and spicy chicken curry cooked in a wok.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?auto=format&fit=crop&w=800&q=80'},
            {'name': 'Mutton Biryani', 'price': 3500, 'category': 'MAIN_COURSE', 'description': 'Aromatic long-grain rice cooked with tender mutton and select spices.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1631515233156-f6336329fc5f?auto=format&fit=crop&w=800&q=80'},
            {'name': 'Margarita Pizza', 'price': 1800, 'category': 'MAIN_COURSE', 'description': 'Classic pizza with tomato sauce, fresh mozzarella, and basil.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&w=800&q=80'},
            {'name': 'Beef Burger', 'price': 2000, 'category': 'MAIN_COURSE', 'description': 'Juicy beef patty with caramelized onions, cheese, and special sauce.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1568901346375-23c9450c58cd?auto=format&fit=crop&w=800&q=80'},
            {'name': 'Mixed Grill Platter', 'price': 4500, 'category': 'MAIN_COURSE', 'description': 'An assortment of grilled kababs, tikkas, and chops.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1529193591184-b1d58069ecdd?auto=format&fit=crop&w=800&q=80'},
            {'name': 'Beef Wellington', 'price': 6500, 'category': 'MAIN_COURSE', 'description': 'Prime beef fillet coated in pâté and duxelles, wrapped in puff pastry.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1603360946369-dc9bb6258143?auto=format&fit=crop&w=800&q=80'},
            {'name': 'Pan-Seared Salmon', 'price': 4200, 'category': 'MAIN_COURSE', 'description': 'Fresh Atlantic salmon served with asparagus and lemon butter sauce.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1467003909585-2f8a72700288?auto=format&fit=crop&w=800&q=80'},
            {'name': 'Butter Chicken', 'price': 2600, 'category': 'MAIN_COURSE', 'description': 'Succulent chicken pieces in a silky tomato and butter-based sauce.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1603894584373-5ac82b2ae398?auto=format&fit=crop&w=800&q=80'},
            {'name': 'Mushroom Risotto', 'price': 2400, 'category': 'MAIN_COURSE', 'description': 'Creamy Arborio rice with earthy wild mushrooms and truffle oil.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1476124369491-e7addf5db371?auto=format&fit=crop&w=800&q=80'},
            {'name': 'Lamb Chops', 'price': 5500, 'category': 'MAIN_COURSE', 'description': 'Grilled New Zealand lamb chops with rosemary sauce.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1604351821811-13386050b86a?auto=format&fit=crop&w=800&q=80'},
            {'name': 'Lobster Thermidor', 'price': 8500, 'category': 'MAIN_COURSE', 'description': 'Luxurious lobster tail baked in a rich creamy brandy sauce.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1553163147-622ab57be1c7?auto=format&fit=crop&w=800&q=80'},
            {'name': 'Shepherd\'s Pie', 'price': 2800, 'category': 'MAIN_COURSE', 'description': 'Hearty minced meat pie topped with creamy mashed potatoes and cheese.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1594998813208-65744aa9ca2a?auto=format&fit=crop&w=800&q=80'},

            # DESSERTS
            {'name': 'Chocolate Lava Cake', 'price': 900, 'category': 'DESSERT', 'description': 'Warm chocolate cake with a gooey center, served with vanilla ice cream.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1624353365286-3f8d62daad51?auto=format&fit=crop&w=800&q=80'},
            {'name': 'Chocolate Brownie', 'price': 850, 'category': 'DESSERT', 'description': 'Rich and fudgy chocolate brownie loaded with walnuts.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1564355808539-22fda35bed7e?auto=format&fit=crop&w=800&q=80'},
            {'name': 'Gulab Jamun', 'price': 600, 'category': 'DESSERT', 'description': 'Traditional warm milk dumplings in a sweet cardamom syrup.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1589113333333-e18e3c368d37?auto=format&fit=crop&w=800&q=80'},
            {'name': 'Tiramisu', 'price': 1200, 'category': 'DESSERT', 'description': 'Classic Italian dessert with coffee-soaked ladyfingers and mascarpone.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?auto=format&fit=crop&w=800&q=80'},
            {'name': 'Cheesecake', 'price': 1100, 'category': 'DESSERT', 'description': 'Creamy New York style cheesecake with a berry compote.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1533134242443-d4fd215305ad?auto=format&fit=crop&w=800&q=80'},
            {'name': 'Fruit Platter', 'price': 1500, 'category': 'DESSERT', 'description': 'Selection of seasonal fresh tropical fruits artistically arranged.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1519996529931-28324d5a630e?auto=format&fit=crop&w=800&q=80'},
            {'name': 'Pistachio Ice Cream', 'price': 500, 'category': 'DESSERT', 'description': 'Handcrafted creamy ice cream with roasted pistachios.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1563805039-1b80cbc8628b?auto=format&fit=crop&w=800&q=80'},
            {'name': 'Apple Tart', 'price': 1000, 'category': 'DESSERT', 'description': 'Caramelized apples on a crisp pastry base with a hint of cinnamon.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1568571780765-9276ac5ad78a?auto=format&fit=crop&w=800&q=80'},
            
            # BEVERAGES
            {'name': 'Fresh Orange Juice', 'price': 600, 'category': 'BEVERAGE', 'description': 'Freshly squeezed seasonal oranges.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1613478223719-2ab802602423?auto=format&fit=crop&w=800&q=80'},
            {'name': 'Cappuccino', 'price': 500, 'category': 'BEVERAGE', 'description': 'Rich espresso with steamed milk foam.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1572442388796-11668a67e53d?auto=format&fit=crop&w=800&q=80'},
            {'name': 'Mango Lassi', 'price': 700, 'category': 'BEVERAGE', 'description': 'Cool and creamy yogurt drink blended with fresh mangoes.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1630953899906-d16511a72558?auto=format&fit=crop&w=800&q=80'},
            {'name': 'Fresh Lime Soda', 'price': 400, 'category': 'BEVERAGE', 'description': 'Refreshing lemon juice with club soda and a hint of mint.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1513558161293-cdaf765ed2fd?auto=format&fit=crop&w=800&q=80'},
            {'name': 'Iced Peach Tea', 'price': 550, 'category': 'BEVERAGE', 'description': 'Hand-picked tea leaves with natural peach flavor and ice.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1499638673689-79a0b5115d87?auto=format&fit=crop&w=800&q=80'},
            {'name': 'Honey Ginger Tea', 'price': 450, 'category': 'BEVERAGE', 'description': 'Soothing tea with fresh ginger, honey, and a touch of lemon.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1544787210-2213d2426687?auto=format&fit=crop&w=800&q=80'},
            {'name': 'Vanilla Shake', 'price': 750, 'category': 'BEVERAGE', 'description': 'Creamy vanilla milkshake topped with whipped cream.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1572490122747-3968b75cc699?auto=format&fit=crop&w=800&q=80'},
            {'name': 'Hot Chocolate', 'price': 800, 'category': 'BEVERAGE', 'description': 'Rich melted Belgian chocolate with steamed milk.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1544787210-2213d2426687?auto=format&fit=crop&w=800&q=80'},

            # SNACKS
            {'name': 'Club Sandwich', 'price': 1500, 'category': 'SNACK', 'description': 'Classic triple-decker sandwich with chicken, egg, and cheese.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1528735602780-2552fd46c7af?auto=format&fit=crop&w=800&q=80'},
            {'name': 'Chicken Burger', 'price': 1800, 'category': 'SNACK', 'description': 'Juicy chicken patty with lettuce, tomato, and secret sauce.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1550547660-d9450f859349?auto=format&fit=crop&w=800&q=80'},
            {'name': 'Garlic Naan', 'price': 300, 'category': 'SNACK', 'description': 'Freshly baked tandoori bread brushed with aromatic garlic butter.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1585937421612-70a008356fbe?auto=format&fit=crop&w=800&q=80'},
            {'name': 'French Fries', 'price': 600, 'category': 'SNACK', 'description': 'Classic golden crispy potato fries with sea salt.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1573080496219-bb080dd4f877?auto=format&fit=crop&w=800&q=80'},
            {'name': 'Onion Rings', 'price': 700, 'category': 'SNACK', 'description': 'Crispy beer-battered onion rings with a spicy dip.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1639024471283-035188835118?auto=format&fit=crop&w=800&q=80'},
            {'name': 'Mozzarella Sticks', 'price': 900, 'category': 'SNACK', 'description': 'Stringy melted mozzarella coated in seasoned breadcrumbs.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1531749956467-ca0acc784407?auto=format&fit=crop&w=800&q=80'},
            {'name': 'Chicken Wings', 'price': 1400, 'category': 'SNACK', 'description': 'Spicy buffalo chicken wings served with ranch dressing.', 'is_available': True, 'image_url': 'https://images.unsplash.com/photo-1567620832903-9fc6debc209f?auto=format&fit=crop&w=800&q=80'},
        ]

        for item_data in food_data:
            item, created = FoodItem.objects.update_or_create(
                name=item_data['name'],
                defaults=item_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created food: {item.name}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Updated food: {item.name}'))
