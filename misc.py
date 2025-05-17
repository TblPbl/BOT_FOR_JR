from datetime import datetime


def on_start():
    time_now = datetime.now().strftime('%H:%M:%S %d/%m/%Y')
    print(f'Бот начал работу  {time_now}')


def on_shutdown():
    time_now = datetime.now().strftime('%H:%M:%S %d/%m/%Y')
    print(f'Бот закончил работу в {time_now}')