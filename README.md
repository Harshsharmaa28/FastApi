# My FastAPI App

This is a simple FastAPI application for user registration, login, linking an ID, joining data from multiple collections, and chain delete functionality.

## Setup

1. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

2. Run the FastAPI application:
    ```sh
    uvicorn app.main:app --reload
    ```

## Endpoints

- **POST /user/register**: Register a new user.
- **POST /auth/login**: Authenticate an existing user.
- **POST /user/link_id**: Link an ID to a user's account.
- **GET /data/user_data**: Get user data along with linked data.
- **DELETE /data/delete_user**: Delete a user and all associated data.