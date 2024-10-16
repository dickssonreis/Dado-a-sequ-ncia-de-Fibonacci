print('-'*30)
print('Sequência fibonacci')
print('-'*30)

# função para calculo 
def fibonacci_sequence(n): 
    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# função para sabe se o número pertence ou não
def is_fibonacci_number(num):
    fib_sequence = fibonacci_sequence(num)
    if num in fib_sequence:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} não pertence à sequência de Fibonacci."

# Exemplo de uso
numero = int(input("Informe um número: "))
mensagem = is_fibonacci_number(numero)
print(mensagem)
