#!/bin/bash

# Falta realizar uma automação neste processo, ainda estou pensando em como contornar isso.

# Comando para definição do cluster Gerente
sudo docker swarm init --advertise-addr <IP>

# O retorno dos comando acima deverá ser executado nos nós works
sudo docker swarm join --token <TOKEN>