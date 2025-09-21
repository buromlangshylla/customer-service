# Customer Service API

A Django REST Framework project for managing customers, addresses, KYC documents, and payment methods.

## Setup Instructions

1. **Clone the repository**
   ```sh
   git clone https://github.com/buromlangshylla/customer-service.git
   cd customer-service
   ```

2. **Create and activate a virtual environment**
   ```sh
   python -m venv customer-venv
   customer-venv\Scripts\activate
   ```

3. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   - Create a `.env` file in the root directory:
     ```env
     SECRET_KEY=your-secret-key
     DEBUG=True
     DATABASE_NAME=customer_service.sqlite3
     JWT_SECRET_KEY=your-jwt-secret-key
     ALLOWED_HOSTS=127.0.0.1,localhost
     ```

5. **Apply migrations**
   ```sh
   python manage.py migrate
   ```

6. **Run the development server**
   ```sh
   python manage.py runserver
   ```

## API Endpoints

All POST requests require JWT authentication.

| Resource         | List/Filter/Search                | Retrieve (with nested data)         |
|------------------|-----------------------------------|-------------------------------------|
| Customers        | `/customers/`                     | `/customers/{id}/`                  |
| Addresses        | `/addresses/`                     | `/addresses/{id}/`                  |
| KYC Documents    | `/kyc-documents/`                 | `/kyc-documents/{id}/`              |
| Payment Methods  | `/payment-methods/`               | `/payment-methods/{id}/`            |

### Example: Create Customer

```http
POST /customers/
Content-Type: application/json
Authorization: Bearer <your-jwt-token>

{
  "first_name": "John",
  "last_name": "Doe",
  "dob": "1990-01-01",
  "gender": "male",
  "primary_email": "john.doe@example.com",
  "primary_phone": "1234567890",
  "preferred_contact_method": "email",
  "occupation": "Engineer",
  "income_bracket": "50k-100k",
  "risk_score": 75.5,
  "kyc_status": "pending"
}
```

### Example: Retrieve Customer (with nested data)

```http
GET /customers/{id}/
Authorization: Bearer <your-jwt-token>
```
Response:
```json
{
  "id": "...",
  "first_name": "John",
  "last_name": "Doe",
  ...,
  "addresses": [ ... ],
  "kyc_documents": [ ... ],
  "payment_methods": [ ... ]
}
```

### Filtering & Searching
- Filter customers by `kyc_status`, `income_bracket`, `risk_score`:
  `/customers/?kyc_status=verified&income_bracket=50k-100k`
- Search by email:
  `/customers/?search=john.doe@example.com`

## API Documentation (Swagger)

Interactive API documentation is available at:

- [Swagger UI](http://127.0.0.1:8000/api/docs/)
- [OpenAPI Schema](http://127.0.0.1:8000/api/schema/)
- [Redoc](http://127.0.0.1:8000/api/redoc/)

Use these endpoints to explore and test the API directly from your browser.

## Postman Collection

The Postman collection for this API is included in the repository as `insurance.postman_collection.json`.

---