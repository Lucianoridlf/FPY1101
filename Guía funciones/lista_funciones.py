

def word_length(word):
    
    word_count = 0
    for i in word:
        word_count +=1
    return word_count

def parity(num):
    if num % 2 == 0:
        return True
    else:
        return False
    

"""def number_average(number_list):
    suma = 0
    quantity = 0
    for i in number_list:
        suma += i
        quantity += 1
        resultado = ((suma) / quantity)
        return resultado
    """

def number_average(number_list):
    cont = 0
    suma = 0
    for number in number_list:
        suma += number
        cont +=1
    return (suma) / cont

        