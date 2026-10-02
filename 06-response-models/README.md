# Lesson 06 — Response Models and Status Codes

A request model describes data the client is allowed to send. A response model describes the data the API should return.

StudentCreate contains a password, but StudentResponse does not. Using response_model=StudentResponse therefore keeps the password out of the response.

status_code=status.HTTP_201_CREATED tells the client that a new resource was created successfully.

Response models keep API responses consistent and prevent unwanted fields from being returned.