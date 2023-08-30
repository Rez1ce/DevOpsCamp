Сборка образа
> docker build -t flask-app ./

Запуск контейнера из образа flask-app
> docker run -d -p 8000:8000 flask-app