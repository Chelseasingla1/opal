# Todo Application with Dynamic Authorization

## Overview

This project demonstrates a web application where user permissions are dynamically managed based on their karma and location. We use OPAL (Open Policy Administration Layer) with OPA (Open Policy Agent) for authorization and deploy the application on a Kubernetes cluster.

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Setup](#setup)
  - [Prerequisites](#prerequisites)
  - [Database Setup](#database-setup)
  - [Backend Setup](#backend-setup)
  - [OPAL Policy Setup](#opal-policy-setup)
  - [Kubernetes Deployment](#kubernetes-deployment)
- [Usage](#usage)

## Architecture

- **Backend:** Node.js with Express
- **Database:** MySQL
- **Authorization:** OPAL with OPA
- **Deployment:** Kubernetes

## Setup

### Prerequisites

- Node.js and npm installed
- MySQL server installed
- Docker installed
- Kubernetes cluster configured
- kubectl installed and configured
- OPAL and OPA configured

### Database Setup

1. **Create MySQL Database and Tables:**
   - Set up a MySQL database named `auth_demo`.
   - Create the necessary tables for users and todos.

### Backend Setup

1. **Install Dependencies:**
   - Use npm to initialize a Node.js project and install `express`, `mysql2`, `body-parser`, and `opa` packages.

2. **Implement Backend:**
   - Set up Express server to handle API requests for managing todos.
   - Connect to the MySQL database to store and retrieve user and todo data.
   - Integrate with OPAL for authorization based on user karma and location.

### OPAL Policy Setup

1. **Define Policies:**
   - Write policies using the Rego language to define access control rules based on user karma and location.
   - Ensure the policies are correctly evaluated by OPA.

### Kubernetes Deployment

1. **Create Kubernetes Manifests:**
   - Define Deployment and Service YAML files for the todo application and OPAL.
   - Ensure the manifests are configured to expose the necessary ports and deploy the containers.

2. **Apply Kubernetes Manifests:**
   - Use `kubectl` to apply the deployment and service configurations to your Kubernetes cluster.

## Usage

1. **Run the Application:**
   - Start the application and ensure it is running correctly.
   - Verify that the application interacts with the MySQL database and applies the authorization policies as expected.

2. **Access the Application:**
   - Use the provided endpoints to create, read, update, and delete todos.
   - Ensure that user permissions are enforced based on their karma and location.
