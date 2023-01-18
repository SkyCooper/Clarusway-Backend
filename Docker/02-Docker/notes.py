# önce backend içine dockerfile oluştur ve içindekileri yaz
FROM python:3.9.16-slim-bullseye
WORKDIR /backend

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . .
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


# .dockerignore oluştur
*.pyc
*.pyo
*.mo
*.db
*.css.map
*.egg-info
*.sql.gz
.cache
.project
.idea
.pydevproject
.idea/workspace.xml
.DS_Store
.git/
.sass-cache
.vagrant/
__pycache__
dist
docs
env/
logs
src/{{ project_name }}/settings/local.py
src/node_modules
web/media
web/static/CACHE
stats
Dockerfile
Footer
node_modules/
npm-debug.log


# image oluştur.
docker build -t backend:v1 .
docker build -t backend:v2 .


# oluşan image'lara bak
docker images

#
docker run -p 8000:8000 --name cooperbackend  backend:1

#
docker compose up
docker compose up -d
docker compose down

#
docker compose exec backend python manage.py migrate


#


#













