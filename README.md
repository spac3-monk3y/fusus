# Fusus Accounts

## Installation Guide

A `docker-compose.yml` file is provided to help execute the application locally. Currently, it would only provide suport for the application's dependencies. Additionally, a **Dockerfile** is present for a containerized deployment.

The compose file provides the following dependencies:

- **Postgres**

### Requirements

- **Docker**
- **Docker compose**
- **Python3.9**

### Steps

1. Clone repository

2. Configure environment variables

   - Create `.env` file from `.env.sample`

     `$ cp .env.sample`

   - Open `.env` file and configure appropiatelly depending on the environment [1](#remarks)

3. Create virtual environment and activate it

   `python3 -m venv venv && source venv/bin/activate`

4. Install requirements

   `pip install -r requirements.txt`

5. Run dependencies in Docker

   `docker compose up`

6. Execute migrations

   `./manage.py migrate`

7. Run tests

   `./manage.py test`

8. Run app

   `./manage.py runserver`

9. Access the app's admin portal at `http://localhost:<PORT>/admin` [2](#remarks)

10. API authentication support Access the app admin pannel at `http://localhost:<PORT>/admin` [2](#remarks)

### Remarks

**1:** _Using the environment variables as defined in `.env.sample` should be enough to locally execute the application._

**2:** _The `PORT` value gets printed when running the `runserver` command (usually `8000`). Admin credentials (email and password) should be as defined in the `.env` file._

**3:** _The three authentication groups (*Administrator*, *Viewer* and *User*) are automatically created as part of the migration._

**4:** _Currently, API authentication can be done using: basic username/password for easy testing (`api/basic-auth/`) and JWT. For JWT auth, provide the token in the header in the form of `Authorization: Bearer <TOKEN>`._

**5:** _For production deployment an external storage such as **S3** is recommended._
