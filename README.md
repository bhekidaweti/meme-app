Meme Generator Web App Documentation
Overview
Welcome to the Meme Generator Web App documentation! This web application is built using Flask, a web framework for Python, and allows users to generate random memes, view an archive of past memes. The app integrates with an external API to fetch random memes, and it uses a SQLite database to permanently store and display archived memes.

Table of Contents
Installation
Usage
Project Structure
Dependencies
Configuration
Database
Creating Migrations
Run the Application
Accessing the App
Contributing
License
Installation

To install the Meme Generator Web App, follow these steps:

Clone the repository to your local machine:



git clone https://github.com/bhekidaweti/meme.git
Navigate to the project directory:



cd meme
Install the required dependencies:



pip install -r requirements.txt
Usage
Once you have installed the application, follow these steps to run it:

Make sure you are in the project directory:



cd meme
Run the application:



python meme.py
Open your web browser and go to http://127.0.0.1:5000/ to access the home page.

Project Structure
The project structure is organized as follows:

meme.py: The main Flask application script.
templates/: Contains HTML templates for the home, archives, about pages, and the layout template.
migrations/: Stores database migration files.
meme.db: SQLite database file.
README.md: Documentation file.
requirements.txt: Lists the Python dependencies for the project.
Dependencies
The Meme Generator Web App relies on the following dependencies:

Flask: A web framework for Python.
Flask-SQLAlchemy: Integration of SQLAlchemy with Flask for database support.
Flask-Migrate: Extension for database migrations with Flask.
Requests: HTTP library for making API requests.
All dependencies are listed in the requirements.txt file.

Configuration
The Flask application is configured in the meme.py file. You can customize the following configurations:

SQLALCHEMY_DATABASE_URI: Database URI. The default is set to use SQLite.
SQLALCHEMY_TRACK_MODIFICATIONS: Set to False to suppress SQLAlchemy modification tracking.
Database
The application uses an SQLite database to store archived memes. The database schema is defined in the meme.py file in the ArchivedMeme class.

Creating Migrations
If you make changes to the database models, you need to create and apply migrations. Follow these steps:

Initialize migrations:





python meme.py
The app will be accessible at http://127.0.0.1:5000/.

Contributing
If you would like to contribute to the Meme Generator Web App, follow these steps:

Fork the repository on GitHub.
Create a new branch for your feature or bug fix.
Make your changes and submit a pull request.
License
The Meme Generator Web App is licensed under the MIT License.

Feel free to explore the app, generate memes, and contribute to its development! If you have any questions or encounter issues, please open an issue on the GitHub repository. Thank you for using and contributing to the Meme Generator Web App!