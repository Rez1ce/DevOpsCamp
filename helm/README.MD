Установите чарт с помощью Helm, заменив my-flask-app на имя релиза и указав автора (так же можно изменить в values.yaml):
> helm install -f values.yaml --set author="YourName" flask-application .

Параметры
```
image.repository: Имя репозитория Docker образа приложения.
image.tag: Тег Docker образа.
replicaCount: Количество реплик приложения.
author: Автор приложения.
namespace: Namespace Kubernetes, в котором будет развернуто приложение.
```