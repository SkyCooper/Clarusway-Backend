# How to spin up the container

- Cd into the same level with Dockerfile
- Add .env file with variables SECRET_KEY and DEBUG.
- Build
```docker
docker build -t task-tracker-django .
```
- Run
```docker
docker run -d -p 8000:8000 task-tracker-django
```
- Test endpoints!

# Optional Discussion Topics

- How to decide the base image?
- Why using COPY statement twice?
- Can we change the ports?
- How to execute commands in the container?