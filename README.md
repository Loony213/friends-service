
# 👥 Friends Service

This microservice is part of the **Distribuida** system and manages user friendships. It provides basic RESTful endpoints to handle friend-related operations.

---

## 📌 Features

- 🧑‍🤝‍🧑 Add and remove friends
- 👁️‍🗨️ View user friends list
- ❌ Block or unblock users
- 📡 RESTful API using FastAPI

---

## 🧩 Architecture

- 🧱 Style: Lightweight, standalone microservice
- 🌐 API: REST (FastAPI)
- 🐍 Language: Python 3.11+
- 🐳 Containerized with Docker

---

## 📁 Project Structure

```
friends-service/
├── .github/               # GitHub Actions or workflows
├── app.py                 # Main FastAPI app with routing logic
├── Dockerfile             # Docker build file
├── requirements.txt       # Python dependencies
└── README.md              # This documentation
```

---

## 🚀 How to Deploy

### 🐳 Using Docker

1. **Clone the repository**:

```bash
git clone https://github.com/Loony213/friends-service.git
cd friends-service
```

2. **Build the Docker image**:

```bash
docker build -t kamartinez/friends-service .
```

3. **Run the container**:

```bash
docker run -d -p 8000:8000 kamartinez/friends-service
```

The API will be available at:  
📍 `http://localhost:8000`

---

## 🔗 Endpoints (examples)

- `GET /friends/{username}` → Get friend list
- `POST /friends/add` → Add a friend
- `DELETE /friends/remove` → Remove a friend
- `POST /friends/block` → Block a user

> Actual endpoints may vary depending on implementation

---

## 🛠️ Requirements

- Python 3.11+
- FastAPI
- Docker
- Possibly a database (e.g., SQL Server, PostgreSQL)

---

## 👤 Author

Developed by **Loony213**  
Image on Docker Hub: `kamartinez/friends-service`  
Part of the **Distribuida** system
