# Lesson 15 — CORS (Cross-Origin Resource Sharing)

## Overview
When a web browser loads a frontend webpage from one origin (for example `http://localhost:3000`) and JavaScript on that page attempts to fetch data from a backend on another origin (such as `http://localhost:8000`), the browser enforces a security mechanism called the **Same-Origin Policy**.

By default, the browser **blocks** the request unless the backend explicitly declares via HTTP headers that the frontend is permitted. This mechanism is called **CORS (Cross-Origin Resource Sharing)**.

---

## What Counts as a Different Origin?
Two URLs have different origins if any of these three differ:
1. **Protocol:** (`http://` vs `https://`)
2. **Domain/Host:** (`example.com` vs `api.example.com` or `localhost` vs `127.0.0.1`)
3. **Port:** (`:3000` vs `:8000`)

---

## Key Concepts & Code Breakdown (`main.py`)

- `from fastapi.middleware.cors import CORSMiddleware`  
  FastAPI's built-in middleware for attaching CORS response headers (`Access-Control-Allow-Origin`, etc.).

- `app.add_middleware(CORSMiddleware, ...)`:
  - `allow_origins=["http://localhost:3000"]`:  
    Whitelists requests coming from a frontend running on port `3000`. Any request from other origins will be blocked by the browser.
  - `allow_credentials=True`:  
    Allows the browser to send cookies, authorization headers, or TLS client certificates across origins.
  - `allow_methods=["*"]`:  
    Allows all standard HTTP methods (`GET`, `POST`, `PUT`, `DELETE`, etc.).
  - `allow_headers=["*"]`:  
    Allows all custom request headers (such as `Authorization` or `Content-Type`).

---

## Hands-On Demonstration

To see CORS in action, we run two separate local servers:

### Step 1: Start the FastAPI Backend (Port 8000)
In your terminal, navigate to `15-cors` and run:

```bash
uvicorn main:app --reload --port 8000
```

### Step 2: Serve the Frontend (Port 3000)
Open a second terminal window in the same `15-cors` directory and start Python's static file server:

```bash
python -m http.server 3000
```

### Step 3: Test the Connection
1. Open your browser and go to `http://localhost:3000`.
2. Click the **"Get Message"** button.
3. Because `http://localhost:3000` is included in `allow_origins`, the request succeeds and displays:
   `"Hello from FastAPI"`.
4. *(Optional experiment)*: If you remove `"http://localhost:3000"` from `allow_origins` in `main.py` and refresh the page, clicking the button will fail with a red CORS error in your browser's Developer Tools Console!
