ConcordiaBook Textbook Listing Module
This Django project is a module for the ConcordiaBook application. It allows students to view available textbooks for trade, filtered by course code.

Features
Textbook Listing: Displays textbooks for a specified course code.
Availability Filtering: Only shows textbooks marked as available.
User-Friendly Template: Shows textbook details or a "no results" message if none are found.
Setup
Clone the Repository:
git clone https://github.com/rizalmahmud/concordiabook.git
cd concordiabook
Create and Activate a Virtual Environment:

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install Dependencies:

bash
pip install -r requirements.txt
Apply Migrations:

bash
python manage.py makemigrations
python manage.py migrate
Run the Server:

bash
python manage.py runserver

Admin Access
To add textbook entries via the Django admin:

bash
python manage.py createsuperuser
Access the admin at http://127.0.0.1:8000/admin/.
