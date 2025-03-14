import socket

# XOR šifrovací funkce
def xor_enc(message, key=79089):
    return ''.join(chr(ord(c) ^ key) for c in message)

# Nastavení klienta
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 1234))
print("Připojení k serveru bylo úspěšné.")

# Přijetí šifrované zprávy
encrypted_msg = client.recv(1024).decode('utf-8')
print(f"Přijatá šifrovaná zpráva: {repr(encrypted_msg)}")

# Dešifrování zprávy
decrypted_msg = xor_enc(encrypted_msg)
print(f"Dešifrovaná zpráva: {decrypted_msg}")

# Uzavření spojení
client.close()
