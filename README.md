# ROBOTs:

Dada uma lista de comandos, um robô deve se locomover em um mapa.

### Comandos:  
PLACE: Coloca o robô no mapa em uma posição x, y e virado para algum lado;  
RIGHT: Faz o robô virar 90º no mapa para a direita;  
LEFT: Faz o robô virar 90º no mapa para a esquerda;  
MOVE: Move o robô 1 quadrado para frente.  

### Informações:  
- Limitar o mapa para 5x5;  
- A posição x=0, y=0 indica a posição mais ao sul e ao oeste do mapa;  
- O robô deve ignorar o comando MOVE, caso esse o faça cair do mapa;  
- Todos os comandos devem ser ignorados, caso o robô ainda não tiver sido colocado no mapa (PLACE).

### Exemplos:  
a) "PLACE 0 0 NORTH", "MOVE" Retorno: 0 1 NORTH  
b) "PLACE 0 0 NORTH", "LEFT" Retorno: 0 0 WEST  
c) "PLACE 1 2 EAST", "MOVE", "MOVE", "LEFT", "MOVE" Retorno: 3 3 NORTH  
d) "PLACE 3 3 SOUTH", "MOVE", "RIGHT" Retorno: 3 2 WEST  
e) "SOUTH", "MOVE", "RIGHT", Retorno: I'm not placed yet!  
f) "SOUTH", "MOVE", "RIGHT", "PLACE 0 0 NORTH", "MOVE", "PLACE 1 2 EAST", "MOVE", "MOVE", "LEFT", "MOVE", Retorno: 3 3 NORTH

### Melhoras futuras:  
- Tratamento de comandos inválidos;  
- Adicionar obstáculos;  
- Tamanho e formato do mapa variável;  
- Comando DESTROY.
