# API Documentation

This documentation provides an overview of the endpoints available for interfacing with the "Person" resource and their standard request and response formats.
It also includes sample usage, known limitations, and instructions for setting up and deploying the API.

## Default URL

The default/base URL for all endpoints is `http://localhost:8000`.

## Endpoints

### Create a new person.

**Request:**
  > POST /api

```http
POST /api
Content-Type: application/json

{
  "name": "chika"
}
```

**Response:**

```json
Status: 200 OK
Content-Type: application/json

{
  "id": "65035f6372f25cd7f0e3e7bf",
  "name": "chika"
}
```

### Read details of all persons.
  > GET /api

**Request:**

```http
GET /api
```

**Response:**

```json
Status: 200 OK
Content-Type: application/json

[
  {
    "id": "65035f6372f25cd7f0e3e7bf",
    "name": "chika"
  }
]
```

### Read details of a person.
  > GET /api/{id}

  > GET /api/{name}

**Request:**

```http
GET /api/65035f6372f25cd7f0e3e7bf
GET /api/chika
```

**Response:**

```json
Status: 200 OK
Content-Type: application/json

{
  "id": "65035f6372f25cd7f0e3e7bf",
  "name": "chika"
}
```

### Update details of a person.
  > PUT /api/{id}

  > PUT /api/{name}

**Request:**

```http
PUT /api/65035f6372f25cd7f0e3e7bf
PUT /api/chika
Content-Type: application/json

{
  "name": "bolu",
}
```

**Response:**

```json
Status: 200 OK
Content-Type: application/json

{
  "id": "65035f6372f25cd7f0e3e7bf",
  "name": "bolu"
}
```

### Delete a person.
  > DELETE /api/{id}

  > DELETE /api/{name}

**Request:**

```http
DELETE /api/65035f6372f25cd7f0e3e7bf
DELETE /api/bolu
```

**Response:**

```json
Status: 204 No Content

{}
```

Note: Replace `{id}` and `{name}` in the URLs with the actual ID or name of the user you want to fetch, update, or delete.


## Sample Usage

Here are some examples of how you can use the API:

1. Adding a new person:
   - Send a `POST` request to `/api` with the person's name in the request body.
   - The API will respond with the person's details, including the assigned ID as a JSON body.

2. Reading details of all persons:
   - Send a `GET` request to `/api` or `/api`.
   - The API will respond with the details of all persons in the database as a JSON list.

3. Reading details of a person:
   - Send a `GET` request to `/api/{id}` or `/api/{name}` with the person's ID or name in the URL.
   - The API will respond with the person's details as a JSON body.
   - 
4. Updating details of a person:
   - Send a `PUT` request to `/api/{id}` or `/api/{name}` with the person's ID or name in the URL and the updated name in the request body.
   - The API will respond with the updated person's details as a JSON body.

5. Deleting a person:
   - Send a `DELETE` request to `/api/{id}` or `/api/{name}` with the person's ID or name in the URL.
   - The API will respond with no content if the deletion is successful.

## Limitations and Assumptions

Please note the following limitations and assumptions of the API:

- The API assumes that the ID provided in the URL for fetching, updating, or deleting a person exists in the database. If the ID is invalid, an error will be returned with a 404 HTTP status code.
- The API does not support bulk operations for creating, updating, or deleting multiple persons at once.
- The API does not implement any authentication or authorization mechanisms. It assumes unrestricted access to the endpoints.
- However, the API is flexible enough to handle dynamic input and will perform validation checks on the path parameters and request body field to ensure they are all unique string types before creating or updating the indicated person resource.
  In the event of a duplication or validation error, the server will respond with an error message and a 400 HTTP status code.

## Setup and Deployment

To set up and deploy the API locally or on a server, follow these instructions:

1. Create a new folder for the project.
2. Clone the project repository from GitHub.
3. Install the required dependencies from the requirements.txt file using pip.
4. Configure the database connection before runtime or ina .env file.
5. Obtain your MongoDB connection string or skip if you do not have a configured database.
6. Start the Flask server.
7. The API will be accessible at `http://localhost:5000` or the specified URL.
