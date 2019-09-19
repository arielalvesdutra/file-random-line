# Informações gerais

A aplicação desenvolvida realiza a leitura de um arquivo, sorteia uma das linhas presentes no arquivo e exibe a linha sorteada no console.

O projeto foi desenvolvido com Python3.

# Uso

1 - É preciso colocar o arquivo a ser lido na pasta __raiz__, antes do `src/`. Caso nãe seja colocado um arquivo para ser lido, o programa irá ler o arquivo `v.txt` que está na raiz do projeto.

2 - Executar o arquivo principal:

```bash
$ python3 run.py
```

3 - Digitar o nome do arquivo e apertar enter. __Reforçando__ que não é obrigatório colocar um arquivo, pois o projeto já vem com o `v.txt`. 

4 - Após realizar a leitura do arquivo, será exibido no console a linha sorteada.

# Testes

Comando para executar os testes:

```bash
$ python3 -m unittest discover -s tests/
```
