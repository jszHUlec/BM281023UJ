"""
parsowanie loga, tak, zeby wysweitlic tylko logi odpowiedzialne za bledy 'error' i 'fatal'
"""
# split()
# "Ale ma kota" -> ["Ala","ma","kota"]

with open("log.txt","r") as file:
    with open("new_log.txt","w") as new_file:

        for linijka in file.readlines():
            x = linijka.split(" ")
            # if "wrong password" in linijka:
            if x[2] == "ERROR":
                new_file.write(linijka)

