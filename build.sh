#!/bin/bash

# Votre commande de construction Docker
docker build -t amel:v1 .

# Vérifier si la construction a réussi (vérification du code de sortie)
if [ $? -eq 0 ]; then
    echo "Construction réussie."
else
    echo "Erreur de construction. Vérifiez les dépendances et le fichier requirements.txt."
fi
