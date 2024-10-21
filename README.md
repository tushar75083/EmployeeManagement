# Django REST API CRUD Project
This project demonstrates a CRUD (Create, Read, Update, Delete) application using Django REST framework. It utilizes class-based views (APIView) along with model serializers to perform various CRUD operations on employee records. The project is built with the following key features:

## Features
<b>CRUD Operations:</b> Supports GET, POST, PUT, PATCH, and DELETE methods for handling employee records.<br>
<b>Class-Based Views (APIView):</b>  Uses Django REST framework's APIView for defining CRUD operations in a structured manner.<br>
<b>Model Serializer:</b>  Simplifies data serialization and deserialization processes with Django's model serializer.<br>
<b>Custom Error Messages:</b>  Returns custom error messages and appropriate HTTP status codes in the API responses.<br>
<b>Exception Handling:</b>  Uses try-except blocks to handle exceptions, such as when a specific employee is not found, ensuring the API responds with informative error messages.<br>
<b>Status in Response:</b>  Sends appropriate HTTP status codes (e.g., 200 OK, 404 Not Found, 400 Bad Request, etc.) along with the response to indicate the result of the API call.<br>

## API Endpoints
<b>1. GET </b> /employees/ - Retrieve a list of all employees.<br>
<b>2. GET </b> /employees/id/ - Retrieve a specific employee by ID.<br>
<b>3. POST </b> /employees/ - Create a new employee record.<br>
<b>4. PUT </b> /employees/id/ - Update an existing employee record.<br>
<b>5. PATCH  </b> /employees/id/ - Partially update fields in an employee record.<br>
<b>6. DELETE </b> /employees/id/ - Delete an employee record.<br>


## Error Handling
The application includes custom error handling to manage cases where an employee is not found, or when validation errors occur. For example:<br>
1. If an employee is not found during a GET or DELETE operation, the API returns a 404 Not Found status with a descriptive error message.<br>
2. Validation errors during POST or PUT operations return a 400 Bad Request status with details on the error.<br>


## Technologies Used
<b>Django -</b> Web framework for building the application.<br>
<b>Django REST Framework -</b> Toolkit for building Web APIs.<br>
<b>Python -</b> Programming language for implementing business logic.<br>
