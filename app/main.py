from fastapi import FastAPI
from app.routes import users, items

app = FastAPI(title="Sample FastAPI Project")

# Include routers
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(items.router, prefix="/items", tags=["Items"])

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI Project"}
