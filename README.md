# Django E-Commerce

This is an e-commerce project that implements the backend using Django and Django REST Framework. It provides a robust and scalable solution for managing products, users, and orders.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Project Timeline](#project-timeline)
- [Installation](#installation)
- [Running Manually](#running-manually)
- [Running via docker](#installaion-and-running-via-docker)

## Features

- User authentication and authorization
- Product management (CRUD operations)
- Caching & paginate the products 
- Comment management (CRUD operations)
- Admin Dashboard customization
- Order processing and management
- Newsletter subscription
- Social authentication (e.g., Google, Facebook)
- Online Checkout (e.g., Stripe, Paymob)

## Technologies

- **Django**: A high-level Python web framework.
- **Django REST Framework**: A powerful toolkit for building Web APIs.
- **PostgreSQL**: The database used to store data.
- **Docker**: For containerization and easy deployment.
- **Cloudinary**: For image storage and management.
- **Redis**: For caching and act as message broker
- **Celery**: For implement the background tasks
- **JWT**: For tokenization
- **Swagger** : Docmumenting the APIs

## Project Timeline 
For implementing the project i come up with 5 steps

1. Write the mindmap of the project in lucid, [Mindmap Link](https://lucid.app/lucidspark/ee3c3556-7805-4883-a4fb-c2db701358e7/edit?viewport_loc=-2772%2C-926%2C3310%2C1539%2C0_0&invitationId=inv_39da33f6-1baf-4065-b39f-65f3425e5d26)

2. Write the database schema in DrawSQL, [Schema Link](https://drawsql.app/teams/test-1748/diagrams/e-commerce)

3. Divide the project into small tasks, and work on each task

4. After finishing on each task i wrote the test file.

5. push changes to github for each done task.


## Installation

```
git clone https://github.com/RadwanHegazy/Django-ECommerce.git
```

```
cd Django-ECommerce
```


## Running Manually

### Set the env vars in `example.env` for running the server without issues

```
pip install -r requirements.txt
```

```
python manage.py migrate
```


```
python manage.py runserver
```

Running Celery behind the server
```
celery -A core worker --pool=solo -l info
```

**NOTES**

1. Check for `redis` is running locally on port `6379`
2. Check that `PostgreSQL` is running locally on port `5432`


## Running via docker

### Set the env vars in `example.env` for running the server without issues

**NOTE: You must have docker in your pc.**
```
docker-compose up --build
```


### Now server is running in http://localhost:8000





