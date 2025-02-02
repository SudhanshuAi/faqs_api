# Multilingual FAQ System

A Django-based FAQ management system with multilingual support, featuring WYSIWYG editing, automatic translations, and efficient caching using Redis.

## Features

-   🌐 Multilingual FAQ management
-   ✍️ WYSIWYG editor support
-   🔄 Automatic translation using Google Translate
-   💾 Redis-based caching for improved performance
-   🚀 RESTful API with language selection
-   🎨 Comprehensive admin interface

## Prerequisites

-   Python 3.8+
-   Redis Server
-   pip (Python package manager)

## Installation

1.  **Clone the repository**

`git clone <repository-url> cd multilingual-faq-system`

2.  **Set up virtual environment**


`# Create virtual environment python -m venv venv   # Activate virtual environment # On Windows: venv\Scripts\activate # On macOS/Linux: source venv/bin/activate`

3.  **Install dependencies**


`pip install -r requirements.txt`

4.  **Environment Setup**


`# Create .env file cp .env.example .env   # Update .env with your settings # Example .env content: SECRET_KEY=your-secret-key-here DEBUG=False ALLOWED_HOSTS=localhost,127.0.0.1 REDIS_URL=redis://localhost:6379/0`

5.  **Database Setup**


`python manage.py migrate`

6.  **Create Superuser**


`python manage.py createsuperuser # Follow the prompts to create admin account`

## Running the Project

1.  **Start Redis Server**


`# On Windows: redis-server.exe   # On macOS/Linux: redis-server`

2.  **Run Development Server**


`python manage.py runserver`

The application will be available at:

-   Admin Interface: [http://localhost:8000/admin/](http://localhost:8000/admin/)
-   API Endpoint: [http://localhost:8000/api/faqs/](http://localhost:8000/api/faqs/)
