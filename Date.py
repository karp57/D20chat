import time
import vk
import vk_api

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def pre_period(n):
    f_counter = 0
    while n % 5 == 0:
        n //= 5
        f_counter += 1
    t_counter = 0
    while n % 2 == 0:
        n //= 2
        t_counter += 1
    return max(f_counter, t_counter)


def dec_period(a, b, PrePeriod):
    res = ""
    end = False
    counter = 0
    while not end:
        a %= b
        a *= 10
        if a == 0:
            end = True
        if counter == PrePeriod and not end:
            old_a = a
            res += "("
        elif counter > PrePeriod:
            if a == old_a:
                res += ")"
                end = True
        counter += 1
        if not end:
            res += str(a // b)
    return res

def periodic_number(a, b):
    a, b = a // gcd(a, b), b // gcd(a, b)
    ans = str(a // b) + "."
    a %= b
    PrePeriod = pre_period(b)
    return ans + dec_period(a, b, PrePeriod)

def cur_time():
    c_time = time.ctime()
    c_time = c_time.split()
    return c_time[3].split(':')


def to_next_hour(c_time):
    return (60 - int(c_time[1])) * 60 + 60 - int(c_time[2])


def date():
    c_time = time.ctime()
    c_time = c_time.split()
    return [c_time[1], c_time[2]]


def number_of_day(c_time):
    if c_time[0] == 'Jun':
        return int(c_time[1]) + 8
    elif c_time[0] == 'Jul':
        return int(c_time[1]) + 38
    else:
        return int(c_time[1]) + 69

def change_name():
    global u_log, u_pas, uid
    hours = (number_of_day(date()) - 1) * 24 + int(cur_time()[0])
    vk = vk_api.VkApi(login = u_log, password = u_pas)
    vk.auth()
    vk.method('messages.editChat', {'chat_id':int(uid), 'title':periodic_number((9 * 2400 + hours), 2400)+ ' Д'})
    return 0


fin = open('fin.txt', 'r')
user_data = fin.readlines()[0].split()
u_log, u_pas, uid = user_data[0], user_data[1], user_data[2]
change_name()
print('Success')
time.sleep(to_next_hour(cur_time()) + 10)
while date() != ['Sep', '1']:
    change_name()
    print('Success')
    time.sleep(3600)
fin.close()
