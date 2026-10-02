# Lesson 14 — Authentication Basics

## Overview
Not every route in an API should be public. Administrative actions, user profiles, and private records must be protected behind authentication.

In modern web development, authentication is commonly implemented using **Bearer Tokens** passed in the HTTP `Authorization` header (`Authorization: Bearer <token>`).

FastAPI has first-class security tools that integrate with OpenAPI, giving you automatic interactive login prompts in Swagger UI (`/docs`).

---

## Key Concepts & Code Breakdown (`main.py`)

- `from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials`  
  Imports FastAPI's built-in security scheme for Bearer token authorization.

- `security = HTTPBearer()`  
  Initializes the security scheme. It instructs FastAPI to inspect incoming requests for an `Authorization: Bearer <token>` header. It also automatically adds an **"Authorize 🔒"** button at the top of `/docs`!

- **Public Route (`/public`):**
  ```python
  @app.get("/public")
  def public_route():
      return {"message": "Anyone can access this"}
  ```
  Accessible to anyone without any headers or tokens.

- **Protected Route (`/protected`):**
  ```python
  @app.get("/protected")
  def protected_route(credentials: HTTPAuthorizationCredentials = Depends(security)):
  ```
  - `Depends(security)`: If a request arrives without an `Authorization` header, FastAPI immediately halts and returns an HTTP `403 Forbidden` error.
  - `credentials.scheme`: Contains the authentication scheme name (e.g. `"Bearer"`).
  - `credentials.credentials`: Contains the actual token string supplied by the user.

- **Token Validation:**
  ```python
  if credentials.credentials != "demo-token":
      raise HTTPException(status_code=401, detail="Invalid token")
  ```
  Validates the token against our secret (`"demo-token"`). In a production application, you would verify a signed JWT (JSON Web Token) or lookup a session token here.

---

## How to Run

From this directory (`14-authentication`), run:

```bash
uvicorn main:app --reload
```

---

## Testing in Swagger Docs (`/docs`)

1. Open `http://127.0.0.1:8000/docs`.
2. Try running `GET /protected` without authenticating:
   - You receive an HTTP 403 Forbidden response.
3. Click the green **Authorize 🔒** button at the top right of the Swagger UI page.
4. In the `Value` box, type `demo-token` and click **Authorize**, then click **Close**.
5. Run `GET /protected` again:
   - It succeeds with `{"message": "Protected endpoint"}`!
6. Try entering an incorrect token (e.g. `wrong-token`) to see the `401 Invalid token` error.
