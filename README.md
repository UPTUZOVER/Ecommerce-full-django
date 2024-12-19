Online Magazin - E-commerce Platform
Welcome to Katta Online Magazin, a modern and scalable e-commerce platform designed for large online stores. This platform enables businesses to sell products, manage inventory, offer discounts, and interact with customers seamlessly. Built using Django and Parler for multi-language support, this platform allows store owners to easily manage their online store and engage customers.

Features
Product Management: Manage products with multi-language support (titles, descriptions).
Categories: Organize products into categories for better user experience.
Product Images: Upload and display multiple images for each product.
Stock Management: Keep track of product stock and show availability.
Discount System: Offer discounts and set "true price" based on discounts.
Multiple Languages: Full support for translations of product names and descriptions.
Customizable: Easily extendable for custom functionality.
Responsive Design: Fully responsive interface for mobile and desktop users.
Requirements
Before you start, make sure you have the following installed:

Python 3.8 or higher
Django 3.x or higher
Django Parler for multi-language support
MySQL, PostgreSQL, or SQLite for the database (SQLite is the default for development)
Pillow (for image processing)
You can install the required Python libraries using the following:

bash
Копировать код
pip install -r requirements.txt
Setup Instructions
1. Clone the Repository
Clone the repository to your local machine:

bash
Копировать код
git clone https://github.com/yourusername/katta-online-magazin.git
cd katta-online-magazin
2. Create a Virtual Environment
Create a virtual environment to isolate the dependencies:

bash
Копировать код
python -m venv venv
Activate the virtual environment:

Windows:
bash
Копировать код
venv\Scripts\activate
macOS/Linux:
bash
Копировать код
source venv/bin/activate
3. Install Required Packages
Install the required Python libraries using pip:

bash
Копировать код
pip install -r requirements.txt
4. Database Setup
Create a database in your chosen database management system (MySQL, PostgreSQL, or SQLite).

For SQLite (default):

SQLite does not require any additional setup. It will create the database file automatically.
For MySQL or PostgreSQL:

Update the DATABASES setting in settings.py to reflect your database credentials.
5. Run Migrations
After setting up your database, run the following command to apply migrations:

bash
Копировать код
python manage.py migrate
6. Create a Superuser
To access the admin panel, create a superuser account:

bash
Копировать код
python manage.py createsuperuser
Follow the prompts to create your admin account.

7. Run the Development Server
You can now run the development server to test the application:

bash
Копировать код
python manage.py runserver
Visit http://127.0.0.1:8000 in your browser to see the platform in action.

Project Structure
Here’s a brief overview of the project structure:

bash
Копировать код
katta-online-magazin/
│
├── categories/            # Category management module
├── products/              # Product management module
│   ├── migrations/
│   └── models.py          # Product model (includes translations, images, etc.)
├── users/                 # User management and authentication
├── templates/             # HTML templates for the front-end
│   └── base.html
├── static/                # Static files (CSS, JS, images)
├── manage.py              # Django management script
├── settings.py            # Project settings
├── requirements.txt       # Python dependencies
└── README.md              # Project README (you are here!)
Key Models
1. Product
The Product model represents products in the store. Each product has:

A name (title), description (description), price (price), and stock count (count).
Multiple images (such as image_main, img1, img2, etc.).
A discount system that calculates the "true price" (true_price) based on the discount percentage.
Example:

python
Копировать код
class Product(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=200, unique=True, verbose_name=_("Product Name")),
        description=models.TextField(blank=True, verbose_name=_("Product Description")),
    )
    categories = models.ForeignKey(Category, verbose_name=_("Category"), on_delete=models.CASCADE)
    image_main = models.ImageField(upload_to='images/', verbose_name=_("Main Image"))
    price = models.DecimalField(verbose_name=_("Product Price"), max_digits=10, decimal_places=2)
    count = models.IntegerField(verbose_name=_("Stock Quantity"))
    discount = models.IntegerField(verbose_name=_("Discount Percentage"), null=True, blank=True)
    true_price = models.DecimalField(verbose_name=_("Discounted Price"), max_digits=10, decimal_places=2, blank=True, null=True)
    # Other fields
2. Category
The Category model is used to organize products into categories.

Admin Panel
You can manage products, categories, users, and more using Django's built-in admin panel.

To access the admin panel:

Start the Django development server using python manage.py runserver.
Visit http://127.0.0.1:8000/admin in your browser.
Log in using the superuser credentials you created earlier.
Customization
The platform is highly customizable. You can:

Add new fields to models (e.g., product ratings, reviews, etc.).
Extend views to support new features (e.g., adding a search bar, sorting, and filtering).
Modify templates to match your store's branding and design.
Add new features like shopping carts, checkout, payment processing, and more.
Deployment
1. Production Setup
For production, you will need to set up a production-ready server, such as:

Nginx or Apache as the web server.
Gunicorn or uWSGI as the application server.
A production database such as MySQL or PostgreSQL.
Make sure to configure static files, media files, and environment variables for security.

2. Cloud Deployment
You can deploy this application to cloud platforms such as:

Heroku
AWS EC2
DigitalOcean
Google Cloud Platform
Ensure you follow best practices for scaling and security.

License
This project is licensed under the MIT License.

Contributing
If you'd like to contribute to the development of this platform, feel free to fork the repository and submit a pull request. Ensure your contributions adhere to the project's coding standards and guidelines.

Contact
For any questions or issues, please contact us at:

Email: support@kattaonlinemagazin.com
Website: www.kattaonlinemagazin.com
Acknowledgments
This platform uses Django for web development.
Parler library is used for multilingual support.
Pillow is used for image handling.
