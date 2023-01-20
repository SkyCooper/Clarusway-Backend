# boş bir klasör aç ve içine;
--newfolder
   --apps.py
   --dockerfile

# apps.py (python dosyası)
print('hello world')

# dockerfile (docker dosyası)
FROM python:alpine3.17
WORKDIR /app
COPY . .
CMD python apps.py


# image oluşturmak için;
docker build .
# isim veya tag vermeden oluşturur, çok kullanılmıyor.
# buradaki nokta base directory temsil ediyor, base'deki dockerfile'den oluştur demek
# eğer başka bir dockerfile kullanmak istesem veya yeri başka olsa, ../app/folder1 gibi belirtmek gerekir

# oluşturulan image'ları görmek için
docker images
docker image ls

REPOSITORY                    TAG       IMAGE ID       CREATED         SIZE
<none>                        <none>    6e9bf76e581e   4 minutes ago   52.4MB

# oluşturulan image'ları silmek için
docker image rm xox (id nin ilk 3 karakteri)
docker rmi xox
docker rmi nameofimage
# mesela; docker rmi hello-world:1

# bir containere bağlı ise -f kullanmak gerekir.
docker rmi -f hello-world:1


# TAG vererek image oluşturmak
# docker build -t nameofimage:tag .
docker build -t hello-world:1 .
# buradaki nokta base directory temsil ediyor, base'deki dockerfile'den oluştur demek
# eğer başka bir dockerfile kullanmak istesem veya yeri başka olsa, ../app/folder1 gibi belirtmek gerekir

REPOSITORY                    TAG       IMAGE ID       CREATED         SIZE
hello-world                   1         587303952c5c   4 seconds ago   52.4MB

# oluşturulan image TAG değiştirmek için;
docker tag nameofimage:tag nameofimage:newtag
#veya
docker tag nameofimage:tag newnameofimage:newtag

# sonra docker images yapılırsa IMAGE ID si aynı olan farklı isim/tag image oluşur.

# image'dan docker container oluşturmak için;
docker run hello-world:1
# çıktısı --> hello world ÇÜNKÜ;
# container, image'den oluşturuluyor, image de dockerfile'den create ediliyor,
# dockerfile de apps.py dosyasını çalıştırıyor(CMD ile)

# çalışan containerları görmek için;
docker ps
# boş gelebilir sadece yukarıdaki komutlar çalıştıysa, çünkü container oluştu, apps.py dosyasını çalıştırdı ve işi bitti,

# çalışan/çalışmayan containerları görmek için;
docker ps -a
# burada ise çalışmasa bile mutlaka görünür, 

# interaktif modda çalıştırmak için --> (it)
docker run -it hello-world:1
# açılan terminal ekranı default bash terminaldir,
# python dosyasını çalıştır ve çıktısını verir (hello world)
# interaktif mod açılmaz,

docker run -it hello-world:1 sh
# interaktif mod açılır,
# bu şekilde shell ile açılır (alpine de shell var)
# açılan ekranda ls yazıp dosyaları görebilir,
# python apps.py yazıp, dosyayı çalıştırabiliriz. (çıktısı --> hello world )
# çıkmak için exit

# container silmek için;
docker rm xox (ID sinin ilk 3 karakteri)


# bütün container'ları silmek için
docker container prune
# peşiden docker ps -a çalışırsa;
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS    PORTS     NAMES
(boş gelir.)

# dockerhub'da repository oluşturmak için,
https://hub.docker.com/
Repositories --> Create Repository
hello-world (repo ismi)
# public/privarte olabilir.


# repo'ya image push yapmak için;
# önceden image yoksa (docker build -t hello-world:1 .)

# docker push dockerusername/repositoryname
docker push coopersky/hello-world

#! An image does not exist locally with the tag: coopersky/hello-world , hatası varsa

# var olan image tag değiştirmek için;
docker tag hello-world:1 coopersky/hello-world:v1

REPOSITORY                    TAG       IMAGE ID       CREATED          SIZE  
hello-world                   1         a4094132c6f1   19 minutes ago   52.4MB
coopersky/hello-world         v1        a4094132c6f1   19 minutes ago   52.4MB


# yani repositoryname ile imagename aynı oldu,
# tekrar push ediyoruz,
docker push coopersky/hello-world:v1


# public olarak paylaşılan bir repodan image pull etmek için
docker pull eneagega/hello-world:v1
docker pull henryfrstr/hello-world:v1

