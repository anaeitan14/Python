import random
import csv
def two():
    generate_random_ip()
    ip_dict = {}

    ip_list_read = open("ipAddress.csv", "r")
    for ip in ip_list_read.read().split():
        if ip in ip_dict.keys():
            ip_dict[ip] += 1
        else:
            ip_dict[ip] = 1

    print(sorted(ip_dict.items(), key=lambda ip_item: ip_item[1], reverse=True)[:3])


def generate_random_ip():
    ip_file = csv.writer(open("ipAddress.csv", "w"))

    for i in range(100000):
        first_num = random.randint(1, 255)
        second_num = random.randint(0, 255)
        third_num = random.randint(0, 255)
        fourth_num = random.randint(0, 255)
        ip = str(first_num) + "." + str(second_num) + "." + str(third_num) + "." + str(fourth_num)
        ip_file.writerow([ip])


if __name__ == "__main__":
    two()