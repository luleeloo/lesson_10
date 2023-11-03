# task1: валідація; домашній номер телефону (тільки цифри та довжина номера)
# import re
#
#
# def validate_home_phone(phone_number):
#
#     pattern = r'^\d{7,13}$'
#
#     if re.match(pattern, phone_number):
#         return True
#     else:
#         return False
#
# task2: валідація; мобільний номер телефону (тільки цифри, можлива наявність плюса, довжина номера)
# import re
#
#
# def validate_mobile_phone(phone_number):
#
#     pattern = r'^\+?\d{10,12}$'
#
#     if re.match(pattern, phone_number):
#         return True
#     else:
#         return False
# task3: валідація; email (наявність @, домену: gmail.com наприклад, мінімальна довжина та максимальна на ваш вибір)
#
# import re
#
#
# def validate_email(email):
#
#     pattern = r'^[a-zA-Z0-9_.+-]{1,64}@[a-zA-Z0-9-]{1,64}\.[a-zA-Z]{2,64}$'
#
#     if re.match(pattern, email):
#         return True
#     else:
#         return False
#
