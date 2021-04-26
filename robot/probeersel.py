import serial

ser = serial.Serial('COM5', 9600, timeout=0.1)
ser.flush()
# print("should send " + msg)
while True:
    ser.write(str.encode("hoi"))
    line = ser.readline().decode('utf-8').rstrip()
    print(line)
    time.sleep(1)