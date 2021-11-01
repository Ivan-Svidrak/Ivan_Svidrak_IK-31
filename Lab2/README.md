# **Лабораторна робота №2**
---
## Послідовність виконання лабораторної роботи:
#### 1. Створюю папку ***Lab2*** в якій ствоюю ***README.md***.
#### 2. За допомогою пакетного менеджера ***PIP*** інсталював ***pipenv*** та створив ізольоване середовище для ***Python***. Використовуючи команди:
```text
sudo pip install pipenv
sudo pipenv --python 3.8
sudo pipenv shell
```
Ознайомився з командаю `pipenv -h` і виконав її.
```text
ivan@ivan-VirtualBox:~/PycharmProjects/pythonProject/Lab2$ pipenv -h
Usage: pipenv [OPTIONS] COMMAND [ARGS]...

Options:
  --where                         Output project home information.
  --venv                          Output virtualenv information.
  --py                            Output Python interpreter information.
  --envs                          Output Environment Variable options.
  --rm                            Remove the virtualenv.
  --bare                          Minimal output.
  --completion                    Output completion (to be executed by the
                                  shell).

  --man                           Display manpage.
  --support                       Output diagnostic information for use in
                                  GitHub issues.

  --site-packages / --no-site-packages
                                  Enable site-packages for the virtualenv.
                                  [env var: PIPENV_SITE_PACKAGES]

  --python TEXT                   Specify which version of Python virtualenv
                                  should use.

  --three / --two                 Use Python 3/2 when creating virtualenv.
  --clear                         Clears caches (pipenv, pip, and pip-tools).
                                  [env var: PIPENV_CLEAR]

  -v, --verbose                   Verbose mode.
  --pypi-mirror TEXT              Specify a PyPI mirror.
  --version                       Show the version and exit.
  -h, --help                      Show this message and exit.


Usage Examples:
   Create a new project using Python 3.7, specifically:
   $ pipenv --python 3.7

   Remove project virtualenv (inferred from current directory):
   $ pipenv --rm

   Install all dependencies for a project (including dev):
   $ pipenv install --dev

   Create a lockfile containing pre-releases:
   $ pipenv lock --pre

   Show a graph of your installed dependencies:
   $ pipenv graph

   Check your installed dependencies for security vulnerabilities:
   $ pipenv check

   Install a local setup.py into your virtual environment/Pipfile:
   $ pipenv install -e .

   Use a lower-level pip command:
   $ pipenv run pip freeze

Commands:
  check      Checks for PyUp Safety security vulnerabilities and against PEP
             508 markers provided in Pipfile.

  clean      Uninstalls all packages not specified in Pipfile.lock.
  graph      Displays currently-installed dependency graph information.
  install    Installs provided packages and adds them to Pipfile, or (if no
             packages are given), installs all packages from Pipfile.

  lock       Generates Pipfile.lock.
  open       View a given module in your editor.
  run        Spawns a command installed into the virtualenv.
  scripts    Lists scripts in current environment config.
  shell      Spawns a shell within the virtualenv.
  sync       Installs all packages specified in Pipfile.lock.
  uninstall  Uninstalls a provided package and removes it from Pipfile.
  update     Runs lock, then sync.
ivan@ivan-VirtualBox:~/PycharmProjects/pythonProject/Lab2$
```
#### 3. Встановив бібліотеку ***requests*** в моєму середовищі. Ця бібліотека дозволяє створювати HTTP запити до заданих Web сторінок. А також встановив бібліотеку ***ntplib*** яка працює з часом.
Використав команди:
```text
sudo pipenv install requests
sudo pipenv install ntplib
```
#### 4. Створив ***app.py*** файл. Скопіював код програми із репозиторію викладача до себе. Для кращого розуміння програми ознайомився з ***Python tutorial***.
#### 5. Запускаю програму за допомогою команди ` python app.py`
Результат виконання:
```text
(Lab2) ivan@ivan-VirtualBox:~/PycharmProjects/pythonProject/Lab2$ python app.py 
========================================
Результат без параметрів: 
No URL passed to function
========================================
Результат з правильною URL: 
Time is:  01:43:03 AM
Date is:  11-01-2021
success
(Lab2) ivan@ivan-VirtualBox:~/PycharmProjects/pythonProject/Lab2$ 
```
#### 6. Встановив бібліотеку `pytest` за допомогою команди `sudo pipenv install pytest`. Для кращого розуміння ознайомився з документацією ***pytest***.
#### 7. Створив папку ***tests***, в якій створив файли ***tests.py*** і ***__init__.py***. Скопіював код програми із репозиторію викладача до себе. Запускаю програму за допомогою команди `pytest tests/tests.py`
Виконанння програми:
```text
((Lab2) ivan@ivan-VirtualBox:~/PycharmProjects/pythonProject/Lab2$ pytest tests/tests.py
========================================================== test session starts ===========================================================
platform linux -- Python 3.8.10, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: /home/ivan/PycharmProjects/pythonProject/Lab2
collected 5 items                                                                                                                        

tests/tests.py .....                                                                                                               [100%]

=========================================================== 5 passed in 0.92s ============================================================
(Lab2) ivan@ivan-VirtualBox:~/PycharmProjects/pythonProject/Lab2$ 
```
#### 8. ❗ (Захист) У програмі дописав функцію яка буде перевіряти час доби AM/PM та відповідно друкувати: Доброго дня/ночі.
Код програми:
```python
def home_work(daytime=datetime.today().strftime("%H:%M %p")):
    message = ""
    if "AM" in daytime:
        message = "Доброго дня"
    elif "PM" in daytime:
        message = "Доброї ночі"
    return message
```
#### 9. ❗ (Захист) Написав тест що буде перевіряти правильність виконання моєї функції.
Код тесту:
```python
def test_home_work(self):
        self.assertEqual(home_work("09:53 PM"), "Доброї ночі")
        self.assertEqual(home_work("02:07 AM"), "Доброго дня")
```
Виконання тесту:
```text
(Lab2) ivan@ivan-VirtualBox:~/PycharmProjects/pythonProject/Lab2$ pytest tests/tests.py
========================================================== test session starts ===========================================================
platform linux -- Python 3.8.10, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: /home/ivan/PycharmProjects/pythonProject/Lab2
collected 5 items                                                                                                                        

tests/tests.py .....                                                                                                               [100%]

=========================================================== 5 passed in 0.82s ============================================================
(Lab2) ivan@ivan-VirtualBox:~/PycharmProjects/pythonProject/Lab2$ 

```
#### 10. Перенаправляю результат виконання тестів у файл ***results.txt*** за допомогою команди `pytest tests/tests.py > results.txt`, а також додаю результат виконання програми у кінець цього ж файл за допомогою команди `python app.py >> results.txt`.
#### 11. Зробив коміт із змінами до свого репозиторію.
#### 12. Заповнив **_Makefile_** необхідними командами (bash) для повної автоматизації процесу СІ мого проекту:

Вміст **_Makefile_**:

```text
.DEFAULT_GOAL := all
all: install test run deploy
install:
	@echo " "
	@echo "--------------------------------------------"
	@echo "Installing pipenv and dependencies."
	@echo "--------------------------------------------"
	@echo " "
	sudo pip install pipenv
	sudo pipenv --python 3.8
	sudo pipenv install requests
	sudo pipenv install ntplib
	sudo pipenv install pytest
test:
	@echo " "
	@echo "--------------------------------------------"
	@echo "Start tests."
	@echo "--------------------------------------------"
	@echo " "
	sudo pipenv run pytest tests/tests.py > results.txt
run:
	@echo " "
	@echo "--------------------------------------------"
	@echo "Run Python app."
	@echo "--------------------------------------------"
	@echo " "
	sudo pipenv run python3 app.py >> results.txt
deploy:
	@echo " "
	@echo "--------------------------------------------"
	@echo "Adding and Committing results.txt to git."
	@echo "--------------------------------------------"
	@echo " "
	git add results.txt
	git commit -m "Automatic commit by MakeFile"
	git push
```

#### 13. Закомітив зміни в Makefile до власного репозиторію.