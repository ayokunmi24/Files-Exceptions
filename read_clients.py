client_file = open('clients.txt', 'r')
clientNo = 1
for client in client_file:
    client = client.strip()
    print(f'{clientNo}. {client}')
    clientNo += 1
client_file.close()
