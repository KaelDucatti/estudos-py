import hashlib


# Verificar os algoritmos dispníveis
print(hashlib.algorithms_available)

# Verificar algoritmos de acordo com o SO
print(hashlib.algorithms_guaranteed)

# Utilizando o SHA-256
algorithm = hashlib.sha256()
algorithm.digest()
message = "The best way to predict the futuro is create it".encode()
algorithm.update(message)
secret_message = algorithm.hexdigest()

# Utilizando o MD5


