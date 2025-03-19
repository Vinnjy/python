import ipaddress
from ipaddress import ip_address

print(f"Задание 4\n")
ip = ip_address('10.124.56.220')
print(f"IP-адрес: {ip}")
print(f"Тип: {type(ip)}")
ip_2 = bin((int(ip)))[2:]
ip_2 = ip_2.zfill(32)
ip_2_s = str(ip_2)
result_2 = ''
for i in range(len(ip_2_s)):
    result_2 = result_2 + ip_2_s[i]
    if (i+1) % 8 == 0 and i != len(ip_2_s) - 1:
        result_2 = result_2 + '.'
print("Двоичная запись: " + result_2)

ip_binary = '00001010.01111100.00111000.11011100'
one = ip_binary[0:8]
two = ip_binary[9:17]
three = ip_binary[18:26]
four = ip_binary[27:35]
one_d = int(one, 2)
two_d = int(two, 2)
three_d = int(three, 2)
four_d = int(four, 2)
result_10 = str(one_d) + '.' + str(two_d) + '.' + str(three_d) + '.' +str(four_d)
print("Десятичная запись: " + result_10 + '\n')

print(f"Задание 5 с использованием заданного ip адреса, количества подсетей и хостов\n")
ip1 = ip_address('192.168.0.0')
ip1_s = str(ip1).split(".")
under_net = 4
hosts = 60
print(f"Для {under_net} подсетей и {hosts} хостов")
N = 0
begin = 0
end = 0
klass = ''
if 0 <= int(ip1_s[0]) <= 127:
    klass = 'A'
    N = 8
    begin = '0.0.0.0'
    end = '127.255.255.255'
elif 128 <= int(ip1_s[0]) <= 191:
    klass = 'B'
    N = 16
    begin = '128.0.0.0'
    end = '191.255.255.255'
elif 192 <= int(ip1_s[0]) <= 223:
    N = 24
    klass = 'C'
    begin = '192.0.0.0'
    end = '223.255.255.255'
elif 224 <= int(ip1_s[0]) <= 239:
    klass = 'D'
    begin = '224.0.0.0'
    end = '239.255.255.255'
else:
    klass = 'E'
    begin = '240.0.0.0'
    end = '255.255.255.255'
print(f"Класс {klass}: у класса начальный адрес - {begin} и конечный адрес - {end}")
S = 0
masks = {0:'0.0.0.0', 1:'128.0.0.0', 2:'192.0.0.0', 3:'224.0.0.0', 4:'240.0.0.0', 5:'248.0.0.0', 6:'252.0.0.0', 7:'254.0.0.0', 8:'255.0.0.0', 9:'255.128.0.0', 10:'255.192.0.0', 11:'255.224.0.0', 12:'255.240.0.0', 13:'255.248.0.0', 14:'255.252.0.0', 15:'255.254.0.0', 16:'255.255.0.0', 17:'255.255.128.0', 18:'255.255.192.0', 19:'255.255.224.0', 20:'255.255.240.0', 21:'255.255.248.0', 22:'255.255.252.0', 23:'255.255.254.0', 24:'255.255.255.0', 25:'255.255.255.128', 26:'255.255.255.192', 27:'255.255.255.224', 28:'255.255.255.240', 29:'255.255.255.248', 30:'255.255.255.252', 31:'255.255.255.254', 32:'255.255.255.255'}
for i in range(under_net):
    if 2**i >= under_net:
        S = i
        break
H = 32 - S - N
count_H = 2**H
if count_H >= hosts:
    print(f"Маска для {under_net} подсетей: {N+S}: {masks.get(N+S)} \n")
else:
    print("увы что-то не так")

print(f"Задание 5 только с применением ip адреса, то есть без учёта S по N\n")
def get_network_info(ip_address):
    try:
        ip = ipaddress.IPv4Address(ip_address) # объект IPv4Address

        first_octet = int(ip.exploded.split('.')[0])
        if first_octet <= 127:
            network_class = 'A'
        elif first_octet <= 191:
            network_class = 'B'
        elif first_octet <= 223:
            network_class = 'C'
        elif first_octet <= 239:
            network_class = 'D'
        else:
            network_class = 'E'
        if network_class == 'A':
            network = ipaddress.IPv4Network(f"{ip}/8", strict=False) # объект сети с маской
        elif network_class == 'B':
            network = ipaddress.IPv4Network(f"{ip}/16", strict=False)
        elif network_class == 'C':
            network = ipaddress.IPv4Network(f"{ip}/24", strict=False)
        else:
            print("Увы D, E не поддерживает стандартные маски подсети.")
            return 0
        print(f"IP-адрес: {ip}")
        print(f"Класс сети: {network_class}")
        print(f"Начальный адрес сети: {network.network_address}")
        print(f"Конечный адрес сети: {network.broadcast_address}")
        print(f"Маска подсети: {network.netmask}\n")
    except ValueError as e:
        print(f"Ошибка: {e}")
get_network_info("192.168.0.0")


print(f"Задание 6\n")
def calculate_network_info(network_address, num_subnets, hosts_per_subnet):
    network = ipaddress.IPv4Network(network_address, strict=False) # объект IPv4Network

    # Определяем новую маску подсети на основе количества хостов
    new_prefix = network.max_prefixlen - (hosts_per_subnet + 2).bit_length()
    subnets = list(network.subnets(new_prefix=new_prefix))

    # Ограничиваем количество подсетей до запрошенного
    if len(subnets) > num_subnets:
        subnets = subnets[:num_subnets]

    for i, subnet in enumerate(subnets, 1):
        print(f"Подсеть {i}:")
        print(f"  Маска сети: {subnet.netmask}")
        print(f"  Класс сети: {'A' if subnet.prefixlen <= 8 else 'B' if subnet.prefixlen <= 16 else 'C'}")
        print(f"  Начало сети: {subnet.network_address}")
        print(f"  Конец сети: {subnet.broadcast_address}")
        print(f"  Количество IP-адресов в сети: {subnet.num_addresses}")
        print(f"  Количество доступных IP-адресов для хостов: {subnet.num_addresses - 2}")
        print(f"  Первые 5 допустимых IP-адресов: {list(subnet.hosts())[:5]}")
        print(f"  Последние 5 допустимых IP-адресов: {list(subnet.hosts())[-5:]}")
        print()
calculate_network_info("192.168.1.0/24", 4, 30)

