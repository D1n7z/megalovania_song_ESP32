import machine
from time import sleep_ms

buzzerpin = 15
delay = 150
duty = 523

buzzer = machine.PWM(machine.Pin(buzzerpin))

# Notas Musicais

A1 = 110
A2 = 220
A3 = 440
B3 = 494
D0 = 36
D3 = 294
G0 = 49
G1 = 98
G2 = 196

# Mélodia

megalovania = [
    D0, D0, B3, G2, G1, G0, D3, D0, D3, G0,
    A3, A3, B3, G2, G1, G0, D3, D0, D3, G0,
    A2, A2, B3, G2, G1, G0, D3, D0, D3, G0,
    A1, A1, B3, G2, G1, G0, D3, D0, D3, G0
]

while True:
    buzzer.init(freq=670, duty=0)
    print("Playing Megalovania...")
    for note in megalovania:
        print("Playing note: ", note)
        if note == 0:
            buzzer.duty(0)
        else:
            buzzer.freq(note)
            buzzer.duty(duty)
        sleep_ms(delay)
    sleep_ms(delay*10)
    buzzer.deinit()
                