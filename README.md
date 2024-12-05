# to-do-list

A simple application for efficient task management that lets you:

* create lists and add tasks to them
* mark tasks as done and undone
* filter lists by done and undone tasks
* delete or update tasks and lists

## Built With

- Django REST framework
- Docker
- PostgreSQL
- Nginx
- Redis
- Celery
- Flower

## Installation

1. Clone the repo

```bash
  git clone https://github.com/QEdn/to-do-list.git
```

2. Create .env file based on .env.example

```bash
  cd to-do-list
  cp .env.example .env
```

3. Run containers

```bash
  docker network create to-do-list-nw
  make build
```

## Usage

Check endpoints with OpenAPI docs:

- http://localhost:8080/api/v1/schema/swagger-ui/
- http://localhost:8080/api/v1/schema/redoc/

