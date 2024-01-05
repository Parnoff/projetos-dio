#!/bin/bash

sudo apt update -y
echo "UPDATE SO OK"

sudo apt upgrade -y
echo "UPGRADE SO OK"

sudo apt install apache2 -y
echo "Installion apache2 OK"

sudo apt install unzip -y
echo "Installion unzip Ok"

cd /tmp/
echo "Logado no dir tmp"

wget https://github.com/denilsonbonatti/linux-site-dio/archive/refs/heads/main.zip
echo "Download da aplicacao OK"

unzip main.zip 
echo "Arquivo extraido com sucesso"

rm main.zip
echo "main.zip deletado"

cd linux-site-dio-main

mv * /var/www/html/

cd /tmp/

rm -rf linux-site-dio-main

rm main.zip

echo "Conf Server is finish!"

