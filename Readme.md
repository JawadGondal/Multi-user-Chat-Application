# Real-Time Multi-User Chat Application

## Overview
This is a real-time chat application built using **FastAPI**, **WebSockets**, **MySQL**, and **Docker**. The application allows multiple users to join a chat room and exchange messages in real-time.

## Features
- Multi-user chat rooms
- Real-time messaging using WebSockets
- User authentication (optional)
- MySQL database for message storage
- Dockerized deployment
- API documentation via FastAPI's interactive Swagger UI

## Project Structure
```
chat-app/
│── main.py               # Entry point for FastAPI app
│── database.py           # Database connection and ORM setup
│── models.py             # Database models
│── schemas.py            # Pydantic schemas
│── auth.py               # Authentication logic (if implemented)
│── routes/
│   ├── users.py         # User-related routes
│   ├── chat.py          # Chat-related routes
│── websocket.py         # WebSocket logic for real-time chat
│── templates/
│   ├── chat.html        # Chat front-end (HTML file)
│── static/              # Static files (CSS, JS, etc.)
│── requirements.txt      # Python dependencies
│── .env                 # Environment variables
│── Dockerfile           # Docker build instructions
│── docker-compose.yml   # Docker Compose configuration
```

## Prerequisites
Ensure you have the following installed:
- **Python 3.10+**
- **Docker & Docker Compose**
- **MySQL** (or use Docker for MySQL)

## Installation

### 1. Set up a virtual environment (Optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure environment variables
Create a `.env` file and update it with your MySQL credentials:
```
DATABASE_URL = mysql+pymysql://root:password@localhost:3306/chat_db
SECRET_KEY = 'your_secret_key_here'
```

## Running the Application

### Without Docker
1. Start MySQL manually if not using Docker.
2. Run the FastAPI server:
```bash
uvicorn main:app --reload
```
3. Open `http://127.0.0.1:8000/docs` for API documentation.
4. Open `http://127.0.0.1:8000/chat/1` to join a chat room.

### With Docker
1. Build and start the application:
```bash
docker compose up --build
```
2. Check running containers:
```bash
docker ps
```
3. Open `http://127.0.0.1:8000/chat/1` in your browser.

## API Endpoints
| Method | Endpoint | Description |
|--------|---------|-------------|
| **POST** | `/api/register` | Allows a user to create an account. |
| **POST** | `/api/login` | Allows a user to log in to their account. |
| **POST** | `/api/logout` | Allows a user to log out of their account. |
| **GET** | `/api/chat/rooms` | Returns a list of all available chat rooms. |
| **GET** | `/api/chat/rooms/{id}` | Returns the details of a specific chat room. |
| **POST** | `/api/chat/rooms/{id}/messages` | Allows a user to send a message to a specific chat room. |
| **GET** | `/api/chat/rooms/{id}/messages` | Returns a list of messages for a specific chat room. |
| **GET** | `/chat/{room_id}` | Serve the chat room HTML page. |
| **GET** | `/ws/chat/{room_id}/{username}` | Connect to a chat WebSocket. |

## WebSocket Implementation
- Users connect to the WebSocket using:
  ```bash
  ws://127.0.0.1:8000/ws/chat/{room_id}/{username}
  ```
- Messages are broadcasted to all users in the same room.
- Example Message Format:
  ```json
  { "sender": "John", "message": "Hello!" }
  ```

## Troubleshooting
- If `docker-compose` is not recognized, install Docker Desktop and restart your terminal.
- If MySQL fails to connect, verify your `.env` file and MySQL container logs using:
  ```bash
  docker logs chat-db
  ```

## License
This project is licensed under the MIT License.

