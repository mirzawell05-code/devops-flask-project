<<<<<<< HEAD
# DevOps Flask Project

A simple DevOps portfolio project with Flask, PostgreSQL, Nginx, Docker Compose and GitHub Actions CI.

## Stack

- Python Flask
- PostgreSQL
- Docker
- Docker Compose
- Nginx
- GitHub Actions

## Architecture

User → Nginx → Flask App → PostgreSQL

## Endpoints

- `/` - main page
- `/health` - health check
- `/users` - users from PostgreSQL

## Run locally

```bash
docker compose up --build

CI test

