#!/bin/bash

usuario="docker"
new_hostname=$1

# Definir o nome do host
hostnamectl set-hostname $new_hostname

# Criar o novo usuário
sudo useradd -m -s /bin/bash $usuario

# Definir a senha para o novo usuário
echo $usuario":Senha123" | sudo chpasswd

# Adicionar o novo usuário ao grupo sudo
sudo usermod -aG sudo $usuario

# Atualizando pacotes
sudo apt update -y  
sudo apt upgrade -y

# Instalando Docker
echo "Instalando o Docker......"

curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Gerando as chaves ssh para o usuário
sudo -u $usuario ssh-keygen -t rsa -b 2048 -f /home/$usuario/.ssh/id_rsa -N ""

# Autorize seu acesso ssh a VM
sudo bash -c 'echo "Sua chave RSA pública" >> /home/'$usuario'/.ssh/authorized_keys'
 
# Reiniciando o serviço do ssh
sudo systemctl restart ssh

sudo reboot