Требуется изменить содержание файла hosts:
```
ansible_host - IP-адрес или DNS имя хоста для применения playbook
ansible_user - Имя пользователя для подключения по SSH
ansible_ssh_private_key_file - Путь к SSH-RSA ключу для подключения по SSH
```
Для изменения файла инвентаря (списка хостов и способа их подключения) требуется изменить файл ansible.cfg

Команда для применения playbook
> ansible-playbook -K playbook.yml

Ключ -K требуется для ручного ввода пароля для пользователя root с правами sudo