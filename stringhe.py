lista=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
maggiore= "anatra"
stringa= input("inserisci una parola: ")
for lettera in lista:
    if stringa.count(lettera) > stringa.count(maggiore):


print("La lettera che compare più spesso è la",maggiore,"e viene ripetuta" stringa.count(maggiore), "volte")