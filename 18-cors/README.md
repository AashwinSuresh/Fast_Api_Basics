# Lesson 18 — CORS

Browsers apply security rules when a webpage makes a request to a different origin.

CORS (Cross-Origin Resource Sharing) tells the browser which origins are allowed to communicate with the API.

Here, FastAPI allows requests from http://localhost:3000. The frontend is served separately on that port, so the browser sees the request as cross-origin.

allow_methods and allow_headers control which HTTP methods and request headers are allowed.

To test the example, run the FastAPI server and serve index.html with:

python -m http.server 3000

Then open http://localhost:3000.