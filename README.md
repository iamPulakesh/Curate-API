# Curate API 🎬📚🎶
An API that provides personalized recommendations for movies, books, and music.

------------------------------------------------------------------------

## Features

-   **Users CRUD** → Create, Read, Update, Delete users with their
    preferences.
-   **Items CRUD** → Manage movies, books, or music items.
-   **Recommendations** → Recommend items to users based on genres/their preferences.
-   **Redis Caching** → Store recommendations for faster responses.
-   **PostgreSQL Database** → Persist users and items.
-   **FastAPI** → Modern, async-ready web framework.
------------------------------------------------------------------------

## Tech Stack

-   **Backend Framework**: FastAPI (Python)
-   **Database**: PostgreSQL
-   **Machine Learning**: scikit-learn (cosine similarity)
-   **Cache**: Redis
------------------------------------------------------------------------

**Prerequisite**:PostgreSQL and Redis server installed and running on your system. 

------------------------------------------------------------------------

## Setup Instructions

### 1. Clone the Repository

``` bash
git clone https://github.com/your-username/curate-api.git
cd curate-api
```

### 2. Install Dependencies

``` bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project root:

``` ini
# PostgreSQL
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST= host_ip
DB_PORT=port_no (default: 5432)
DB_NAME=your_db_name

# Redis
REDIS_HOST=redis_host_ip
REDIS_PORT=redis_Port_no (default: 6379)

# FastAPI
APP_NAME=Curate API
APP_HOST=your_app_host
APP_PORT=your_app_port (default: 8000)
```

### 4. Run the App

``` bash
python -m app.main
```

------------------------------------------------------------------------

## API Endpoints

### Users

-   `POST /users/` → Create a new user
-   `GET /users/` → List all users
-   `GET /users/{id}` → Get user by ID
-   `PUT /users/{id}` → Update user
-   `DELETE /users/delete={id}` → Delete user

### Items

-   `POST /items/` → Create a new item
-   `GET /items/` → List all items
-   `GET /items/genre={genre}` → Get item by Genre
-   `PUT /items/{id}` → Update item
-   `DELETE /items/{id}` → Delete item

### Recommendations

-   `GET /recommendations/{user_id}` → Get recommendations for a user

------------------------------------------------------------------------

## Example Response

``` json
{
  "user_id": 1,
  "user_name": "Bob",
  "Preferences": ["Action", "Sci-Fi"] 
  "recommendations": [
    "Inception",
    "The Dark Knight",
    "Guardians of the Galaxy"
  ]
}
```
------------------------------------------------------------------------

## Contributing

Feel free to fork, create PRs, or raise issues to improve this project.

