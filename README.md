<p align="center">
 <img src="https://github.com/permitio/opal/assets/4082578/4e21f85f-30ab-43e2-92de-b82f78888c71" height=170 alt="opal" border="0" />
</p>
<h1 align="center">
🌤️ WeatherApp with Permit.io and OPAL Integration
</h1>

<h2 align="center">
Open Policy Administration Layer
</h2>

<a href="https://github.com/permitio/opal/actions?query=workflow%3ATests" target="_blank">
    <img src="https://github.com/permitio/opal/workflows/Tests/badge.svg" alt="Tests">
</a>
<a href="https://pypi.org/project/opal-server/" target="_blank">
    <img src="https://img.shields.io/pypi/v/opal-server?color=%2331C654&label=OPAL%20Server%20%28PyPi%29" alt="Package">
</a>
<a href="https://pypi.org/project/opal-client/" target="_blank">
    <img src="https://img.shields.io/pypi/v/opal-client?color=%2331C654&label=OPAL%20Client%20%28PyPi%29" alt="Package">
</a>
<a href="https://pepy.tech/project/opal-server" target="_blank">
    <img src="https://static.pepy.tech/personalized-badge/opal-client?period=total&units=international_system&left_color=black&right_color=blue&left_text=Downloads" alt="Downloads">
</a>

<a href="https://hub.docker.com/r/permitio/opal-server" target="_blank">
    <img src="https://img.shields.io/docker/pulls/permitio/opal-client?label=Docker%20pulls" alt="Docker pulls">
</a>

<a href="https://bit.ly/permit-slack" target="_blank">
    <img src="https://img.shields.io/badge/Slack%20Community-4A154B?logo=slack&logoColor=white" alt="Join our Slack!">
</a>
<a href="https://twitter.com/intent/follow?original_referer=https%3A%2F%2Fpublish.twitter.com%2F%3FbuttonType%3DFollowButton%26query%3Dhttps%253A%252F%252Ftwitter.com%252Fpermit_io%26widget%3DButton&ref_src=twsrc%5Etfw&region=follow_link&screen_name=permit_io&tw_p=followbutton"><img src="https://img.shields.io/twitter/follow/permit_io?label=Follow%20%40permit_io&style=social">
</a>

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

[Watch the video demo here](https://www.youtube.com/watch?v=yourvideolink)
