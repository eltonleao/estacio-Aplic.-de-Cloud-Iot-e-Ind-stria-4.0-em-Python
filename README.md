# Simon Game com Arduino e Python

Este projeto faz parte de uma **iniciativa de extensão** executada na escola HappyCode, onde crianças e adolescentes entre 10 e 16 anos são introduzidos a conceitos de programação, eletrônica e IoT (Internet das Coisas) por meio da criação de um jogo Simon com Arduino.

O objetivo é ensinar de maneira prática como a programação interage com o mundo físico através de componentes eletrônicos, como LEDs, botões e buzzers. Ao final do projeto, os participantes compreendem como o código controla um dispositivo físico, além de aprenderem a lógica por trás do jogo Simon.

## Funcionamento do Jogo

- O jogo exibe uma sequência de LEDs acesos em ordem aleatória. Cada LED corresponde a uma cor e a um som.
- O jogador precisa pressionar os botões na mesma ordem em que os LEDs acenderam.
- Se o jogador acertar, um novo LED será adicionado à sequência, e o jogo continua.
- Se o jogador errar, o jogo toca um som de "Game Over" e reinicia.

## Objetivos do Projeto de Extensão

- **Introduzir crianças e adolescentes à programação e eletrônica**: Os participantes aprenderão como programar um Arduino para controlar LEDs e botões, além de instalar e configurar o código dentro de um componente físico.
- **Ensinar conceitos de IoT**: Demonstrar a interação entre software e hardware por meio da criação de um sistema eletrônico simples.
- **Promover o aprendizado prático**: A oficina utiliza o método LET (Lean Education Technology), que foca em uma abordagem prática e iterativa para o ensino, garantindo que os alunos estejam diretamente envolvidos na montagem e programação do jogo.
- **Estimular o raciocínio lógico e a criatividade**: Ao aprender a lógica do jogo Simon e como programar o Arduino, os participantes desenvolvem habilidades de resolução de problemas e criatividade.

## Requisitos de Hardware

- **Arduino Uno** (ou compatível)
- **4 LEDs** (Vermelho, Verde, Azul e Amarelo)
- **4 Botões** (Vermelho, Verde, Azul e Amarelo)
- **4 Resistores** de 220Ω (para os LEDs)
- **Buzzer Piezo**
- **Conexões jumper e uma protoboard**

### Pinagem do Arduino:

| Pino do Arduino | Componente     |
|-----------------|----------------|
| 12              | LED Vermelho   |
| 11              | LED Verde      |
| 10              | LED Azul       |
| 9               | LED Amarelo    |
| 8               | Buzzer         |
| 5               | Botão Vermelho |
| 4               | Botão Verde    |
| 3               | Botão Azul     |
| 2               | Botão Amarelo  |

### Diagrama de Conexão

Os LEDs devem ser conectados com resistores de 220Ω. Os botões devem ser conectados com resistores pull-down ou configurados no modo pull-up no Arduino.

## Requisitos de Software

- **Python 3.x**
- **Biblioteca PyFirmata** para controle do Arduino.
- **Biblioteca Pygame** para sons.
- Arduino com **firmware Firmata** instalado.

### Instalação das Dependências

1. Instale as bibliotecas Python necessárias:
   ```bash
   pip install pyfirmata pygame
   ```

2. Carregue o **firmware StandardFirmata** no seu Arduino através da IDE Arduino. Isso permite que o Python controle os pinos do Arduino usando a biblioteca **PyFirmata**.

## Como Usar

1. Certifique-se de que os componentes eletrônicos estão corretamente conectados ao Arduino de acordo com a tabela de pinagem.
2. Conecte o Arduino ao seu computador via USB.
3. Clone este repositório ou baixe os arquivos:
   ```bash
   git clone https://github.com/seu-usuario/simon-game-python-arduino.git
   ```

4. No código Python (`simon_game.py`), ajuste o valor da porta do Arduino:
   ```python
   board = pyfirmata.Arduino('COM3')  # Substitua 'COM3' pela porta correta no seu sistema
   ```

5. Execute o jogo:
   ```bash
   python simon_game.py
   ```

## Estrutura do Projeto

```
├── simon_game.py       # Código principal do jogo
├── README.md           # Instruções do projeto
├── sons/               # Pasta contendo os arquivos de som (G3.wav, C4.wav, etc.)
└── LICENSE             # Licença do projeto
```

## Sons

Os arquivos de som correspondentes a cada LED devem estar na pasta `sons/` e nomeados da seguinte forma:
- **G3.wav** (para o LED Vermelho)
- **C4.wav** (para o LED Verde)
- **E4.wav** (para o LED Azul)
- **G5.wav** (para o LED Amarelo)

## Projeto de Extensão - Detalhes

Este projeto é parte do programa de extensão na **escola HappyCode**, uma escola focada em ensinar programação e robótica para crianças e adolescentes. Durante o curso do projeto, os participantes:

1. **Montam o hardware**: Os alunos conectam LEDs, botões e resistores em um Arduino para montar a estrutura física do jogo.
2. **Programam o Arduino**: Usam um código já preparado para controlar o jogo Simon, mas antes entendem como o código funciona.
3. **Instalam o código no Arduino**: Os alunos aprendem a carregar o código no Arduino e testar o funcionamento do jogo.
4. **Experimentam o IoT na prática**: Com a interação entre o código e o hardware, os alunos ganham uma compreensão prática do que é a Internet das Coisas.