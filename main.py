from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from database import engine
# from sqlalchemy import text

app = FastAPI(
    title="Application Review API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Application Review API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

# @app.get("/connection-status")
# def health():
#     try:
#         with engine.connect() as conn:
#            conn.execute(text("SELECT 1"))
#         return {"status": "Success", "db": "Database connected successfully"}
#     except Exception as e:
#         return {"status": "error", "db": "not connected", "error": str(e)}
