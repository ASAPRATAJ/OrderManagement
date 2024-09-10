# READ.ME FILE

## ENDPOINTS:

### Create User:
- **Method:** POST
- **URL:** http://127.0.0.1:8000/api/users/create/
- **Example payload:**
  ```json
  {
    "email": "exampleuser@example.com",
    "company_name": "EXAMPLE",
    "password": "examplepassword123"
  }

### Login User:
- **Method:** POST
- **URL:** http://127.0.0.1:8000/api/users/token/create/
- **Example payload:**
  ```json
  {
    "email": "exampleuser@example.com",
    "password": "examplepassword123"
  }

### Create Order:
- **Method:** POST
- **URL:** http://127.0.0.1:8000/api/orders/create/
- **Permissions:** IsAuthenticated
- **Example payload:**
  ```json
  {
    "products": [
        {
            "product_id": 1,
            "quantity": 5
        },
        {
            "product_id": 2,
            "quantity": 4
        }
    ]
  }

### List of User Orders:
- **Method:** GET
- **URL:** http://127.0.0.1:8000/api/users/orders/
- **Permissions:** IsAuthenticated


### Create Product:
- **Method:** POST
- **URL:** http://127.0.0.1:8000/api/products/create/
- **Permissions:** IsAuthenticated, IsAdminUser (is_staff)
- **Example payload:**
  ```json
  {
    "title": "Example",
    "description": "Example description",
    "price": "30"
  }


### List of Products:
- **Method:** GET
- **URL:** http://127.0.0.1:8000/api/products/
- **Permissions:** IsAuthenticated

### List of created Users:
- **Method:** GET
- **URL:** http://127.0.0.1:8000/api/users/
- **Permissions:** IsAuthenticated, IsAdminUser (is_staff)


