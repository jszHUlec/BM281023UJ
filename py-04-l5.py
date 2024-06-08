"""
napisz program, ktory wykonuje ping do hosta
i sprawdza czy host dziala
"""
import os
host = input("Podaj hosta: ")
os.system(f"ping -c 4 {host} > rezultat.txt")

with open("rezultat.txt","r") as file:
    if "icmp_seq" in file.read():
        print("host UP")
    else:
        print("host DOWN")


