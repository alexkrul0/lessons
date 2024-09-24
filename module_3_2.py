
def send_email(message, recipient, *, sender='university.help@gmail.com'):

    # if ('@' and ('.com' or '.ru' or '.net')) not in (recipient or sender):
    #     print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')

    if '@' not in recipient or '@' not in sender or not (recipient.endswith(('.com', '.ru', '.net'))
            and sender.endswith(('.com', '.ru', '.net'))):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')



    # if ((('@' not in sender) or ('@' not in recipient)) or
    #         (not (sender.endswith('.com') or not (recipient.endswith('.com')) or
    #          not (sender.endswith('.ru') or not (recipient.endswith('.ru')) or
    #          not (sender.endswith('.net') or not (recipient.endswith('.net'))))))):
    #     print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
    # elif ((not sender.endswith('.com') and not recipient.endswith('.com')) and
    #     (not sender.endswith('.ru') and not recipient.endswith('.ru')) and
    #     (not sender.endswith('.net') and not recipient.endswith('.net'))):
    #     print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')

    elif sender == recipient:
        print('Нельзя отправить письмо самому самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
