# EllCare
Elder Care System

2017 Summer
# Bluetooth
## Noraml HM-10
"line encoding 없음" 또는 "Both NL & CL"

Baudrate = "9600"
## iBeacon
### Yellow sticker HM-10
"line encoding 없음"

Baudrate = "115200"
### AT Command

AT+를 입력하고 COMMAND를 입력하고 ?를 붙이면 세팅된 정보를 가져오고 PARAMETER를 입력하면 원하는 값으로 세팅한다.

ex)AT+NAME? -> 세팅된 NAME을 보여줌

ex)AT+NAMEB01 -> NAME을 B01로 

NAME 설정: AT+NAME

UUID 설정: AT+UUID

ex) AT+UUID0x0001

MAJOR 설정: AT+MARJ

ex) AT+MARJ0x0001

MINOR 설정: AT+MINO

ex) AT+MINO0x0001

iBeacon 설정: AT+IBEA 0이면 disable 1이면 enabled

advertisement 주기 설정: AT+ADVI5 5이면 0.5초 간격

AT+DELO2 : broadcast only

AT+RESET

AT+PWRM0 하면 auto sleep 이고 wake 시킬려면 80자 이상을 보내면 된다.

※ 세팅하고 한번씩 AT+RESET 해주기

## RPi iBeacon scanner
Install required library/packages
```
sudo -s

apt-get install git libbluetooth-dev libboost-python-dev libboost-thread-dev libglib2.0-dev bluez bluez-hcidump python-bluez build-essential

hciconfig hci0 up

mkdir Bluetooth
```
Install pybluez (https://pybluez.github.io/)
```
sudo -s

cd Bluetooth

git clone https://github.com/pybluez/pybluez

cd pybluez

python setup.py install

python setup.py build

cd ..
```
Install bluepy (https://github.com/IanHarvey/bluepy)
```
sudo -s

cd Bluetooth

git clone https://github.com/IanHarvey/bluepy.git

cd bluepy

python setup.py build

python setup.py install

cd ..
```
Install iBeacon-Scanner (https://github.com/search?q=pybluez&ref=opensearch)
```
cd Bluetooth

git clone https://github.com/switchdoclabs/iBeacon-Scanner-

sudo chown pi iBeacon-Scanner-

sudo chgrp pi iBeacon-Scanner-

cd iBeacon-Scanner-

sudo python testblescan.py

cd ..
```

