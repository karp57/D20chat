# Программа может работать только летом 2018 года
# Запускайте из консоли
import time
import vk
import vk_api


def date():
    c_time = time.ctime()
    c_time = c_time.split()
    return [c_time[1], c_time[2]]


def number_of_day(c_time):
    if c_time[0] == 'Jun':
        return int(c_time[1]) + 8 # В мае 8 свободных дней
    elif c_time[0] == 'Jul':
        return int(c_time[1]) + 38 # В июне 30 свободных дней
    else:
        return int(c_time[1]) + 69 # В июле 31 свободный день


def res_value(c_time):
    return number_of_day(c_time) / number_of_day(['Aug', '31'])


def change_name():
    global u_log, u_pas
    k = vk_api.VkApi(login = u_log, password = u_pas)
    vk.auth()
    vk.method('messages.editChat', {'chat_id':int(user_data[2]), 'title':str(9 + res_value(date())) + ' Д'})
    return 0;


print('Для корректной работы в одной папке с этим файлом должен быть сохранён файл fin.txt.\nВ нём должны быть Ваш логин, пароль для VK и ваш chat_id беседы d20!\nОни должны быть записаны в одну строчку через пробел (сначала -- логин, потом -- пароль, в конце -- chat_id)!')
fin = open('fin.txt', 'r')
user_data = fin.readlines()[0].split()
u_log, u_pas = user_data[0], user_data[1]
sec = 0
while date() != ['Sep', '1']:
    time.sleep(86400)
    change_name()
fin.close()