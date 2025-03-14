import socket

# XOR šifrovací funkce
def xor_enc(message, key=79089):
    return ''.join(chr(ord(c) ^ key) for c in message)

# Nastavení serveru
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 1234))
server.listen(1)

print("Server běží... Čekám na připojení klienta.")
client, addr = server.accept()
print(f"Připojení přijato od: {addr}")

# Zpráva k odeslání
msg = "how are you"
encrypted_msg = xor_enc(msg)  # Zašifrování zprávy
print(f"Šifrovaná zpráva: {repr(encrypted_msg)}")

# Odeslání zprávy klientovi
client.send(encrypted_msg.encode('utf-8'))
print("Šifrovaná zpráva byla odeslána klientovi.")

# Uzavření spojení
client.close()
server.close()
