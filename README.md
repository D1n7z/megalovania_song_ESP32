<h3 align = "center">
    <img src="https://static.wikia.nocookie.net/nerddragon/images/6/6a/Sans.png/revision/latest?cb=20190217074222&path-prefix=pt-br" width="200" /><br/>
    <br/> Megalovania's song <br/>
</h3>

<br/>

## Descrição

O nosso projeto consiste em tocar a musica do jogo Undertale, "Megalovania", no ESP32, utilizando um buzzer para reproduzir as notas da música e cinco LEDs que ascendem sempre que uma nota é tocada, cada um para um tipo diferente de frequência.

<br/>

## Montagem do dispositivo físico

### Lista de materiais

| Quantidade | Nome | Link para referência |
| --- | --- | --- |
| 1 | ESP32 e cabo USB | https://www.baudaeletronica.com.br/placa-doit-esp32-bluetooth-e-wifi.html |
| 5 | LED 5mm e 3mm Alto Brilho | https://shopee.com.br/product/980365465/58218822732 |
| 1 | Buzzer Passivo 5v Continuo Arduino Raspberry | https://www.mercadolivre.com.br/buzzer-passivo-5v-continuo-arduino-raspberry/up/MLBU1990133010 |
| 1 | Protoboard | https://www.eletrogate.com/protoboard-400-pontos |
| 2 | Resistor de 150 Ohms | --- |
| 3 | Resistor de 47 Ohms | --- |
| 1 | Fonte de alimentação PowerBank | https://www.americanas.com.br/produto/2706391331 |

### Lista de conexões

| Componente | Pino da placa |
| --- | --- |
| LED A | 19 |
| LED B | 18 |
| LED C | 5 |
| LED D | 17 |
| LED E | 16 |
| Buzzer | 15 |


### Funcionamento dos LEDs e Buzzer

#### LED de 5mm e 3mm Alto Brilho

O LED (Light Emitting Diode), convencionalmente, recebe uma corrente eletrica da ponta mais longa Anodo(+) conectada ao polo positivo, transforma essa energia em luz e devolve a corrente pela ponta mais curta Catodo(-) conectada ao polo negativo. Para emitir luz, o LED precisa ser polarizado diretamente, ou seja, o anodo deve receber um potencial elétrico maior que o catodo. Quando os elétrons cruzam a junção semicondutora do LED, eles liberam energia na forma de luz. 

Detalhes:

- Utilizamos essa tabela para calcular estimadamente a resistência de cada LED:
  ![Tabela de amperagem dos LEDs](https://www.mundodaeletrica.com.br/y/5379/Bacgraund-1.jpg)

(Especificações tecnicas em: https://portal.vidadesilicio.com.br/led-com-esp32-curso-esp32-basico/).

#### Buzzer Passivo 5v

Um buzzer é um dispositivos eletromecânico ou piezoelétrico que transforma energia elétrica em som audível. diferentemente de um buzzer ativo, o buzzer passivo possui um circuito interno que é capaz de gerar um tom específico quando uma tensão específica é aplicada (como PWM ou uma frequência específica gerada por código via função ```tone()```), ideal para  projetos que requerem a geração de variados tipos de som, como a reprodução de notas musicais. 

Algumas caracteristicas:

- Polaridade: O buzzer possui um lado positivo (+, pino mais longo) e um negativo (-, pino mais curto) assim como o LED. Inverter pode danificá-lo ou impedi-lo de funcionar.

- Alimentação: A maioria opera entre 3V e 5V, compatível com os pinos GPIO do ESP32 (3.3V). Para modelos que puxam mais corrente, recomenda-se o uso de um transistor NPN ou módulo próprio

(Especificações tecnicas em: https://portal.vidadesilicio.com.br/buzzer-com-esp32-curso-esp32-basico/).

### Circuito

<p align="center">
    <img src="./Diagrama Do Circuito.png" width="400" /><br/>
    Figura - Diagrama/Imagem do circuito<br/>
</p>

<br/>

## Funcionamento do sistema

<br/>

<p align="center">
    <strong>Link para o vídeo do sistema funcionando:</strong> <br/>
    <a href="https://youtu.be/kYrjofbJoD4" target="_blank">
        <img src="https://i.ytimg.com/vi/kYrjofbJoD4/hq720.jpg?sqp=-oaymwFBCOgCEMoBSFryq4qpAzMIARUAAIhCGAHYAQHiAQoIGBACGAY4AUAB8AEB-AH-CYAC0AWKAgwIABABGGUgZShlMA8=&rs=AOn4CLBqCnFY-2CWGIi3N63t74Nb3EDiGA" alt="Video do sistema funcionando" width="500">
    </a> <br/>
</p>

<br/>

### Funções do código

| Linha(s) | Funcionalidade |
| --- | --- |
| 1 - 2 | importação de bibliotecas |
| 5, 9, 10, 11, 12, 13 | definição de pins (5 = buzzer) e (9-13  = ledA, ledB, ledC, ledD e ledE respectivamente) |
| 6 | define o tempo de espera de 150 milissegundos  |
| 7 | definição do brilho do led, sendo de aproximadamente 50% de seu máximo |
| 17-19 | definição de leds |
| 21 | definição do buzzer |
| 24 - 43 | atribuição de variáveis para cada frequência, relativo a notas musicais |
| 48 - 104 | array detentor das notas musicais de Megalovania |
| 106 | entrada no loop, o qual é infinito por ser sempre verdadeiro |
| 107 | iniciação do buzzer com frequência 670 Hz e volume nulo (sem som) |
| 108 | impressão |
| 109 | início do loop para tocar os elementos do array Megalovania  |
| 111 - 112 | se o elemento for 0, o buzzer não terá som  |
| 114 | se a frequência da nota for menor do que 280, ou seja, de A3 a CS4 |
| 115 - 119 | liga o led A e desliga os demais |
| 120 | se a frequência da nota for menor do que 320 e 280, ou seja, de D4 e DS4 |
| 121 - 125 | liga led B e desliga os demais |
| 126 | se a frequência da nota for menor do que 370 e maior do que 320, ou seja, E4 até F4 |
| 127 - 131 | liga led C e desliga demais |
| 132 | se a frequência da nota for menor do que 410 e maior do que 370, ou seja, FS4 e G4 |
| 133- 137 | liga led D e desliga os demais |
| 138 | se a frequência da nota for maior do que 410, ou seja, GS4 até D5 |
| 139 - 143 | liga led E e desliga os demais  |
| 144 | toca a frequência da nota em megalovania  |
| 145 | chamada o volume do som |
| 146 | tempo de espera até a próxima nota |
| 147 | tempo de espera até o próximo loop do array  |
| 148 | desativa o buzzer e libera os recursos que estavam sendo utilizados |
| 149 - 151 | desliga o led A, B e C |

<br/>

## Contribuir no projeto

### Features para incrementar no projeto

- [ ] Possibilidade do usuário configurar um display para mostrar uma animação enquanto a musica toca.

<br/>

## Autores do Projeto

Nathália Rodrigues Pereira

Luiggi Henrique Silva Oliveira

Eduardo Diniz da Silva
