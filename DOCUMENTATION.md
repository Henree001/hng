Documentation of the REST API Project that handles CRUD operations
This documentation provides detailed information on the REST API built with Flask, SQLAlchemy and other dependencies. It covers the standard format for requests and responses, sample API usage, known limitations, and setup/deployment instructions.

Table of Contents
Prereqisites
Setup and Deployment
Standard Request and Response Format
Sample API Usage
Known Limitations
Prerequisites
Before you begin, ensure you have the following prerequisites installed in your system:

Python (3.8 or higher)
pip (Python package manager)
pipenv
git bash terminal (For windows)
Setup and Deployment
To set up and deploy this API locally or on a server, follow these steps:

Clone the repository: git clone https://github.com/Henree001/hng

Enter the cloned directory: cd hng

Create a virtual environment: pipenv shell

Run the API locally: python api_endpoint/myapp.py

The API will be accessible at http://localhost:5000.

For production deployment, consider using a production-ready web server (e.g., Gunicorn) and configuring a proper database server.

Standard Request and Response Format

### GET /api/<user_id:string>

**Request to get a user:**

- No request body required.

**Response (200 OK):**

````json
{
    "id": 1,
    "name": "John Doe"
}

### POST /api
**Request to create a new user:**
- Request body required.
{
    "name": "New User"
}

**Response (200 ok):**
```json
{
    "id": 3,
    "name": "New User"
}

### PUT /api/<user_id:string>
**Request to update the records of an existing user:**
- Request body required.
{
    "name": "Updated User Name"
}

**Response (200 OK):**
```json
{
    "id": 1,
    "name": "Updated User Name"
}


### DELETE /users/<user_id:string>
**Request to delete a user:
- No request body required.

**Response (200 Ok):**
```json
{
    "Delete": "success"
}

## Sample API Usage


Retrieve a user (GET /api/<user_id:string>)
Request:
GET http://localhost:5000/api/1

Response (200 OK):
{
    "id": 1,
    "name": "John Doe"
}

Create a new user (POST /users)
Request:
POST http://localhost:5000/api
Content-Type: application/json
{
    "name": "New User"
}

Response (200 ok):
{
    "id": 3,
    "name": "New User"
}

Update a user by ID (PUT /users/<user_id:string>)
Request:
PUT http://localhost:5000/api/1
Content-Type: application/json
{
    "name": "Updated User Name"
}

Response (200 OK):
{
    "id": 1,
    "name": "Updated User Name"
}


Delete a user by ID (DELETE /users/<user_id:string>)
Request:
DELETE http://localhost:5000/api/1
Content-Type: application/json

Response (200 OK):
{
    "Delete": "Success"
}

## Known Limitations
- This API does not include authentication or authorization mechanisms. It assumes open access.
- Error handling for invalid requests is minimal in this sample.
- The database connection is not configured for production use. It uses a SQLite database by default.
````
