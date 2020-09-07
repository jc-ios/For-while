def palindrome(linea):
    esPalindrome = True
    for i in range(0, len(linea) // 2):
        if linea[i] != linea[len(linea) - i - 1]:
            esPalindrome = False

            break
    if esPalindrome:
        print("es palindrome xxx")
    else:
        print("no es palindrome")