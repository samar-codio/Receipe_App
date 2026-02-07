🍳 Recipe Sharing Platform

A full-stack Django web app to create, manage, and discover recipes. Built with clean MVC architecture and user authentication.

✨ Features

User Authentication: Register, login, and manage sessions securely

Recipe Management: Create, update, delete, and view recipes with images

Search: Real-time, case-insensitive recipe search

User-Recipe Relation: Recipes are linked to their owners

🛠️ Tech Stack

Backend: Django 4.2

Database: SQLite3

Frontend: Bootstrap 5

File Storage: Django ImageField for images

📂 Project Structure

vege/ – Project settings

home/ – Main app (models, views, templates)

media/ – Uploaded images

public/ – Static files

manage.py – Django management script

🚀 Getting Started

Clone the repo & navigate to project

Activate virtual environment

Install dependencies (django, pillow)

Run migrations

Start the development server

Open in browser:

register → Create account

receipe/ → Dashboard

🔐 Security

CSRF protection

Password-based authentication

Server-side input validation

Recipe ownership verification

🔮 Future Enhancements

Recipe ratings & comments

Categories & tags

Social features (likes, follows)

Advanced search filters

Mobile API integration

Email notifications
