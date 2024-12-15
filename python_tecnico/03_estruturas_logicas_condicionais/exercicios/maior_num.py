"""
1. Faça um programa que receba dois números inteiros e mostre qual deles é o maior.
"""

num1: int = int(input("Num 1: "))
num2: int = int(input("Num 2: "))

if num1 > num2:
    print(f"{num1} é maior que {num2}")
elif num1 < num2:
    print(f"{num2} é maior que {num1}")
else:
    print("Os números são iguais")
    