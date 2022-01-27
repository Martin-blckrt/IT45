-- README --

Si vous voulez lancer le programme depuis le main.c dans un IDE, il faut modifier la ligne 40 de :

FILE* file = fopen("berlin52.tsp", "r");

pour la transformer en :

FILE* file = fopen("../berlin52.tsp", "r");