from typing import Text
from faker import Faker
import re
##########################
email_format = re.compile(r"\w+.\w+@\w+.\w+.(com|net|org|info|biz)")
email_list = []
#####################################################################
# for emails :
with open('potential-contacts.txt', 'r') as file:
        cont = file.readlines()
        for line in cont:
           if email_format.search(line):
             found = email_format.search(line)
             found = found.group()
             emails = sorted(found)
             email_list.append(found)
with open('emails.txt', 'w+') as file:
    cont = file.readlines()
    for email in email_list:
        file.write(f'{email}\n')
##########################################################################
#for phone numbers :
phone_nums = []
phone_num_format = re.compile(r"(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})")
special_char=[".","+1-",")","("]
area_code = "206"
with open('potential-contacts.txt', 'r') as file:
    cont = file.readlines()
    for line in cont:
        if phone_num_format.search(line):
            num_found = phone_num_format.search(line)
            num_found = num_found.group()
            #print(num_found)
            #for nums in num_found:
                #for char in special_char:
            if "(" in num_found:
             num_found = num_found.strip("(")
            if ")" in num_found:
             num_found = num_found.replace(")","-")
            if "." in num_found:
             num_found = num_found.replace(".", "-")
            if len(num_found) == 10:
              num_found = f"{num_found[:3]}-{num_found[3:5]}-{num_found[5:]}"
            if len(num_found) == 7:
              num_found = f"206{num_found}"
            phone_nums.append(num_found)
            print(phone_nums)
            phone_nums = sorted(phone_nums)
with open('phone_numbers.txt', 'w+') as file:
    cont = file.readlines()
    for number in phone_nums:
        file.write(f'{number}\n')




