# Программа может работать только летом 2018 года
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


print('Ваш логин для VK?')
u_log = input()
print('Ваш пароль для VK?')
u_pas = input()
vk = vk_api.VkApi(login = u_log, password = u_pas)
vk.auth()
print('Вы точно хотите поменять название беседы d20? (y/[n])?')
if input() == 'y':
    vk.method('messages.editChat', {'chat_id':40, 'title':str(9 + res_value(date())) + ' Д'})
    print('Ура, название успешно изменено!')


