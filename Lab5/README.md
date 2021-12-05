# **Лабораторна робота №5**
---
## Послідовність виконання лабораторної роботи:
#### 1. Для ознайомляння з `docker-compose` звернувся до документації.
Щоб встановити `docker-compose` використав команди:
```text
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```
#### 2. Ознайомився з бібліотекою `Flask`, яку найчастіше використовують для створення простих веб-сайтів на Python.
#### 3. Моє завдання: за допомогою Docker автоматизувати розгортання веб сайту з усіма супутніми процесами. Зроблю я це двома методами: 
* за допомогою `Makefile`;
* за допомогою `docker-compose.yaml`.

#### 4. Першим розгляну метод з `Makefile`, але спочатку створю робочий проект.
#### 5. Створив папку `my_app` в якій буде знаходитись мій проект. Створив папку `tests` де будуть тести на перевірку працездатності мого проекту. Скопіював файли `my_app/templates/index.html`, `my_app/app.py `, `my_app/requirements.txt`, `tests/conftest.py`, `tests/requirements.txt`, `tests/test_app.py` з репозиторію викладача у відповідні папки мого репозеторію. Ознайомився із вмістом кожного з файлів. Звернув увагу на файл requirements.txt у папці проекту та тестах. Даний файл буде мітити залежності для мого проекту він містить назви бібліотек які імпортуються.
#### 6. Я спробував чи проект є працездатним перейшовши у папку `my_app` та після ініціалізації середовища виконав команди записані нижче:
```text
sudo pipenv --python 3.8
sudo pipenv install -r requirements.txt
sudo pipenv run python app.py
```
1. Так само я ініціалузував середовище для тестів у іншій вкладці шелу та запустив їх командою `sudo pipenv run pytest test_app.py --url http://localhost:5000` але спочатку треба перейти в папку `tests`:
   
2. Звернув увагу, що в мене автоматично створюються файли `Pipfile` та `Pipfile.lock`, а також на хост машині буде створена папка `.venv`. Після зупинки проекту видалив їх.
3. Перевірив роботу сайту перейшовши головну сторінку. Сайт не працює бо на відсутній `redis`.


#### 7. Видалив файли які постворювались після тестового запуску. Щоб моє середовище було чистим, все буде створюватись і виконуватись всередині Docker. Створив два файла `Dockerfile.app`, `Dockerfile.tests` та `Makefile` який допоможе автоматизувати процес розгортання.
#### 8. Скопіював вміст файлів `Dockerfile.app`, `Dockerfile.tests` та `Makefile` з репозиторію викладача та ознайомився із вмістом `Dockerfile` та `Makefile` та його директивами. 
Вміст файла `Dockerfile.app`:
```text
FROM python:3.8-slim
LABEL author="Ivan Svidrak"

# оновлюємо систему та встановлюємо потрібні пакети
RUN apt-get update \
    && apt-get upgrade -y\
    && apt-get install git -y\
    && pip install pipenv

WORKDIR /app

# Копіюємо файл із списком пакетів які нам потрібно інсталювати
COPY my_app/requirements.txt ./
RUN pipenv install -r requirements.txt

# Копіюємо наш додаток
COPY my_app/ ./

# Створюємо папку для логів
RUN mkdir logs

EXPOSE 5000

ENTRYPOINT pipenv run python app.py
```
Вміст файла `Dockerfile.tests`:
```text
FROM python:3.8-slim
LABEL author="Ivan Svidrak"

# оновлюємо систему та встановлюємо потрібні пакети
RUN apt-get update \
    && apt-get upgrade -y\
    && apt-get install git -y\
    && pip install pipenv

WORKDIR /tests

# Копіюємо файл із списком пакетів які нам потрібно інсталювати
COPY tests/requirements.txt ./
RUN pipenv install -r requirements.txt

# Копіюємо нашого проекту
COPY tests/ ./

ENTRYPOINT pipenv run pytest test_app.py --url http://app:5000
```
Вміст файла `Makefile`:
```text
STATES := app tests
REPO := svidrak/lab4

.PHONY: $(STATES)

$(STATES):
	@docker build -f Dockerfile.$(@) -t $(REPO):$(@) .

run:
	@docker network create --driver=bridge appnet \
	&& docker run --rm --name redis --net=appnet -d redis \
	&& docker run --rm --name app --net=appnet -p 5000:5000 -d $(REPO):app

test-app:
	@docker run --rm -it --name test --net=appnet $(REPO):tests

docker-prune:
	@docker rm $$(docker ps -a -q) --force || true \
	&& docker container prune --force \
	&& docker volume prune --force \
	&& docker network prune --force \
	&& docker image prune --force

```
Дерективи `app` та `tests`:
Створення імеджів для сайту та тесту відповідно.
Деректива `run`:
Запускає сторінку сайту.
Деректива `test-app`:
Запуск тесту сторінки.
Деректива `docker-prune`:
Очищення іміджів, контейнера і інших файлів без тегів.
#### 9. Для початку, використовуючи команду `sudo make app` створіть Docker імеджі для додатку та для тестів `sudo make tests`. Теги для цих імеджів є з моїм Docker Hub репозиторієм. Запустив додаток командою `sudo make run` та перейшовши в іншу вкладку шелу запустіть тести командою `sudo make test-app`.
Запуск сайту
```text
ivan@ivan-VirtualBox:~/PycharmProjects/pythonProject/Lab5$ sudo make run
4b37f53c68ebf6114332e00bafa96daf44502cb286e120e131db3a8fe14e825a
Unable to find image 'redis:latest' locally
latest: Pulling from library/redis
e5ae68f74026: Pull complete 
37c4354629da: Pull complete 
b065b1b1fa0f: Pull complete 
6954d19bb2e5: Pull complete 
6333f8baaf7c: Pull complete 
f9772c8a44e7: Pull complete 
Digest: sha256:2f502d27c3e9b54295f1c591b3970340d02f8a5824402c8179dcd20d4076b796
Status: Downloaded newer image for redis:latest
ccfc41dc1bd6720e67c7e53b20fd0926b5618eada810d28d426bf77ab02ea050
a8264b2489267fbdba12cb29a9fee4038b41458a340d5c792d5bfe9f9695ed80
```
Проходження тесту:
```text
ivan@ivan-VirtualBox:~/PycharmProjects/pythonProject/Lab5$ sudo make test-app
[sudo] пароль до ivan: 
============================= test session starts ==============================
platform linux -- Python 3.8.12, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /tests
collected 4 items                                                              

test_app.py ....                                                         [100%]

============================== 4 passed in 0.54s ===============================

```
* Головна сторінка:
![task_9](https://github.com/Ivan-Svidrak/Ivan_Svidrak_IK-31/blob/main/Lab5/img/1.jpg)
* Сторінка hits:
![task_9](https://github.com/Ivan-Svidrak/Ivan_Svidrak_IK-31/blob/main/Lab5/img/2.jpg)
* Сторінка logs:
![task_9](https://github.com/Ivan-Svidrak/Ivan_Svidrak_IK-31/blob/main/Lab5/img/3.jpg)
#### 10. Зупинив проект натиснувши Ctrl+C та почистив всі ресурси `Docker` за допомогою `make`.

#### 11. Створив директиву `docker-push` в Makefile для завантаження створених імеджів у мій Docker Hub репозиторій.
Деректива `docker-push`:
```text
docker-push:
	@docker login \
	&& docker push $(REPO):app \
	&& docker push $(REPO):tests
```

#### 12. Видалив створені та закачані імеджі. Команда `docker images` виводить пусті рядки. Створив директиву в Makefile яка автоматизує процес видалення моїх імеджів.
Деректива `images-delete`:
```text
images-delete:
	@docker rmi $$(docker images -q)
```

#### 13. Перейшов до іншого варіанту з використанням `docker-compose.yaml`. Для цього створив даний файл у кореновій папці проекту та заповнив вмістом з прикладу. Проект який я буду розгортити за цим варіантом трохи відрізняється від першого тим що у нього зявляється дві мережі: приватна і публічна.
Файл `docker-compose.yaml`:
```text
version: '3.8'
services:
  hits:
    build:
      context: .
      dockerfile: Dockerfile.app
    image: svidrak/lab4:compose-app
    container_name: app
    depends_on:
      - redis
    networks:
      - public
      - secret
    ports:
      - 80:5000
    volumes:
      - hits-logs:/hits/logs
  tests:
    build:
      context: .
      dockerfile: Dockerfile.tests
    image: svidrak/lab4:compose-tests
    container_name: tests
    depends_on:
      - hits
    networks:
      - public
  redis:
    image: redis:alpine
    container_name: redis
    volumes:
      - redis-data:/data
    networks:
      - secret
volumes:
  redis-data:
    driver: local
  hits-logs:
    driver: local

networks:
  secret:
    driver: bridge
  public:
    driver: bridge
```

#### 14. Перевірив чи `Docker-compose` встановлений та працює у моїй системі, а далі просто запускаю `docker-compose`:
```text
docker-compose --version
sudo docker-compose -p lab5 up
```


#### 15. Перевірив чи працює веб-сайт. Дана сторінка відображається за адресою `http://172.20.0.2:5000/`:
![task_15](https://github.com/Ivan-Svidrak/Ivan_Svidrak_IK-31/blob/main/Lab5/img/4.jpg)

#### 16. Перевірив чи компоуз створив докер імеджі. Всі теги коректні і назва репозиторія вказана коректно:
```text
ivan@ivan-VirtualBox:~/PycharmProjects/pythonProject/Lab5$ sudo docker images
[sudo] пароль до ivan: 
REPOSITORY     TAG             IMAGE ID       CREATED         SIZE
svidrak/lab4   compose-tests   8500b48c0d45   5 minutes ago   300MB
svidrak/lab4   compose-app     d4c1447b18a3   7 minutes ago   299MB
python         3.8-slim        1e46b5746c7c   2 days ago      122MB
redis          alpine          3900abf41552   5 days ago      32.4MB

```

#### 17. Зупинив проект натиснувши `Ctrl+C` і почистітив ресурси створені компоуз командою `docker-compose down`.

#### 18. Завантажив створені імеджі до Docker Hub репозиторію за допомого команди `sudo docker-compose push`.

#### 19. Що на Вашу думку краще використовувати `Makefile` чи `docker-compose.yaml`? 
- Для багатоконтейнерної структури краще використовувати docker-compose, а для простіших випадків доцільніше використовувати Makefile

#### 20. (Завдання) Оскільки Ви навчились створювати docker-compose.yaml у цій лабораторній то потрібно:
- Cтворив `docker-compose.yaml` для лабораторної №4. Компоуз повинен створити два імеджі для `Django` сайту та моніторингу, а також їх успішно запустити.
Файлик `docker-compose.yaml`:
```text
version: '3.8'
services:
  app:
    build:
      context: .
      dockerfile: Dockerfile
    image: svidrak/lab4:compose-jango
    container_name: django
    networks:
      - public
    ports:
      - 8000:8000
  monitoring:
    build:
      context: .
      dockerfile: Dockerfile.site
    image: svidrak/lab4:compose-monitoring
    container_name: monitoring
    network_mode: host

networks:
  public:
    driver: bridge
```
Сайт працює 
![task_20](https://github.com/Ivan-Svidrak/Ivan_Svidrak_IK-31/tree/main/Lab5/img/5.png)
#### 21. Після успішного виконання роботи я відредагував свій `README.md` у цьому репозиторію та створив pull request.
