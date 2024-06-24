<h1 align="center">
🌤️ WeatherApp with Permit.io and OPAL Integration
</h1>
<p align="center">
 <img src="https://github.com/permitio/opal/assets/4082578/4e21f85f-30ab-43e2-92de-b82f78888c71" height=80 alt="opal" border="0" />
</p>

## Overview

This project is a weather web application built with Flask, SQLAlchemy, and PostgreSQL. It demonstrates the use of Permit.io and OPAL (Open Policy Administration Layer) for real-time data and configuration updates to authorization policies across applications. The web app allows users to view weather information for different cities, showcasing a simple policy model with role-based access control (RBAC).

## Features

- 🌐 View weather information for different cities.
- 🔑 Admin and guest users with distinct access rights.
- 🕒 Real-time policy updates using OPAL.
- 🐳 Dockerized setup for easy deployment.

## Tech Stack

- **Flask**: A micro web framework for Python.
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) library for Python.
- **PostgreSQL**: An open-source relational database.
- **Permit.io**: Authorization platform.
- **OPAL**: Open Policy Administration Layer for policy and data updates.
- **Docker**: Container

## Setup and Installation

### Prerequisites

- 🐋 Docker and Docker Compose installed on your machine.
- 🐘 PostgreSQL installed and running (if not using Docker for PostgreSQL).

### Local Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/weatherapp.git
   cd weatherapp
   ```

2. **Configure the Flask app**

   Update the `SQLALCHEMY_DATABASE_URI` in `app.py` with your PostgreSQL connection details:

   ```python
   app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mypassword@localhost/sit331'
   ```

3. **Initialize the database**

   ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

4. **Run the Flask app**

   ```bash
   flask run
   ```

### Docker Setup

1. **Create a Docker network**

   ```bash
   docker network create opal_network
   ```

2. **Create a `docker-compose.yml` file**

3. **Start the services**

   ```bash
   docker-compose up -d
   ```

### Permit.io Integration

1. **Initialize Permit.io**

   Create an instance of Permit in your `app.py`.

## Usage

1. 🌐 Navigate to `http://localhost:5000` to access the web application.
2. 🔍 Use the form to search for weather information by city.
3. 🔑 Based on the user role, access rights to specific features will be determined.

### Role-Based Access Control (RBAC)

- **Admin users**: Can view and manage all city weather data.
- **Guest users**: Can only view weather data for specific cities.

## Contributing

1. 🍴 Fork the repository.
2. 🌿 Create a new branch (`git checkout -b feature-branch`).
3. 📝 Make your changes.
4. 📌 Commit your changes (`git commit -m 'Add new feature'`).
5. 🚀 Push to the branch (`git push origin feature-branch`).
6. 🔄 Open a pull request.

## Acknowledgements

- 💼 [Permit.io](https://www.permit.io/) for providing the authorization platform.
- 🔒 [OPAL](https://www.permit.io/opal) for the policy administration layer.
- 🍰 [Flask](https://flask.palletsprojects.com/) for the web framework.
- 🛠️ [SQLAlchemy](https://www.sqlalchemy.org/) for the ORM.
- 🐘 [PostgreSQL](https://www.postgresql.org/) for the database.

## 📹 Video Demo

[![Video Demo](https://img.youtube.com/vi/cp04UAQaD-E/0.jpg)](https://youtu.be/cp04UAQaD-E)
