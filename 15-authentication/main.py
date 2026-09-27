from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

app = FastAPI(title="FastAPI Basics - Lesson 15")
security = HTTPBearer()

@app.get("/public")
def public_route():
    return {"message": "Anyone can access this"}

@app.get("/protected")
def protected_route(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.credentials != "demo-token":
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"message": "Protected endpoint"}
