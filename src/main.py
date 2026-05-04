from machine import Pin, SoftI2C
import dht
import time
import network
import urequests
from ssd1306 import SSD1306_I2C

sensor = dht.DHT22(Pin(15))

i2c = SoftI2C(scl = Pin(22), sda = Pin(21))
oled = SSD1306_I2C(128, 64, i2c)

led_verde = Pin(13, Pin.OUT)
led_vermelho = Pin(12, Pin.OUT)

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect("Wokwi-GUEST", "")

while not wifi.isconnected():
  pass
print("Wifi Conectado!")

time.sleep(1)

while True:
  try:
    sensor.measure()
    temp = sensor.temperature()
    hum = sensor.humidity()

    print(f"Temperatura: {temp}°C Humidade: {hum}%")

    if temp > 30:
        led_vermelho.on()
        led_verde.off()
    else:
        led_vermelho.off()
        led_verde.on()    

    oled.fill(0)
    oled.text("Monitor DHT22", 0, 0)
    oled.text(f"Temperatura: {temp} C", 0, 20)
    oled.text(f"Humidade: {hum} %", 0, 40)

    if temp > 30:
        oled.text("Temperatura alta", 0, 55)
    oled.show()

  except Exception as e:
    print(f"Erro na leitura do sensor: {e}")
    led_vermelho.on()
    led_verde.on()
    time.sleep(0.5)
    led_vermelho.off()
    led_verde.off()

    oled.fill(0)
    oled.text("Erro no sensor", 0, 0)
    oled.show()

  time.sleep(2)
 