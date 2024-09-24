import pyfirmata
import time
import pygame
import random

# Configuração da placa Arduino e portas
board = pyfirmata.Arduino('COM3')  # Substitua 'COM3' pela porta do seu Arduino

led_pins = [12, 11, 10, 9]
button_pins = [5, 4, 3, 2]
buzzer_pin = 8

# Inicializa os LEDs e botões
for pin in led_pins:
    board.digital[pin].mode = pyfirmata.OUTPUT

for pin in button_pins:
    board.digital[pin].mode = pyfirmata.INPUT

# Inicializando o pygame para tocar sons
pygame.mixer.init()

# Definindo os tons para cada cor
tones = [pygame.mixer.Sound("G3.wav"), 
         pygame.mixer.Sound("C4.wav"), 
         pygame.mixer.Sound("E4.wav"), 
         pygame.mixer.Sound("G5.wav")]

# Função para acender o LED e tocar o som correspondente
def light_led_and_play_tone(led_index):
    board.digital[led_pins[led_index]].write(1)
    tones[led_index].play()
    time.sleep(0.5)  # Tempo que o LED fica aceso e o som é tocado
    board.digital[led_pins[led_index]].write(0)
    tones[led_index].stop()
    time.sleep(0.2)  # Pequeno intervalo entre os LEDs

# Função para tocar a sequência de LEDs
def play_sequence(sequence):
    for led in sequence:
        light_led_and_play_tone(led)

# Função para verificar o botão pressionado
def check_buttons():
    while True:
        for i, button_pin in enumerate(button_pins):
            if board.digital[button_pin].read() == 0:
                return i
        time.sleep(0.01)

# Função para verificar se o jogador repetiu a sequência corretamente
def check_user_sequence(sequence):
    for led in sequence:
        user_input = check_buttons()
        light_led_and_play_tone(user_input)
        if user_input != led:
            return False
    return True

# Função para tocar o som de "game over"
def game_over():
    print("Game Over!")
    tones[0].play()
    time.sleep(1)
    tones[0].stop()
    time.sleep(0.5)

# Função para tocar o som de "level up"
def level_up():
    print("Level Up!")
    tones[1].play()
    time.sleep(0.3)
    tones[2].play()
    time.sleep(0.3)
    tones[3].play()
    time.sleep(0.3)
    tones[2].stop()
    tones[1].stop()
    tones[3].stop()

# Função principal do jogo
def simon_game():
    sequence = []
    while True:
        # Adiciona um novo LED à sequência
        sequence.append(random.randint(0, 3))
        play_sequence(sequence)

        # Verifica se o jogador repetiu a sequência corretamente
        if not check_user_sequence(sequence):
            game_over()
            sequence = []  # Reinicia o jogo
            time.sleep(1)
        else:
            level_up()
            time.sleep(1)

# Inicializa o jogo Simon
if __name__ == "__main__":
    try:
        simon_game()
    except KeyboardInterrupt:
        board.exit()
