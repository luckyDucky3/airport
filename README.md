### Запуск проекта

**Перед запуском необходимо скачать docker desctop:**

https://docs.docker.com/desktop/setup/install/windows-install/

и запустить его.

Далее в папке airport выполнить команду: `docker-compose up -d`

В расширениях установить MySQL и SQLTools

Подключиться к MySQL через VSCode (необязательно, но желательно):
Под рабочей областью будет плашка:

![image](https://github.com/user-attachments/assets/05585a58-ea21-437c-92f4-db451edd9a13)

Нажать "+" далее ввести localhost, admin, 100506Ki, 3308, enter.
Подключение должно пройти успешно. Если нет, то надо через wsl зайти в контейнер командой:

`docker exec -it mysql bash`

и далее выполнить:

`mysql -u root -p`

`CREATE USER 'admin'@'%' IDENTIFIED BY '100506Ki';`
`GRANT ALL PRIVILEGES ON airport_db.* TO 'admin'@'%';`
`FLUSH PRIVILEGES;`
`ALTER USER 'admin'@'%' IDENTIFIED WITH mysql_native_password BY '100506Ki';`
`FLUSH PRIVILEGES;`
`exit;`
`exit`

'docker restart mysql'

Удалить в VSCode текущее подключение и пересоздать его.

Теперь бд можно будет отслеживать через VSCode:

![image](https://github.com/user-attachments/assets/cd370f93-064c-4ab1-a9a4-36459144c3d1)


Создать виртуальное окружение: `python -m venv venv`

Активировать: `venv/Scripts/activate`

Обновить установщик: `python -m pip install --upgrade pip`

Установить зависимости: `pip install -r requirements.txt`

Применить миграции: `python manage.py migrate`

Запуск на сервере: `python blogicum/manage.py runserver`

Создание суперюзера: `python blogicum/manage.py createsuperuser`

Ввести необходимые данные
