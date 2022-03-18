# 202203181629 Как узнать fingerprint SSH-сервера

```bash
for f in  `ls /etc/ssh/ssh_host_*.pub`; do ssh-keygen -l -f $f; done
```

Пример:

![](2022-03-18-16-42-09.png)

Для удаленного сервера, также можно использовать `ssh-keyscan`
