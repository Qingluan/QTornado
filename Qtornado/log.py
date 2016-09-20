from termcolor import cprint, colored

INFO = 0x08
ERR = 0x00
OK = 0x04
WRN = 0x02
FAIL = 0x01



def tag_print(tag, *args, tag_color='red', tag_attr=['bold', 'blink'], txt_color='grey', txt_attr=[], **kargs):
    tag = "[%s] " % colored(tag, tag_color, attrs=tag_attr)
    txt = colored(' '.join([str(i) for i in args]), txt_color, attrs=txt_attr)
    print(tag + txt, **kargs)


class LogControl:
    INFO = 0x08
    ERR = 0x00
    OK = 0x04
    WRN = 0x02
    FAIL = 0x01
    LOG_LEVEL = 0x00 | 0x01 | 0x02

    @staticmethod
    def err(*args, txt_color='grey', txt_attr=['bold'], **kargs):
        tag_print('err', *args, txt_color=txt_color, txt_attr=txt_attr, **kargs)

    @staticmethod
    def info(*args, txt_color='grey', txt_attr=[], **kargs):
        if LogControl.LOG_LEVEL & INFO:
            tag_print('info', *args,  tag_color='cyan', tag_attr=['bold'],  txt_color=txt_color, txt_attr=txt_attr, **kargs)

    @staticmethod
    def wrn(*args, txt_color='grey', txt_attr=[], **kargs):
        if LogControl.LOG_LEVEL & WRN:
            tag_print('warning', *args,  tag_color='yellow', tag_attr=['bold'],  txt_color=txt_color, txt_attr=txt_attr, **kargs)

    @staticmethod
    def ok(*args, txt_color='grey', txt_attr=[], **kargs):
        if LogControl.LOG_LEVEL & OK:
            tag_print('√', *args,  tag_color='green', tag_attr=['bold'],  txt_color=txt_color, txt_attr=txt_attr, **kargs)

    @staticmethod
    def fail(*args, txt_color='grey', txt_attr=[], **kargs):
        if LogControl.LOG_LEVEL & FAIL:
            tag_print('X', *args,  tag_color='red', tag_attr=['bold'],  txt_color=txt_color, txt_attr=txt_attr, **kargs)
