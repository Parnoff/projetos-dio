#!/bin/bash
echo "Apando diretórios se já existirem"
rm -rf /home/publico /home/adm /home/ven /home/sec
echo "Criando diretórios"
mkdir /home/publico /home/adm /home/ven /home/sec
echo "Diretórios /home/publico /home/adm /home/ven /home/sec criados com sucesso!"
echo "Garantindo que o usuário root será o dono dos diretórios"
chown root /home/publico /home/adm /home/ven /home/sec

#Laço de repetição para os grupos
grupos=("GRP_ADM" "GRP_VEN" "GRP_SEC")

for grupo in "${grupos[@]}"; do
        groupadd "$grupo"
        echo "Grupo $grupo criado."
done

echo "Criando os usuários"

grp_adm=("carlos" "maria" "joao")
for grp1 in "${grp_adm[@]}"; do
        userdel -r -f "$grp1"
        useradd "$grp1" -s /bin/bash -G GRP_ADM
        passwd "$grp1" -e
        echo "User $grp1 criado."
done

grp_ven=("debora" "sebastiana" "roberto")
for grp2 in "${grp_ven[@]}"; do
        userdel -r -f "$grp2"
        useradd "$grp2" -s /bin/bash -G GRP_VEN
        passwd "$grp2" -e
        echo "User $grp2 criado."
done

grp_sec=("josefina" "amanda" "rogerio")
for grp3 in "${grp_sec[@]}"; do
        userdel -r -f "$grp3"
        useradd "$grp3" -s /bin/bash -G GRP_SEC
        passwd "$grp3" -e
        echo "User $grp3 criado."
done

echo "Aplicando os privilégios"
chmod 777 /home/publico/

chown :GRP_ADM /home/adm
chmod 770 /home/adm

chown :GRP_VEN /home/ven
chmod 770 /home/ven

chown :GRP_SEC /home/sec
chmod 770 /home/sec
