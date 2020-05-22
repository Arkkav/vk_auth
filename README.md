## Авторизация на сайте через социальную сеть  "ВКонтакте".

### Техническое задание: 
Разработать веб приложение авторизации с помощью социальной сети "ВКонтакте". <br/>
Авторизация должна производится с помощью протокола oauth2. <br/>
После авторизации отобразить имя авторизованного пользователя и 5 любых друзей. <br/>
Для авторизованного пользователя создать сессию и не предлагать авторизацию при последующих заходах на сайт. <br/>

### Имплементация
Приложение реализовано на фреймворке Django с пакетом social-auth-app-django.
 
#### Основные модули 
- views - главный модуль приложения
- urls.py - URL-структура приложения

### Установка приложения 
```bash
git clone https://github.com/Arkkav/vk_auth.git vk_auth_app
cd vk_auth_app
python3 -m venv env
./env/bin/activate
pip install -r requirements.txt
```
### Запуск сервиса
```bash
manage.py runserver 
``` 
