#!/bin/bash

# Falta realizar uma automação neste processo, ainda estou pensando em como contornar isso.

# Comando para definição do cluster Gerente
sudo docker swarm init --advertise-addr 192.168.0.204

# O retorno dos comando acima deverá ser executado nos nós works
sudo docker swarm join --token SWMTKN-1-3qkgolmner3jw5p80umerr2l3gb0y3odd3hqk49by24ditgt32-au1x0t90csa5fnlmgonwa7627 192.168.0.204:2377