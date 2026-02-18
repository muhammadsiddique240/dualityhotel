# DualityHotel - Luxury Hotel Booking Platform

DualityHotel is a premium hotel booking web application built with Django and Bootstrap 5. It features a luxury dark/gold aesthetic, smooth animations, and a complete booking system.

## Features
- **Luxury UI/UX**: Custom design with Hero slider, AOS animations, and responsive layout.
- **Room Management**: View rooms with details, pricing, and images.
- **Booking System**: Users can book rooms with date validation.
- **Contact Form**: Inquiries are saved to the database.
- **Admin Panel**: Manage rooms, bookings, and messages.

## Tech Stack
- **Backend**: Python, Django
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript (AOS)
- **Database**: SQLite (Dev)

## Setup Instructions

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd dualityhotel
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install django pillow requests
    ```

4.  **Run migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Populate the database with dummy data:**
    ```bash
    python manage.py populate_rooms
    ```

6.  **Create a superuser (for Admin panel):**
    ```bash
    python manage.py createsuperuser
    ```

7.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

8.  **Access the application:**
    - Website: http://127.0.0.1:8000/
    - Admin Panel: http://127.0.0.1:8000/admin/
