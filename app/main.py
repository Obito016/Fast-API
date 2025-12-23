from fastapi import FastAPI

# Create FastAPI app
app = FastAPI()


# Home route
@app.get("/")
def root():
    return {"message": "FastAPI server is running"}
