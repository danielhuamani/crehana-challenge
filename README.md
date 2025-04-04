# Crehana Challenge – Todo List API

## 📜 Description

This project is a technical challenge for **Crehana**. It consists of a simple **Todo List API** built with **FastAPI** and containerized with **Docker**

---

## 📦 Requirements

To run this project, you must have the following installed:

- [Docker](https://www.docker.com/)

---

## ⚙️ Project Installation

Follow these steps to set up the project locally:

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/crehana-challenge.git
   cd crehana-challenge
   ```

2. **Navigate to the Docker folder**
   ```bash
   cd docker
   ```

3. **Create the `.env` file from the template**
   ```bash
   cp .env_template .env
   ```

4. **Build the Docker containers**
   ```bash
   make build
   ```

---

## ▶️ Run the Application

To start the application:

```bash
make up
```

The API will be available at: [http://localhost:8000](http://localhost:8000)

You can also access the **Swagger documentation** at:  
[http://localhost:8000/docs](http://localhost:8000/docs)

---

## Run Unit Tests

To run the test suite:

1. Open a new terminal window
2. Run:

   ```bash
   make test
   ```

This command runs all tests using `pytest` inside the Docker container.

---

## 📁 Project Structure

```
.
├── docker/                  # Docker & 
│   ├── docker-compose.yml
│   └── .env_template
├── src/                     # Application source code
│   ├── main.py
│   ├── tasks/
│   └── core/
|   |__ tests/               # Unit tests
├── Makefile                 # commands
└── README.md                
```

---

## ✅ Notes

- The app uses a **separate database for testing** (`crehana_test`) to avoid affecting real data.
- The project uses a `Makefile` to simplify common development tasks.

---

## 🛠️ Technologies Used

- **FastAPI** – High-performance Python web framework
- **SQLModel** – SQL + Pydantic + SQLAlchemy ORM
- **Docker & Docker Compose** – Containerized environment
- **Pytest** – Python testing framework
- **Make** – Task runner for development

---
