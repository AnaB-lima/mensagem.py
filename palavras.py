frase = input("Digite uma frase: ")

palavras = frase.split()

quantidade = len(palavras)
print(f"A frase tem {quantidade} palavra(s).")

palavras_invertidas = palavras[::-1]

frase_invertida = " ".join(palavras_invertidas)
print("Frase com as palavras invertidas:")
print(frase_invertida)
