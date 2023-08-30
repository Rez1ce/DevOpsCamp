Применение манифеста
> kubectl apply -f .\manifest.yml

Для проверки отработки манифеста можно использовать следующие команды:
> kubectl get replicaset -n flask-namespace
> 
> kubectl get service -n flask-namespace
> 
> kubectl get pods -n flask-namespace
```
NAME                   DESIRED   CURRENT   READY   AGE
flask-app-68cd8f7d57   3         3         3       19m

NAME            TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE
flask-service   ClusterIP   10.98.27.130   <none>        8000/TCP   2d

NAME                         READY   STATUS    RESTARTS   AGE
flask-app-68cd8f7d57-4kcsh   1/1     Running   0          20m
flask-app-68cd8f7d57-gbfpk   1/1     Running   0          20m
flask-app-68cd8f7d57-l7khm   1/1     Running   0          20m
```
Port forward для проверки по пути 127.0.0.1:8000
> kubectl port-forward service/flask-service 8000:8000 -n flask-namespace
