import datetime
import random

# Написать программу определения стоимости разговора по телефону с учетом 
# скидки 20%, предоставляемой по субботам и воскресеньям
def billing_call(cost, time):
    if datetime.datetime.now().weekday() > 5:
        return time * cost * 0.8
    return time * cost

# Создать две рандомные переменные «a» и «b» от -10 до 10. Затем написать 
# скрипт, который работает по следующему принципу:
#  если “a” и “b” положительные, вывести их разность;
#  если “a” и “b” отрицательные, вывести их произведение;
#  если “a” и “b” разных знаков, вывести их сумму
def check_a_b():
    ul = 10
    ll = -10
    a = random() * (ul - ll) + ll
    b = random() * (ul - ll) + ll
    if a > 0 and b > 0:
        return a - b
    if a < 0 and b < 0:
        return a * b
    if (a < 0 and b > 0) or (a > 0 and b < 0):
        return a + b
    
# Спросите пользователя, идет ли дождь. Преобразуйте его ответ к нижнему 
# регистру. Если пользователь ответит «yes», спросите, ветрено ли на улице. Если 
# пользователь ответит «yes» и на второй вопрос, выведите сообщение «It is too 
# windy for an umbrella»; в противном случае выведите сообщение «Take an 
# umbrella». Если же пользователь не дал положительного ответа на первый вопрос, 
# выведите сообщение «Enjoy your day»
def day():
    answ1 = input("Идет ли дождь?").lower()
    if answ1 == "yes":
        print("Enjoy your day")
        return
    if answ1 == "no":
        answ2 = input("Ветренно ли на улице?").lower()
        if answ2 == "yes":
            print("It is too windy for an umbrella")
        else:
            print("Take an umbrella")

def main():
    print("Hello from lesson1-2!")


if __name__ == "__main__":
    main()
