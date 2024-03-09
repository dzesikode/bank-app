# Bank App

Bank App is a proof-of-concept, single-page application that generates banking product recommendations to registered users based on answers to a questionnaire.

## Features
* User authentication
* Tokens
* User permissions and roles
* Data persistence
* User interface
* RESTful APIs

## Tech
* Python
* Django
* PostgreSQL
* TypeScript
* Angular
* Docker

## Setup
1. Get the code
   ```sh
   git clone https://github.com/dzesikode/bank-app
   ```
2. Ensure you're in the root directory (bank-app)
3. Copy the example env file
   ```sh
   cp ./back-end/config/.env.example ./back-end/config/.env
   ```
4. Start the app
   ```sh
   docker-compose up --build
   ```
5. Navigate to http://localhost:4200 in your browser

## Future features
* Update project and libraries to newest versions
* Polishing of UI


Method | Path | Description | User Role
--- | --- | --- | ---
POST | /api/login | Authenticate user | None (Anonymous)
POST | /api/register | Create user | None (Anonymous)
GET | /api/products/search?age={age}&income={income}&student={student} | Get product(s) by criteria | User
GET | /api/manage/products | Get all products | Admin, Product Manager
GET | /api/manage/products/{productName} | Get specific product | Admin, Product Manager
POST | /api/manage/products/add | Create product | Admin, Product Manager
PUT | /api/manage/products/{productName} | Update product | Admin, Product Manager
DELETE | /api/manage/products/{productName} | Delete product | Admin, Product Manager
GET | /api/manage/users | Get all users | Admin
GET | /api/manage/users/{id} | Get specific user | Admin
PUT | /api/manage/users/{id} | Update user | Admin
DELETE | /api/manage/users/{id} | Delete user | Admin

