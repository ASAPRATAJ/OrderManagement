# READ.ME FILE

**Admin user:**
- admin@example.com
- testpass123

**Normal user:**
- user@example.com
- testpass123

## ENDPOINTS:
## users/...
#### ***Create User:***
- **Method:** POST
- **URL:** http://127.0.0.1:8000/api/users/create/
- **Example payload:**
  ```json
  {
    "email": "exampleuser@example.com",
    "company_name": "EXAMPLE",
    "password": "examplepassword123"
  }

#### ***Login User:***
- **Method:** POST
- **URL:** http://127.0.0.1:8000/api/users/token/create/
- **Example payload:**
  ```json
  {
    "email": "exampleuser@example.com",
    "password": "examplepassword123"
  }

#### ***List User's orders:***
- **Method:** GET
- **URL:** http://127.0.0.1:8000/api/users/orders/
- **Permissions:** IsAuthenticated

#### ***List all users:***
- **Method:** GET
- **URL:** http://127.0.0.1:8000/api/users/
- **Permissions:** IsAuthenticated, IsAdminUser (is_staff)

## orders/...
#### Create Order:
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
#### List all Orders:
- **Method:** GET
- **URL:** http://127.0.0.1:8000/api/orders/
- **Permissions:** IsAuthenticated, IsAdminUser (is_staff)

## products/...

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

### Update/change Product:
- **Method:** POST
- **URL:** http://127.0.0.1:8000/api/products/<product-id>/update-image/
- **Permissions:** IsAuthenticated, IsAdminUser (is_staff)
- **Example payload:**
  ```json
  {
    "title": "Example",
    "description": "Example description",
    "price": "30",
    "image": "http://127.0.0.1:8000/media/products/images/PolishLodyLogo.jpg
  }



