# Lesson 14 — Response Types

FastAPI can return more than JSON.

PlainTextResponse sends plain text, HTMLResponse sends HTML, and FileResponse sends a file from the server.

The generic Response class is useful when you want to control the response content, media type, or headers yourself. The examples use it for plain text, CSV, and XML.

Content-Type tells the client what kind of data it received. Content-Disposition can tell the browser to display a response inline or treat it as a downloadable file.

The sample PDF must exist in the files folder before the download endpoint is tested.