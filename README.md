# Crehana challenge

## Description

Crehana's todo list project for the challenge

## Requirements

requirements to execute the project:

- `docker`

## Project installation

1. **Clone the repository**
   ```bash
   git clone git@github.com:danielhuamani/crehana-challenge.git
   cd crehana-challenge
2. cd docker
2. cp .env_template .env
3. Execute command: make build

## Run
===============
- `make up`.

The API will be available at: http://localhost:8000

You can also access the Swagger documentation at:
http://localhost:8000/docs

## Uni Test
-  Open new terminal
- run `make docker-test`.


## Technologies Used
FastAPI – Web framework

SQLModel – ORM + data validation

Docker & Docker Compose – Containerization

Pytest – Testing framework