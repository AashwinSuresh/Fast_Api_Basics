# Lesson 04 — Request Bodies

A request body contains data sent with a request, commonly as JSON.

The Student Pydantic model describes the expected structure. When student: Student is used in the route, FastAPI reads the request body and validates it against that model.

The database list is only temporary storage. It is reset whenever the server restarts.

Body, Form, and UploadFile are different ways of receiving request data when JSON is not the right format.