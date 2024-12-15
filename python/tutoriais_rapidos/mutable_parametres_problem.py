def add_client(name: str, client_list: list = None) -> list:
    if not client_list:
        client_list = []
    client_list.append(name)
    return client_list

client_list_1 = add_client("Kael")
add_client("Naju", client_list_1)

client_list_2 = add_client("Grace")
add_client("Nina", client_list_2)