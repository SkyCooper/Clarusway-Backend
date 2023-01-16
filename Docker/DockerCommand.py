# boş bir klasör aç ve içine;

# apps.py (python dosyası)
print('hello world')

# dockerfile (docker dosyası)
FROM python:alpine3.17
WORKDIR /app
COPY . .
CMD python apps.py


# image oluşturmak için;
docker build .

# oluşturulan image'ları görmek için
docker images
docker image ls

REPOSITORY                    TAG       IMAGE ID       CREATED         SIZE
<none>                        <none>    6e9bf76e581e   4 minutes ago   52.4MB

# oluşturulan image'ları silmek için
docker image rm xox (id nin ilk 3 karakteri)

# TAG vererek image oluşturmak
docker build -t hello-world:1 .

REPOSITORY                    TAG       IMAGE ID       CREATED         SIZE
hello-world                   1         587303952c5c   4 seconds ago   52.4MB

# image'dan docker container oluşturmak için;
docker run hello-world:1
# çıktısı --> hello world

# çalışan containerları görmek için;
docker ps

# çalışan/çalışmayan containerları görmek için;
docker ps -a

# it (interaktif modda çalıştı, ve bana terminal açtı)
# default bash, 
docker run -it hello-world:1 sh
# çıkmak için exit

#  image'ları silmek için ilave; (remove image with force)
# bir containere bağlı ise -f kullanmak gerekir.
docker rmi -f hello-world:1


# bütün container'ları silmek için
docker container prune
# peşiden docker ps -a çalışırsa;
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
(boş gelir.)

# dockerhub'da repository oluşturmak için,
https://hub.docker.com/
Repositories --> Create Repository
hello-world (repo ismi)


# repo'ya image push yapmak için;
# önceden image yoksa (docker build -t hello-world:1 .)

# docker push dockerusername/repositoryname
docker push coopersky/hello-world

# An image does not exist locally with the tag: coopersky/hello-world , hatası varsa

# var olan iamage tag değiştirmek için;
docker tag hello-world:1 coopersky/hello-world:v1

REPOSITORY                    TAG       IMAGE ID       CREATED          SIZE  
hello-world                   1         a4094132c6f1   19 minutes ago   52.4MB
coopersky/hello-world         v1        a4094132c6f1   19 minutes ago   52.4MB

# tekrar push ediyoruz,
docker push coopersky/hello-world:v1

# pull etmek için
docker pull eneagega/hello-world:v1

# var olan image'lar bakıyorum eneagega gelmiş mi?
docker images
REPOSITORY                    TAG       IMAGE ID       CREATED          SIZE
coopersky/hello-world         v1        a4094132c6f1   25 minutes ago   52.4MB
hello-world                   1         a4094132c6f1   25 minutes ago   52.4MB
eneagega/hello-world          v1        405a1d8e0109   48 minutes ago   52.4MB

# çalıştırmak için,
docker run eneagega/hello-world:v1
docker run 405(image ID ilk 3 rakamı)