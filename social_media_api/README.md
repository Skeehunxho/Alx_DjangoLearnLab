📱 Social Media API

A RESTful API built with Django + Django REST Framework, providing user authentication, posts, and comments functionality for a simple social media platform.

🚀 Features

User Authentication

Register, login, and manage profiles

Token-based authentication (rest_framework.authtoken)

Posts

Create, read, update, and delete posts

Search and filter posts by title, content, or author

Pagination for large datasets

Comments

Add comments to posts

CRUD operations with permissions

Nested endpoint for fetching comments of a post

Permissions

Only owners can update/delete their posts and comments

Everyone can view public posts and comments

🛠️ Tech Stack

Backend Framework: Django, Django REST Framework

Authentication: Token Authentication

Database: SQLite (default, can be swapped for PostgreSQL/MySQL)

Filtering & Search: django-filter

⚙️ Installation

Clone the repository

git clone <your_repo_url>
cd social_media_api


Create a virtual environment & install dependencies

python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
pip install -r requirements.txt


If requirements.txt is not yet created, install manually:

pip install django djangorestframework djangorestframework-authtoken django-filter pillow


Apply migrations

python manage.py makemigrations
python manage.py migrate


Create superuser (for Django admin)

python manage.py createsuperuser


Run server

python manage.py runserver

🔑 Authentication

We use Token Authentication.

Register → returns a token

Login → returns a token

Use token in all authenticated requests:

Authorization: Token <your_token>

📖 API Endpoints
Accounts (/api/accounts/)
Method	Endpoint	Description	Auth Required
POST	/register/	Register new user + token	❌
POST	/login/	Login user + token	❌
GET	/profile/	Get current user profile	✅
PATCH	/profile/	Update profile info	✅
Posts (/api/posts/)
Method	Endpoint	Description	Auth Required
GET	/	List posts (paginated)	❌
POST	/	Create a new post	✅
GET	/{id}/	Retrieve post details (incl. comments)	❌
PATCH	/{id}/	Update post (author only)	✅
DELETE	/{id}/	Delete post (author only)	✅
GET	/{id}/comments/	List comments for a post	❌

🔎 Filtering & search:

/api/posts/?search=hello

/api/posts/?author=1

/api/posts/?ordering=created_at

Comments (/api/comments/)
Method	Endpoint	Description	Auth Required
GET	/	List all comments (filterable)	❌
POST	/	Add a comment	✅
GET	/{id}/	Retrieve a comment	❌
PATCH	/{id}/	Update comment (author only)	✅
DELETE	/{id}/	Delete comment (author only)	✅

🔎 Filtering:

/api/comments/?post=1

/api/comments/?author=2

🧪 Testing

Run Django tests:

python manage.py test


Or test manually with Postman / cURL by sending requests to the endpoints listed above.

📂 Project Structure
social_media_api/
│── accounts/        # User authentication app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
│── posts/           # Posts & comments app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── permissions.py
│   └── urls.py
│
│── social_media_api/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
└── manage.py

✅ Roadmap

 User authentication (register/login/profile)

 CRUD for posts

 CRUD for comments

 Pagination, filtering, search

 Like/Unlike functionality

 Follower/Following system integration

 Real-time notifications (via Django Channels)

💡 Tip: Start testing endpoints as soon as migrations are done to make sure everything works.
### 👥 Follow / Unfollow Users
- **POST** `/api/accounts/users/<id>/follow/` → Follow a user
- **POST** `/api/accounts/users/<id>/unfollow/` → Unfollow a user

### 📰 Feed
- **GET** `/api/posts/feed/`  
Returns posts from users that the authenticated user follows, ordered by most recent.