# var olan image'lar bakıyorum eneagega gelmiş mi?
docker images

REPOSITORY                    TAG       IMAGE ID       CREATED          SIZE
coopersky/hello-world         v1        a4094132c6f1   25 minutes ago   52.4MB
hello-world                   1         a4094132c6f1   25 minutes ago   52.4MB
eneagega/hello-world          v1        405a1d8e0109   48 minutes ago   52.4MB

# çalıştırmak için,
docker run eneagega/hello-world:v1
# veya
docker run 405(image ID ilk 3 rakamı)

# çalışan CONTAINER durdurnmak için,
docker stop nameofCONTAINER



#! ***********************************
#! Fullstack bir projenin ayağa kaldırılması
#! ***********************************

-- DOCKER
------ frontend
------ backend

#? *****************************************
#? önce local olarak çalıştırıp kontrol ettik;
#? *****************************************

#* ----------------------------------------------------------------
#* backend ayağa kaldırmak için terminali backend içinde konumlandır
cd backend

# env dosyasını oluştur, aktif et
python -m venv env
source env/Script/activate

# requirements yükle,
pip install -r requirement.txt

# env dosyasını oluştur,
SECRET_KEY=VSVHSSY98SYSHVSHDVISHV

# migrate yap
python manage.py migrate

# localde çalıştır
python manage.py runserver


#* ----------------------------------------------------------------
#* frontend ayağa kaldırmak için yeni terminal aç ve konumunu ayarla
cd frontend

# node modules yükle
yarn veya 
yarn install

# localde çalıştır
yarn start


#? *****************************************
#? DOCKER ile çalıştırmak için;
#? *****************************************


#todo **************************************************************************************
#todo 1nci yöntem frontend ve backend klasörleri içine ayrı ayrı İMAGE ve CONTAINER oluşturma;
#todo **************************************************************************************

- dockerignore oluştur,  # (frontend ve backend aynı olabilir)
- dockerfile oluştur, # (frontend ve backend FARKLI olmak zrourunda)

   --backend için dockerfile;
        FROM python:3.9.16-bullseye
        WORKDIR /backend
        ENV PYTHONDONTWRITEBYTECODE=1
        ENV PYTHONUNBUFFERED=1
        COPY requirements.txt .
        RUN pip install -r requirements.txt
        COPY . .
        CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
        
    --frontend için dockerfile;
        FROM node:19-slim
        WORKDIR /frontend
        COPY . .
        RUN yarn install
        EXPOSE 3000
        CMD [ "yarn", "start" ]
        
# dockerfile'dan IMAGE oluştur,
docker build -t backend:v1 .
docker build -t frontend:v1 .

docker images(ile bakılabilir)

# IMAGE'lerden CONTAINER oluştur,
-p (port demek) 
-d (deamon vaya detach mod deniyor) 
-d ile yapılırsa terminalde kod kalabalıklığı olmadan arka planda çalışır,
-8000:8000 localimdeki ile dockerdaki portları eşleştiriyorum
-frontend için 3000:3000
--name container ismi
-en sona hangi IMAGE'den create edilecekse onun ismi,
docker run -p -d 8000:8000 --name nameofCONTAINER nameofIMAGE

docker run -p -d 8000:8000 --name backend backend:v1
# veya
docker run -p -d 3000:3000 --name frontend frontend:v1
# artık DOCKER üzerinde projeler çalışıyor,(frontend daha geç gelebilir)

# aslında sadece 
docker run nameofIMAGE
# bu bir CONTAINER ayağa kaldırır fakat isimsiz olur ve bir port bağlantısı olmaz,


# data'lar kalıcı değilse IMAGE'de ne varsa öyle gelir yani;
# bir CONTAINER oluşturup veri girişi yapıldıktan sonra aynı IMAGE'den yeni bir CONTAINER oluşturulduğunda
# önceden girilen veriler görünmez, (eğer kalıcı hale getirilmediyse)

# veya frontende bir değişiklik yapıldığında görünmesi için değişiklikten sonra yeni bir IMAGE oluşturup,
# ondan yeni bir CONTAINER ayağa kaldırmak gerekir.



#todo **************************************************************************************
#todo  2nci yöntem tek bir DOCKER-COMPOSE dosyası ile yapma; (SQLITE3)
#todo **************************************************************************************

# ana dizine yml uzantılı docker compose file oluşturulur,
-- DOCKER
------ frontend
------ backend
------ docker-compose.yml

# docker-compose.yml içerisine;

