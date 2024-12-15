"""
3. Faça um programa que recebe um número inteiro e informe se este número é par ou ímpar.
"""

num: int = int(input("Num: "))

if num % 2 == 0:
    print(f"{num} é par")
else:
    print(f"{num} é ímpar")
