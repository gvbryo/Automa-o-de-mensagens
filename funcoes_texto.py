def comando(texto):
    texto = texto.lower()
    if texto =="oi":
        print("Olá!")
    elif texto =="abrir":
        print ("Abrindo sistema...")
    elif texto == "hora":
        print ("Duas pra nestante")
    elif texto == "ria":
        print ("HAHAHAHAHAHHAHAHA")
    else:
        print("Comando invalido!")  

while True:
  texto= input("digite seu texto:")
  comando(texto)
  if texto == "Sair":
      print ("Programa finalizado")
      break