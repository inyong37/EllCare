# EllCare
Elder Care System

2017 Summer
## iBeacon (Bluetooth Low Energy)
### 1. Noraml HM-10
```
"line encoding 없음" 또는 "Both NL & CL"
Baudrate = "9600"
```
### 2. Yellow sticker HM-10
```
"line encoding 없음"
Baudrate = "115200"
```
### 3. AT Command

AT+를 입력하고 COMMAND를 입력하고 ?를 붙이면 세팅된 정보를 가져오고 PARAMETER를 입력하면 원하는 값으로 세팅한다.
```
ex)AT+NAME? -> 세팅된 NAME을 보여줌
ex)AT+NAMEB01 -> NAME을 B01로 
```
```
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
```
## RPi iBeacon scanner
### 1. Make workspace
```
sudo -s
mkdir Bluetooth
cd Bluetooth
```
### 2. Install dependecies
```
apt-get install git libbluetooth-dev libboost-python-dev libboost-thread-dev libglib2.0-dev bluez bluez-hcidump python-bluez build-essential
```
Turn on the bluetooth module
```
hciconfig hci0 up
```
### 3. Install pybluez
Reference: https://github.com/pybluez/pybluez
```
git clone https://github.com/pybluez/pybluez
cd pybluez
python setup.py build
python setup.py install
cd ..
```
### 4. Install bluepy
Reference: https://engineersportal.com/blog/2017/12/31/using-raspberry-pi-hm-10-and-bluepy-to-develop-an-ibeacon-mesh-network-part-1
```
git clone https://github.com/IanHarvey/bluepy.git
cd bluepy
python setup.py build
python setup.py install
cd ..
```
### 5. Install iBeacon-Scanner
```
git clone https://github.com/switchdoclabs/iBeacon-Scanner-
sudo chown pi iBeacon-Scanner-
sudo chgrp pi iBeacon-Scanner-
```
Test code
```
cd iBeacon-Scanner-
python testblescan.py
```
