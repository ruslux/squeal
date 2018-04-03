class template:
    sick = '🤧 Болезнь'
    sick_leave = '🏥 Посещение врача'
    sick_leave_completion = '💼 Закрытие больничного'
    holiday = '🌴 Отпуск'
    compensatory_holiday = '🕟 Запланированный отгул'
    force_majeure = '🥒 Форс-мажор'
    overtime = '🌝 Овертайм'
    monetization = '🌚 Монетизация овертайма'
    schedule_change = '⏰ Изменение графика работы'
    list = [
        sick,
        sick_leave,
        sick_leave_completion,
        holiday,
        compensatory_holiday,
        force_majeure,
        overtime,
        monetization,
        schedule_change
    ]


class dialog:
    start = 'Я могу отправлять уведомляющие электронные письма соответственно заявленным в [базовом обучении](https:/' \
            '/skynet.spl.co/projects/qacode/wiki/Правила_уведомления_о_форс-мажорных_обстоятельствах_отпуске_болезни_' \
            'и_тп_Шаблоны_писем) шаблонам:\n{}'.format('\n'.join(template.list))
    start_setup = 'Приступим к настройке, отправь мне свои имя и фамилию в следующем формате:\n'
    full_name_format = '_Ivan Ivanov_'
    parse_error = 'Не далось распарсить данные, попробуй еще раз.'
    get_auth = 'Необходимо пройти авторизацию в Google\nТвой email — {current_email}'
    get_email = 'Отправь мне свой email'
    auth_done = 'Авторизация пройдена 👍\nМожешь отправить письмо с помощью команды /report или изменить списки ' \
        'адресатов, а так же имя, фамилию, email и настройку запросов на монетизацию с помощью команды /settings'
    settings_list = 'Доступные настройки:\n'
    get_sign = '''Отправь мне свою подпись
Пример:
--
Ivan Ivanov
Junior QA engineer,
SPL
Mobile: +7 (912) 345-67-89
Skype: ivan.ivanov.spl
Telegram: @ivan_ivanov_spl'''
    sign_done = 'Подпись установлена 👍'
    default_recipients = 'Корневой список (действует на все шаблоны кроме тех, что числятся в исключениях):\n\n'
    exceptions = 'Список исключений и соответствующих адресатов (по указании корневого списка шаблон будет удален из \
списка исключений):\n\n'
    to = '**To:** '
    cc = '**CC:** '
    edit_template_recipients = 'Редактирование списка адресатов для шаблона "{template}"\nОтправь список в следующем \
формате:\n\n'
    recipients_format = '''_semen.smirnov@spl.co_ # До первого переноса строки указываются получатели "To" через пробел
_ivan.ivanov@spl.co_ # После — получатели "CC"
# Так же допустимо вставлять адресатов как "Ivan Smirnov <ivan.smirnov@spl.co>" через точку с запятой'''
    delete_exception_done = 'Список адресатов для шаблона "{template}" сброшен до корневого 👍'
    add_exception = 'Добавить исключение:\n\n'
    edit_template_recipients_done = 'Список адресатов для шаблона "Овертайм" изменен 👍'
    current_amount = 'Текущее количество овертайм-часов: {amount}'
    get_amount = 'Отправь мне актуальное количество овертайм-часов'
    edit_amount_done = 'Количество овертайм-часов актуализировано 👍'
    get_template = 'Выбери шаблон для составления письма:\n\n'
    get_overtime = 'Отправь отчет об овертайме по одной задаче в следующем формате:\n\n'
    overtime_format = '''_<[вчера | YYYY-MM-DD]>_ # По умолчанию будет взята текущая дата
_HG Спонсорство iOS ver. 1.7 (Round 3)_
_<[с 18[:00] [по {hour}[:{minute}]] | {hours}]>_ \
# По умолчанию будет взято количество часов с 19:00 указанной даты по текущий момент'''
    overtime_body = '**Тема**: Овертайм\n\nОтчет об овертайме:\n'
    send_done = 'Письмо "{theme}" отправлено 👍'
    get_monetizing = '''Текущее количество овертайм-часов: {amount}
Отправить письмо на монетизацию 40 часов?'''
    reply_notification = 'На письмо "{theme}" от {date} получен ответ от {author}:\n\n{body}'


class button:
    auth = '🔑 Авторизоваться'
    change_email = '📧 Изменить email'
    name = '📇 Имя'
    email = '📧 Email'
    sign = '🖋️ Подпись'
    recipients = '📜 Списки адресатов'
    monetization_tracking = '🏦 Запросы на монетизацию'
    edit = '✍️ Изменить'
    add_exception = '➕ Добавить исключение'
    edit_amount = '✍️ Актуализировать количество'
    show_log = '🕟 Вывести лог'
    send = '💌 Отправить'
    open_in_google_sheets = '🔗 Открыть в Google Sheets'
    open_in_gmail = '🔗 Открыть в GMail'
    add_task = '➕ Добавить задачу'
    delete = '🗑️ Удалить'
    yes = '💸 Да'
    no_dont_ask = '🏦 Нет, больше не спрашивать (действие можно отменить в /settings)'
    delete_reply = '🗑️ Пометить, как прочитанное, и переместить в корзину'