version: "3.8" # (opsiyonel, yazmazsak en son versiyonu alır,)

services:  # (kaç tane app dockerize edilecek, kaç container çalışacak burada yazıyoruz 1-backend, 2-frontend )

  backend: # (servis isimleri istenen şekilde verilebilir, anlaşılır olması önemli)
    image: docker-compose-backend # (oluşacak IMAGE ismi)
    build: ./backend # (neredeki dockerfile'den IMAGE oluşturacak, backend içindeki)
    ports:
      - 8000:8000 # (localimle eşleşecek port hangisi olsun, onu yazıyoruz.)
    restart: on-failure # (opsiyonel, yazılmasada olur, failure olunca restart olsun demek)

  frontend:
    image: docker-compose-frontend # (oluşacak IMAGE ismi)
    build: ./frontend # (neredeki dockerfile'den IMAGE oluşturacak, frontend içindeki)
    ports:
      - 3000:3000
    restart: on-failure
    depends_on: # (bağlantısı backend, yani önce backend ayağa kalksın, o bitince frontend ayağa kalksın)
      - backend
      

# her bir app içinde dockerfile olup/olmadığına bak, yoksa oluştur,
- dockerfile,

   --backend için dockerfile;
        FROM python:3.9.16-bullseye
        WORKDIR /backend
        ENV PYTHONDONTWRITEBYTECODE=1
        ENV PYTHONUNBUFFERED=1
        COPY requirements.txt .
        RUN pip install -r requirements.txt
        COPY . .
        CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
        
    --frontend için dockerfile;
        FROM node:19-slim
        WORKDIR /frontend
        COPY . .
        RUN yarn install
        EXPOSE 3000
        CMD [ "yarn", "start" ]
        
# terminali ana dizinde konumlandır,
docker compose up
docker compose up -d (deamon vaya detach mod) terminalde kod kalabalığı olmadan yapıyor.
# bu komut her iki dockerfile'dan önce birer tane IMAGE oluşturur
# sonra bu IMAGE'lerden CONTAINER oluşturur ve iki serviside ayağa kaldırır,

# oluşturulan CONTAINER'ları silmek için,
docker compose down

# tekrar,
docker compose up -d
# aynı IMAGE'lardan cash'ten kullanarak yeni CONTAINER oluşturur,

# herşeyi baştan kurmak yeni IMAGE, yeni CONTAINER ayağa kaldırmak için,
docker compose up -d --build



# her yeni CONTAINER oluşturulduğunda giriş yapılan data kaybolur, persist değil
# bunu önlemek için yml dosyasına volume: tanımıyoruz,

    volumes:
      - ./backend/db.sqlite3:/backend/db.sqlite3 
# yani ne demek, localimde/bilgisayarımda çalıştığım ana dizinden sonra backend klasörü içindeki db.sqlite3 ile;
# docker da oluşturduğum CONTAINER içindeki (burada ismi backend, başka birşeyde olabilir) db.sqlite3 eşleştir.
# artık her yeni CONTAINER'de girilen verilen kaybolmadan kalacak,
      - ./backend:/backend
# böyle yapınca da localimde/bilgisayarımda backend dosyasındaki kodlarda yaptığım değişiklik 
# docker da oluşturduğum CONTAINER içindeki (backend) kodlar ile eşleşti,
# artık anlık değişiklikler görünecek ve kalıcı olacak.


docker compose up -d
# yapılmış iken terminal değiştirmeden komut yazılabilir,
docker compose exec      --> # burası sabit
backend                  --> # yml dosyasındaki volume ismi
python manage.py migrate --> # hangi komut çalıştırılacaksa yazılır.

docker compose exec backend python manage.py migrate
docker compose exec backend python manage.py createsuperuser
# eğer sadece docker compose up yapılmış ise komut yazılmaz terminale,
# docker compose down yapıp tekrardan docker compose up -d yapmak lazım terminale komut yazmak için,

#? *************************************************
#? 1.sqlite3 kullanırsam docker-compose.yml içeriği;
#? *************************************************

version: "3.8"

services:
  frontend:
    image: docker-compose-frontend
    build: ./frontend
    ports:
      - 3000:3000
    restart: on-failure
    depends_on:
      - backend
    volumes:
      - ./frontend:/frontend

  backend:
    image: docker-compose-backend
    build: ./backend
    ports:
      - 8000:8000
    restart: on-failure
    volumes:
      - ./backend/db.sqlite3:/backend/db.sqlite3
      - ./backend:/backend


