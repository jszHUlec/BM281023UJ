import socket



def convert_ip_to_binary(ip_address):
  """Konwertuje adres IP na postać binarną."""
  binary_ip = []
  for octet in ip_address.split("."):
    binary_octet = bin(int(octet))[2:]  # Usuwa prefiks "0b"
    binary_octet = binary_octet.zfill(8)  # Uzupełnia zerami do 8 znaków
    binary_ip.append(binary_octet)
  return "".join(binary_ip)

def main():
  """Główna funkcja programu."""
  ip_address = "127.0.0.1"
  binary_ip = convert_ip_to_binary(ip_address)

  print(f"Adres IP: {ip_address}")
  print(f"Adres IP w postaci binarnej: {binary_ip}")

if __name__ == "__main__":
  main()