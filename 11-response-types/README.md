# Lesson 11 — Response Types

## Overview
By default, FastAPI automatically serializes Python dictionaries and Pydantic models into **JSON** (`application/json`).

However, real APIs frequently need to return non-JSON formats:
- Raw plain text logs
- HTML pages rendered on the fly
- Downloadable files (PDF documents, images, zip files)
- Exported spreadsheets (CSV) or XML feeds

This lesson demonstrates how to use FastAPI's specialized response classes as well as the generic `Response` class.

---

## Key Concepts & Code Breakdown (`main.py`)

- `from fastapi.responses import FileResponse, HTMLResponse, PlainTextResponse`  
  Imports dedicated response classes that automatically set the appropriate HTTP headers.

- **1. Plain Text (`PlainTextResponse`):**
  ```python
  @app.get("/text", response_class=PlainTextResponse)
  ```
  Returns raw unformatted text with `Content-Type: text/plain; charset=utf-8`.

- **2. HTML Pages (`HTMLResponse`):**
  ```python
  @app.get("/page", response_class=HTMLResponse)
  ```
  Returns HTML markup with `Content-Type: text/html`. Browsers will render it directly as a webpage.

- **3. File Downloads (`FileResponse`):**
  ```python
  report_path = Path(__file__).parent / "files" / "report.pdf"
  return FileResponse(report_path, filename="monthly_report.pdf")
  ```
  Streams a local file to the client. The `filename` parameter controls the default saved filename on the client's computer.

- **4. Generic `Response` (CSV & XML):**
  When a dedicated class doesn't exist, use `Response(content=..., media_type=..., headers=...)`:
  - `media_type="text/csv"` or `media_type="application/xml"`: Sets custom MIME types.
  - `headers={"Content-Disposition": "attachment; filename=data.csv"}`: Instructs browsers to download the file rather than displaying it raw.

---

## How to Run

From this directory (`11-response-types`), run:

```bash
uvicorn main:app --reload
```

---

## Testing the Endpoints

| URL Path | Response Type | Content-Type | What to Expect |
| :--- | :--- | :--- | :--- |
| `http://127.0.0.1:8000/text` | Plain Text | `text/plain` | Raw text message |
| `http://127.0.0.1:8000/page` | HTML | `text/html` | Formatted web page with heading |
| `http://127.0.0.1:8000/download-report` | File | `application/pdf` | PDF download / preview |
| `http://127.0.0.1:8000/export-csv` | CSV | `text/csv` | Browser downloads `data.csv` |
| `http://127.0.0.1:8000/xml-data` | XML | `application/xml` | Browser downloads `data.xml` |
