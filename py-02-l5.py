# pobierz od uzytkownika jego IP i wyswietl poszczegolne elementy
# 10.0.0.3
# oct1= 10
# oct2= 0
# oct3= 0
# oct4= 3

ip = input("podaj adres IP:").split(".")

print(f"twoje IP: {ip[0]} - {ip[1]} - {ip[2]} - {ip[3]}")

print("oct1: ", bin(int(ip[0]))[2:])
print("oct2: ", bin(int(ip[1]))[2:])
print("oct3: ", bin(int(ip[2]))[2:])
print("oct4: ", bin(int(ip[3]))[2:]) # 0xFF 0b11101