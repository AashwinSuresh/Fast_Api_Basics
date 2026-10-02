# 🎟️ Event Registration API

## Project Brief

Build a **FastAPI backend** for a college event registration system.

The system should allow a college to manage its events and allow students to register for those events.

There is **no frontend requirement** for this project. The API should be completely testable through FastAPI's Swagger documentation at `/docs`.

---

## 💡 The Idea

Imagine a college conducting events such as:

- Python Workshop
- Hackathon
- Coding Competition
- AI Seminar
- Technical Talk

The backend should keep track of these events and their registrations.



A student should be able to view the available events and register for one.

An organizer should be able to create, update, and remove events.

---

## 🔧 What Your API Should Support

Your backend should provide functionality for:

- Viewing available events
- Viewing details of a particular event
- Searching or filtering events
- Creating new events
- Updating existing events
- Removing events
- Registering for an event
- Handling events that have reached their capacity

You should decide **how these operations are represented in your API**.

For example, think about:

> Which operations should use `GET`, `POST`, `PUT`, or `DELETE`?

> Which information belongs in the URL?

> Which information should be sent in the request body?

> Where would query parameters be useful?

These decisions are part of the project.

---

## 📋 Requirements

Your implementation should demonstrate the FastAPI concepts covered in the course, including:

- HTTP methods
- Path parameters
- Query parameters
- Request bodies
- Pydantic models
- Basic validation
- Appropriate responses and error handling

You may use **mock/in-memory data**(python list , dictionaries etc ..). A database is not required.

---

## 🎯 Example Scenario

Suppose an event has a capacity of `50` and currently has `49` registrations.

A new registration should be possible.

After the registration:

```text
Capacity:   50
Registered: 50
```

Another registration should not be accepted because the event is already full.

How you design and implement this behavior is up to you.

---

## 🚫 Constraints

- FastAPI must be used for the backend.
- No frontend is required.
- No database is required.
- Use the FastAPI concepts covered in the course.
- Keep the project focused on the backend functionality.

---

## ⭐ Optional

Once the basic system is working, you can add your own improvements.

For example:

- Additional filtering
- Event search
- Different event statuses
- Registration details
- Duplicate-registration handling
- Other useful features you think belong in an event system

These are optional. The focus should be on building a clean and working API.

---

## 🏆 Goal

Build a backend that could realistically serve as the API behind a college event registration application.

**The API design and implementation are up to you.**