#todo *****************************
#todo   (POSTGRES KULLANMAK İÇİN)
#todo *****************************


# backend -> settings içindeki DATABASES bölümünü silip/yoruma alıp, 

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# } 

# postgre ayarları ile tekrar yazıyoruz,

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("SQL_DATABASE"),
        "USER": config("SQL_USER"),
        "PASSWORD": config("SQL_PASSWORD"),
        "HOST": config("SQL_HOST"),
        "PORT": config("SQL_PORT"),
        "ATOMIC_REQUESTS": True,
    }
}

# daha sonra .env dosyasının içine değişkenleri tanımlıyoruz,
SECRET_KEY=VSVHSSY98SYSHVSHDVISHV
SQL_DATABASE=docker_django
SQL_USER=cooper
SQL_PASSWORD=cooper123
SQL_HOST=db
SQL_PORT=5432 --> standart

# yml dosyası içine kullanılacak database ile ilgili verileri yazıyoruz,

  db: # (burasi ismi, istediğimiz ismi yazabiliriz.)    #! --> SQL_HOST
    image: postgres:13-alpine # (build tanımlamıyoruz, çünkü image create edeceği bir dockerfile yok,
    # buraya direk, docker up'tan kullanacağı hazır bir postgres image yazıyoruz.
    # bunu bulmak için dockerhub'tan arama yerine postgresql yazıp, tag sekmesine geçti,
    # oradan da alpine olanların boyutu küçük olur diye onu arattı.
    # postgres:13-alpine --> imagename:tagname)
    
    environment: # (bu bölümdeki değişkenler stantard, hepsi olmak zorunda, karşılarına istediğim ismi, şifreyi yazabilirim, önemli olan burada ne yazdıysam .env içinde aynısının yazılması.)
      - POSTGRES_USER=cooper                    --> SQL_USER
      - POSTGRES_PASSWORD=cooper123             --> SQL_PASSWORD
      - POSTGRES_DB=docker_django               --> SQL_DATABASE
      
# bu durumda nasıl ki frontend ayağa kalkması için önce backend ayağa kalkmalı,
# backend ayağa kalkması için önce database ayağa kalkmalı
# bunun için backend'e depends_on eklenmeli
    depends_on:
      - db
      
# postgresql sqlite3 den farklı olarak serverde çalıştığı için, volume tanımlaması yaparken postgresql datalarının kayıt edildiği standart bir yer var,

    volumes:
      - pg_data:/var/lib/postgresql/data/
      # pg_data:                  --> burası localimdeki ismi, istediğimi yazabilirim
      # /var/lib/postgresql/data/ --> burası standart, serverda CONTAINER tarafında buraya kayıt edilir.
      
# bir volüm tanımlaması yapıldı, server için fakat localde karşılığı yok, onun için localde/bilgisayarımda nereye kayıt edecek onu tanımlıyorum,

volumes:
  pg_data: -->  # yukarıda ne isim verdiysem aynısı olacak. 

# artık sqlite3 için tanımladığım volumleri silebilirm.
# bu işlemldern sonra psycopg2 paketini backend eklemek gerekiyor, postgresql çalışması için.
# psycopg2-binary>=2.8 , bunu requirements.txt içine ekle,
# docker server linux tabanlı olduğundan windowsta kurulan bazı paketler problem çıkarabiliyor,(mesela pywin32 gibi)
# bunun için requirements.txt içinde sadece ana paketler kalsın, diğerlerini silebilirsin, bu proje için sadece bunlar kalabilir,
django-cors-headers==3.13.0
djangorestframework==3.14.0
python-decouple==3.6
psycopg2-binary>=2.8

#! *************************************************
#! 2.postgesql kullanırsam docker-compose.yml içeriği;
#! *************************************************
version: "3.8"

services:
  frontend:
    image: docker-compose-frontend
    build: ./frontend
    ports:
      - 3000:3000
    restart: on-failure
    depends_on:
      - backend
    volumes:
      - ./frontend:/frontend

  backend:
    image: docker-compose-backend
    build: ./backend
    ports:
      - 8000:8000
    restart: on-failure
    volumes:
      - ./backend:/backend
    depends_on:
      - db

  db:
    image: postgres:13-alpine
    environment:
      - POSTGRES_USER=cooper
      - POSTGRES_PASSWORD=cooper123
      - POSTGRES_DB=docker_django

    volumes:
      - pg_data:/var/lib/postgresql/data/

volumes:
  pg_data: