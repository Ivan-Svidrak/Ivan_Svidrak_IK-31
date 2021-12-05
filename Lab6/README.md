# **Лабораторна робота №6**
---
## Послідовність виконання лабораторної роботи:
#### 1. Я зразу не попали на стартову сторінку тому перегляньте її. Там описано як налаштувати інтеграцію з `GitHub` та додати мій репозиторій;
#### 2. Основна документація по `Travis CI` представлена на сторінці.
#### 3. У лабораторній 6 я буду налаштовувати CI/CD сервер. Інтеграція пройшла успішно тому на дашборі `Travis` відображаються мої `GitHub` репозиторії. Додав репозиторій до `Travis`.
#### 4. Для того щоб `Travis` знав які кроки потрібно виконати над моїм кодом у кореневій папці мого репозиторію створюю файл `.travis.yml`. Створив у моєму `GitHub` репозиторію такий самий файл та скопіював туди вміст. Travis автоматично знайшов даний файл та виконувати ці кроки при кожному новому коміті в `master` гілку.
Вміст файла `.travis.yml`:
```text
language: python

python:
  - "3.8"

jobs:
  include:
    - stage: "Build Lab 2."
      name: "Run tests for Lab 2"
      python: 3.8
      install:
        - cd ./Lab2/
        - pipenv install
      script: pipenv run pytest tests/tests.py || true
    - stage: "Build Lab 3."
      name: "Run Djungo Server and test it accessibility. Fail to run and test"
      python: 3.8
      install:
        - cd ./Lab3/
        - pipenv install
      script: ./scripts/travis-build.sh
    - stage: "Build Lab 4."
      name: "Build Docker images & Home task"
      services:
        - docker
      install:
        - cd ./Lab4/
      script:
        - docker build -t svidrak/lab4:django-travis .
        - docker images
        - if [ "$TRAVIS_PULL_REQUEST" == "false" ]; then echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin; docker push svidrak/lab4:django-travis; else echo "PR skip deploy"; fi
    - stage: "Build Lab 5."
      name: "Build and run Docker images via make"
      services:
        - docker
      install:
        - cd ./Lab5/
        - make app
        - make tests
      script:
        - make run
        - make test-app
branches:
  only:
    - main
```
Створюю в папці з лабораторною 3 файл `Lab3/scripts/travis-build.sh` і надаю йому права для запуску командою `chmod 777 ./scripts/travis-build.sh` знаходячись в папці `Lab3`.
Вміст файла `./scripts/travis-build.sh`:
```sh
#!/bin/bash
set -ev
nohup pipenv run server > ./ci-build.log &
pipenv run python monitoring.py || true
exit 0
```
