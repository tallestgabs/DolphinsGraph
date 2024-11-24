# DolphinsGraph
![image](https://github.com/user-attachments/assets/dfad9149-cb02-4821-8b15-1ed1b413db16)
## Universidade de Brasília 

- Projeto 1 de Teoria e Aplicação de Grafos / Semestre: 2024.2
- Professor: Dibio Leandro Borges
- *Aluno: Gabriel de Castro Dias / Matricula: 211055432*

*Para mais informações sobre o Projeto por favor leia o arquivo "proj1-tag-a-2-2024.pdf"*
## To-Do

- [x] o vértice, e seu respectivo grau (para todos os vértices);
- [x]  todos os cliques maximais (indicando o número de vértices e quais);
- [x]  O Coeficiente de Aglomeração de cada vértice;
- [x]  O Coeficiente médio de Aglomeração do Grafo.
- [x]  Gera uma visualização do grafo completo, colocando cores diferentes em todos os cliques
maximais.


# Guia de Instalação
### Bibliotecas necessárias:
1. networkx
2. matplotlib

___
- Para executar o projeto apenas instale o arquvio .zip ou clone o repositório, depois entre no diretório do arquivo e rode o comando

```python3
python3 projeto1.py
```

### Observação
Se você tiver problemas na hora de instalar as bibliotecas porque seu Python está configurado para ser gerido pelo sistema operacional, recomendo a criação de um ambiente virtual com *venv*
```bash
sudo apt install python3.12-venv
```
```python3
python3 -m venv venv
```

```bash
source venv/bin/activate
```

Agora sim você pode instalar as bibliotecas usando
```bash
pip install networkx
pip install matplotlib
```
Quando terminar não esqueça de fechar o ambiente virtual que foi ativado anteriormente
```bash
deactivate
```



