#!/bin/bash
echo "Apando diretórios se já existirem"
rm -rf /home/publico /home/adm /home/ven /home/sec
echo "Criando diretórios"
mkdir /home/publico /home/adm /home/ven /home/sec
echo "Diretórios /home/publico /home/adm /home/ven /home/sec criados com sucesso!"
echo "Garantindo que o usuário root será o dono dos diretórios"
chown root /home/publico /home/adm /home/ven /home/sec

echo "Criando os grupos de usuários"
groupdel GRP_ADM
groupdel GRP_VEN
groupdel GRP_SEC
groupadd GRP_ADM
groupadd GRP_VEN
groupadd GRP_SEC

echo "Criando os usuários"
userdel -r -f carlos
userdel -r -f maria
userdel -r -f joao
userdel -r -f debora
userdel -r -f sebastiana
userdel -r -f roberto
userdel -r -f josefina
userdel -r -f amanda
userdel -r -f rogerio
useradd carlos -s /bin/bash -p $(openssl passwd -1 123456) -G GRP_ADM
passwd carlos -e
useradd maria -s /bin/bash -p $(openssl passwd -1 123456) -G GRP_ADM
passwd maria -e
useradd joao -s /bin/bash -p $(openssl passwd -1 123456) -G GRP_ADM
passwd joao -e
useradd debora -s /bin/bash -p $(openssl passwd -1 123456) -G GRP_VEN
passwd debora -e
useradd sebastiana -s /bin/bash -p $(openssl passwd -1 123456) -G GRP_VEN
passwd sebastiana -e
useradd roberto -s /bin/bash -p $(openssl passwd -1 123456) -G GRP_VEN
passwd roberto -e
useradd josefina -s /bin/bash -p $(openssl passwd -1 123456) -G GRP_SEC
passwd josefina -e
useradd amanda -s /bin/bash -p $(openssl passwd -1 123456) -G GRP_SEC
passwd amanda -e
useradd rogerio -s /bin/bash -p $(openssl passwd -1 123456) -G GRP_SEC
passwd rogerio -e

echo "Aplicando os privilégios"
chmod 777 /home/publico/

chown :GRP_ADM /home/adm
chmod 770 /home/adm/

chown :GRP_VEN /home/ven
chmod 770 /home/ven/

chown :GRP_SEC /home/sec
chmod 770 /home/sec/
