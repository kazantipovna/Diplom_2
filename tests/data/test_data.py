from helpers import orders

# Данные для проверки регистрации пользователя с незаполненным обязательным полем
register_field_missed = [("Email_no_Name", "Pass_no_Name", ""),
                         ("Email_no_Pass", "", "Name_no_Pass"),
                         ("", "Pass_no_Email", "Name_no_Email")]

# Данные для проверки редактирования пользователя
check_changes = [(None, None, 'New_Name'),
                 (None, 'New_pass', None),
                 ('New_email_666@ya.ru', None, None)]

# Список ингредиентов с некорректными хешами
incorrect_hash = [orders.get_ingredients_hash(0)+'666', orders.get_ingredients_hash(1)+'666']
