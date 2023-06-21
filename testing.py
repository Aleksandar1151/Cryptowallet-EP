port = "5000"

if port == "5000":
    with open("Keys/node1_public_hash.txt", "r") as file:
        node_address = file.read().strip()

print(node_address)