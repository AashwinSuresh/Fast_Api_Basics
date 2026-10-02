# Lesson 07 — CRUD API

This folder combines the earlier concepts into a complete in-memory CRUD API.

CRUD means Create, Read, Update, and Delete. The routes demonstrate these operations using POST, GET, PUT, and DELETE.

StudentCreate describes incoming data, while Student adds the generated ID used by stored students.

model_dump() converts the Pydantic model into a dictionary so its values can be passed into another model.

enumerate() is used when updating or deleting because both the student and its position in the list are needed.

The list is temporary, so all data disappears when the server restarts.