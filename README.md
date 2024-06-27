# Project Setup Guide

Welcome to the project! This guide will help you set up your development environment and get started.

## Prerequisites

- Ensure you have Docker and Poetry installed on your machine. If not, please follow the installation guides for [Docker](https://docs.docker.com/get-docker/) and [Poetry](https://python-poetry.org/docs/#installation).

## Setup

### Poetry Setup

1. Install project dependencies using Poetry. Run the following command in the project root directory:

    ```bash
    poetry install
    ```

### Environment Variables

2. Copy the `.env.temp` file to `.env` to set up your environment variables:

    ```bash
    cp .env.temp .env
    ```

### Docker Compose

3. To get started with Docker Compose, run the following command to build and start the containers:

    ```bash
    docker-compose up --build
    ```

This command will start all the necessary services defined in your `docker-compose.yml` file.

### Django Admin Login

4. To log in to the Django admin panel, use the credentials mentioned in the `run.sh` script. Typically, this script sets up a superuser account for you.

    ```bash
    # Example from run.sh
    # python manage.py createsuperuser --username=admin --email=admin@example.com
    ```

Refer to the `run.sh` script in your project directory for the exact command and credentials.

## Additional Resources

- For more information on how this Django project is structured, please refer to my blog post: [How to Structure the Django Project](https://blog.kdpisda.in/how-to-structure-the-django-project-9cb352814c16).
