import math
import random

print('1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.')
def ex1(number: str):
    sum = 0
    number = number.replace("-", "")
    number = number.replace(".", "")
    print(number)
    print('range: ',len(number))
    for i in range(len(number)):
        sum = sum + int(number[i])
    print(sum)
#number = str(input('Введите число: '))
#ex1(number)

print('2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.')

def ex2(number):
    list = []
    for i in range(number):
        list.append(math.factorial(i+1))
    print(list)
#number2 = int(input('Введите число: '))
#ex2(number2)

print('3. Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.')

def ex3(number):
    list = []
    for i in range(number):
        n = i + 1
        list.append((1+1/(i + 1))**(i+1))
    print(list)
#number3 = int(input('Введите число: '))
#ex3(number3)

print('4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.')
def ex4(number):
    list = []
    list2 = []
    for i in range(-number, number + 1):
        list.append(i)
    print(list)
    path = 'file.txt'
    data = open(path, 'r')
    for line in data:
        list2.append(int(line))
    data.close()
    print('Позиции для переумножения: ',list2)
    if list2[0] and list2[1] >= number:
        return print('Out of range')
    else: return print('Произведение чисел: ', list[list2[0]] * list[list2[1]])
#number4 = int(input('Введите число: '))
#ex4(number4) 

print('5. Реализуйте алгоритм перемешивания списка ')
min = 0
max = 10

def createRandomArray(min, max) -> list:
    list = []
    for i in range(max):
        list.append(random.randint(min, max))
    print(list)


def shufflingArray(list2, max) -> list:
    shflArray = list2
    for i in range(max):
        j = random.randint(0, max - 1)
        temp = shflArray[i]   #TypeError: 'NoneType' object is not subscriptable <- не довел до конца :(
        shflArray[i] = shflArray[j]
        shflArray[j] = temp
    return shflArray

firstArray = createRandomArray(min, max)
print(firstArray)
shuffleArray = shufflingArray(firstArray, max)
print(shuffleArray)
    