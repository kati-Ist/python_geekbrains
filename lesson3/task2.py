# 2. Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def statistic(name, surname, year, country, email, phone):
    return print(f"name: {name}, surname: {surname}, year: {year}, country: {country}, email: {email}, phone: {phone}")


nameUser = input("Enter name: ")
surnameUser = input("Enter surname: ")
yearUser = input("Enter year: ")
countryUser = input("Enter country: ")
emailUser = input("Enter email: ")
phoneUser = input("Enter phone: ")

statistic(name=nameUser, surname=surnameUser, year=yearUser, country=countryUser, email=emailUser, phone=phoneUser)
