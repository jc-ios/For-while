def palindrome(linea):
    esPalindrome = True
    for i in range(0, len(linea) // 2):
        if linea[i] != linea[len(linea) - i - 1]:
            esPalindrome = False
            print("falso")
            break
    if esPalindrome:
        print("es palindrome ")
    else:
        print("no es palindrome")
def tablaMultiplicar():
    MIN,MAX = 1,10
    print(" ",end="")
    for i in range(MIN, MAX+1):
        print("%4d" % i,  end="")
    print()