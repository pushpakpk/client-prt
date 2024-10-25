# client-project


# Django REST API for Client-Project Management

## 1. How to Run the Machine

### Prerequisites
- Python 3.x
- PostgreSQL (Ensure PostgreSQL is running)
- Git

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd myproject
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # For Windows: .\env\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure PostgreSQL database** in `settings.py` (change `NAME`, `USER`, `PASSWORD`, `HOST` to match your local setup):
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'myproject',
           'USER': 'myuser',
           'PASSWORD': 'mypassword',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

5. **Run migrations** to create the necessary database tables:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create a superuser** to access Django's admin panel:
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the server**:
   ```bash
   python manage.py runserver
   ```

### Access the APIs
- Base URL: `http://localhost:8000/api/`
- **Admin panel**: `http://localhost:8000/admin/`

## 2. Database Design

The system consists of three entities: `User`, `Client`, and `Project`.

### Models

1. **Client**:
    - `client_name`: Name of the client
    - `created_at`: Timestamp when the client was created
    - `created_by`: Foreign key to `User`, referring to who created the client

2. **Project**:
    - `project_name`: Name of the project
    - `client`: Foreign key to `Client`
    - `users`: Many-to-Many relationship with `User`
    - `created_at`: Timestamp when the project was created
    - `created_by`: Foreign key to `User`, referring to who created the project

### Relationships

- A `Client` can have multiple `Projects`.
- A `Project` can be assigned to multiple `Users` (Many-to-Many relationship).

### Database Schema

- **Client Table**:
    - `id` (Primary Key)
    - `client_name`
    - `created_at`
    - `created_by_id` (Foreign Key to `User`)

- **Project Table**:
    - `id` (Primary Key)
    - `project_name`
    - `client_id` (Foreign Key to `Client`)
    - `created_at`
    - `created_by_id` (Foreign Key to `User`)

- **User Table** (Django’s default User model):
    - `id` (Primary Key)
    - `username`
    - `password`

- **Project Users Table** (Many-to-Many relation):
    - `project_id` (Foreign Key to `Project`)
    - `user_id` (Foreign Key to `User`)

## 3. API Endpoints and How to Run the Code

### API Endpoints

#### 1. List all clients
   - **Endpoint**: `GET /api/clients/`
   - **Description**: Returns a list of all clients.
   
#### 2. Create a new client
   - **Endpoint**: `POST /api/clients/`
   - **Request Body**:
     ```json
     {
       "client_name": "Company A"
     }
     ```

#### 3. Retrieve a specific client by ID (with projects)
   - **Endpoint**: `GET /api/clients/:id/`
   
#### 4. Update a client's information
   - **Endpoint**: `PUT/PATCH /api/clients/:id/`
   - **Request Body**:
     ```json
     {
       "client_name": "Updated Company Name"
     }
     ```
     
#### 5. Delete a client
   - **Endpoint**: `DELETE /api/clients/:id/`
   - **Description**: Deletes a client and returns a 204 No Content response.

#### 6. Create a new project for a client
   - **Endpoint**: `POST /api/clients/:client_id/projects/`
   - **Request Body**:
     ```json
     {
       "project_name": "Project A",
       "users": [1, 2]  # User IDs
     }
     ```

#### 7. List all projects assigned to the logged-in user
   - **Endpoint**: `GET /api/projects/`
   - **Description**: Returns all projects assigned to the authenticated user.

### Testing the APIs
Use Postman or curl to test the API endpoints.

- **Authorization**: Use Django’s token-based or session-based authentication.
- **Headers**: Set `Content-Type: application/json` when making POST/PUT requests.

### Notes
- Ensure PostgreSQL is running before starting the Django server.
- Access the Django admin panel at `http://localhost:8000/admin/` to manage users.

## 4. Deployment
To deploy, follow these steps on your production server:
- Set `DEBUG=False` in `settings.py`
- Set up PostgreSQL and configure the environment variables.
- Use `gunicorn` and `nginx` for serving the Django application.
