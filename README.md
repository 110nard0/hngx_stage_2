# REST API with Basic CRUD Operations

This is a REST API capable of basic CRUD operations, built with Flask 2.3 and MongoDB 6.0.  
It dynamically handles request parameters, in order to perform create, read, update, and delete (CRUD) operations on a "person" resource. 

## Table of Contents
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Error Handling](#error-handling)
- [Testing](#testing)
- [UML Diagram](#uml-diagram)
- [License](#license)

## Installation
- You must have Python and pip package manager installed on your operating system.
- Follow the steps in the official Python [venv docs](https://docs.python.org/3/library/venv.html) to create a virtual environment (OPTIONAL).
- Create a new folder for the project.
- Clone this repository into the folder using the `git clone` command.
- Install the dependencies by running the following command in the terminal:

    > pip -r requirements.txt
 
## Configuration
- Configure the Flask app to serve the API on a different host and port by including the HOST_NAME and PORT variables in the run command. By default, the app is served on http://localhost:5000.
- You can configure the Flask app to use a different database by specifying the MONGODB_URI connection string while starting the server. The database defaults to http://localhost:27017/hngx without any authentication if no connection string is specified.

## Usage
- Run the following command to start the server:
  - Linux/MacOS: `[HOST_NAME] [PORT] [MONGODB_URI] python3 -m api.v2.app`
  - Windows: `[HOST_NAME] [PORT] [MONGODB_URI] python -m api.v2.app`
- Base URL: http://localhost:5000
- Detailed documentation of the API can be found here: [API Documentation](DOCUMENTATION.md)

### Create a new person

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

### Read details of all persons
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

### Read details of a person
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

### Update details of a person
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

### Delete a person
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
```

Note: Replace `{id}` and `{name}` in the URLs with the actual ID or name of the user you want to fetch, update, or delete.

## Error Handling
The API returns the following in case of an error:

```json
Status: Error Code
Content-Type: application/json

{
    "error": "Error Message"
}
```

Example:
```json
Status: 404
Content-Type: application/json

{
    "error": "Not found"
}
```

## Testing
The API was extensively tested using Postman. The full scripts are available [here](postman_tests.json).

### Test screenshots

![Tests_1](https://github.com/110nard0/hngx_stage_2/assets/76947677/22f206e3-6e58-430c-af2a-5264f54cd6ed)

![Tests_2](https://github.com/110nard0/hngx_stage_2/assets/76947677/fbf490da-58d1-4d13-beeb-0c9e836d0b85)


The collection of the test requests and with included scripts can be found here:

[![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/29693336-222f5790-c981-4f71-b8a4-952c25b0a7c8?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D29693336-222f5790-c981-4f71-b8a4-952c25b0a7c8%26entityType%3Dcollection%26workspaceId%3D9be6953d-8de3-4898-840e-123f4f0b5429)

## UML Diagram
![UML Diagram](https://github.com/110nard0/hngx_stage_2/assets/76947677/2a344c21-1de3-4cfd-9290-136b596e1cd3)

## License
The Flask framework is open-sourced software licensed under the [BSD3 license](https://opensource.org/license/bsd-3-clause/).

[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
