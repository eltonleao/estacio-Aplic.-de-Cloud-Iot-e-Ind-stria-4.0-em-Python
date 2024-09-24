# Simon Game com Arduino e Python

Este projeto implementa o famoso jogo Simon utilizando uma placa Arduino controlada por Python. O objetivo do jogo é que o jogador repita corretamente uma sequência crescente de LEDs acesos, cada um acompanhado por um som específico. O jogo continua até que o jogador erre a sequência, resultando em um "Game Over".

## Funcionamento do Jogo

- O jogo exibe uma sequência de LEDs acesos em ordem aleatória. Cada LED corresponde a uma cor e a um som.
- O jogador precisa pressionar os botões na mesma ordem em que os LEDs acenderam.
- Se o jogador acertar, um novo LED será adicionado à sequência, e o jogo continua.
- Se o jogador errar, o jogo toca um som de "Game Over" e reinicia.

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
