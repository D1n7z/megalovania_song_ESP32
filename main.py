import machine
from time import sleep_ms


buzzerPin =  15
delay = 150
duty = 523

ledA_Pin = 19
ledB_Pin = 18
ledC_Pin = 5
ledD_Pin = 17
ledE_Pin = 16

ledA = machine.Pin(ledA_Pin, machine.Pin.OUT)
ledB = machine.Pin(ledB_Pin, machine.Pin.OUT)
ledC = machine.Pin(ledC_Pin, machine.Pin.OUT)
ledD = machine.Pin(ledD_Pin, machine.Pin.OUT)
ledE = machine.Pin(ledE_Pin, machine.Pin.OUT)

buzzer = machine.PWM(machine.Pin(buzzerPin))

A3 = 220
AS3 = 233
B3 = 247
C4 = 262
CS4 = 277
D4 = 294
DS4 = 311
E4 = 330
F4 = 349
FS4 = 370
G4 = 392
GS4 = 415
A4 = 440
AS4 = 466
B4 = 494
C5 = 523
CS5 = 554
D5 = 587

# 'PAUSA': 0  # Usado para silêncios na música

# Melodia do Megalovania (Undertale)
megalovania = [
    D4, D4, D5, 0, A4, 0, GS4, G4,
    0, F4, 0, D4, F4, G4, 0, 0,
    D4, D4, D5, 0, A4, 0, GS4, G4,
    0, F4, 0, D4, F4, G4, 0, 0,
    B3, B3, D5, 0, A4, 0, GS4, G4,
    0, F4, 0, D4, F4, G4, 0, 0,
    AS3, AS3, D5, 0, A4, 0, GS4, G4,
    0, F4, 0, D4, F4, G4, 0, 0
]

while True:
    buzzer.init(freq=670, duty=0)
    print("Playing Megalovania...")
    for note in megalovania:
        print("Playing note: ", note)
        if note == 0:
            buzzer.duty(0)
        else:
            if note < 280:
                ledA.on()
                ledB.off()
                ledC.off()
                ledD.off()
                ledE.off()
            elif note < 320:
                ledA.off()
                ledB.on()
                ledC.off()
                ledD.off()
                ledE.off()
            elif note < 370:
                ledA.off()
                ledB.off()
                ledC.on()
                ledD.off()
                ledE.off()
            elif note < 410:
                ledA.off()
                ledB.off()
                ledC.off()
                ledD.on()
                ledE.off()
            else:
                ledA.off()
                ledB.off()
                ledC.off()
                ledD.off()
                ledE.on()
            buzzer.freq(note)
            buzzer.duty(duty)
        sleep_ms(delay)
    sleep_ms(delay*10)
    buzzer.deinit()
    ledA.off()
    ledB.off()
    ledC.off()
   