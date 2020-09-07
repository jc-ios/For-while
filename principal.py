# primer ejemplo de uso de for
# es un palindrome
linea = input("Digite una palabra")
esPalindrome = True
for i in range(0, len(linea)//2):
    if linea[i] != linea[len(linea)-i-1]:
        esPalindrome = False
        print("falso")
        break
if esPalindrome:
    print("es palindrome xxx")
else:
    print("no es palindrome")