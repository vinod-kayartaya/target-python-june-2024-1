#! .venv/bin/python
from myutils import line, dir2


class Phone(object):
    def __init__(self) -> None:
        super().__init__()
        print('Phone.__init__() called')

    def dial_number(self):
        print('dialing a number using phone')

    def print_info(self):
        print('this info is from Phone')


class MobilePhone(Phone):
    def __init__(self) -> None:
        super().__init__()
        print('MobilePhone.__init__() called')

    def send_sms(self):
        print('sending an sms using mobile phone')


class Camera(object):
    def __init__(self) -> None:
        super().__init__()
        print('Camera.__init__() called')

    def take_picture(self):
        print('taking a picture using a camera')


class Radio(object):
    def __init__(self) -> None:
        super().__init__()
        print('Radio.__init__() called')

    def print_info(self):
        print('this info is from Radio')


class SmartPhone(MobilePhone, Radio, Camera):
    def __init__(self) -> None:
        super().__init__()
        print('SmartPhone.__init__() called')

    def watch_video(self):
        print('watching video using smart phone')


def main():
    line()
    sp = SmartPhone()
    print(dir2(sp))
    sp.print_info()
    Radio.print_info(sp)

    print(SmartPhone.__mro__)
    line()

if __name__ == '__main__':
    main()

