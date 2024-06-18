from . import app

# We Only add this if we are running directly. When using uvicorn, this is not needed.
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)