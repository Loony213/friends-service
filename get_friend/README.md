
# Friends Service - Microservice

🚀 **Welcome to the Friends Service Microservice repository!** 🚀

This repository is designed for managing friend requests and user interactions in a social media application. It provides essential APIs for sending, accepting, and rejecting friend requests.

## 📂 Project Structure

```
get_friend/
├── app/
│   ├── api/
│   │   └── friends_api.py
│   ├── models/
│   │   └── friend_request.py
│   ├── services/
│   │   └── friends_service.py
│   ├── app.py
│   └── Dockerfile
├── requirements.txt
└── README.md
```

## 🛠️ Technologies & Tools

- **Python 3.x** 🐍
- **Flask**: Lightweight web framework for building RESTful APIs 🌐
- **Docker**: Containerization 🐳

## 🔗 Architecture

- **Style**: Microservice-based Architecture 🌍
- **API Style**: RESTful 🧑‍💻
- **Design Pattern**: Service Layer, Singleton pattern used for service instances 🔧

### Core Principles
- **Single Responsibility**: Each microservice performs a single task (friendship management).
- **Loose Coupling**: Each service can interact with others through APIs, but is independent.
- **Scalability**: The microservice is designed to scale horizontally for increased load.

## 🧑‍💻 Running the Application

1. Clone this repository to your local machine:

```bash
git clone https://github.com/Loony213/friends_service.git
cd friends_service
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. To run the application locally:

```bash
python app.py
```

4. To run using Docker:

```bash
docker build -t friends_service .
docker run -p 5000:5000 friends_service
```

This will make your service available at `http://localhost:5000`.


## 🔧 Docker Configuration

The project includes a **Dockerfile** to build and run the service inside a container. 

### Build the Docker image:

```bash
docker build -t friends_service .
```

### Run the Docker container:

```bash
docker run -d -p 5000:5000 friends_service
```

The service will be available on port `5000` inside the container.

## 📑 Requirements

- **Flask**: Web framework to handle API requests
- **Flask-RESTful**: To manage REST APIs
- **SQLAlchemy**: ORM for database interactions (Optional)
- **Psycopg2**: PostgreSQL database adapter (Optional)

## 🔒 Security Considerations

- **Authentication**: Use of JWT tokens (to be implemented)
- **Authorization**: Only authenticated users can send or accept friend requests

## 🌍 DockerHub & Deployment

You can push this Docker image to DockerHub with your `kamartinez` account:

```bash
docker tag friends_service kamartinez/friends_service:latest
docker push kamartinez/friends_service:latest
```

## 🔄 Contributing

Feel free to fork this repository, submit issues, and contribute to improving the service!

---

**Author**: Kamartinez 🧑‍💻  

