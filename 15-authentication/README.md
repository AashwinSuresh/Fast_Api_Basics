# Lesson 17 — Authentication Basics

Authentication checks who is making a request. Authorization controls what that authenticated user is allowed to access.

HTTPBearer() tells FastAPI to expect a bearer token in the Authorization header.

Depends(security) extracts the credentials and passes them to the route.

This example uses the fixed value demo-token only to demonstrate the flow. It is not a production authentication system and does not store users or securely issue tokens.