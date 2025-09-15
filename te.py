import tempfile
import ext

import dis

gettempdir = lambda: "12"

def gettempdir():pass

template= 1
def mktem(suffix="", prefix=template, dir=gettempdir()):
    pass


def mktemp(suffix="", prefix=template, dir:=gettempdir()):
        pass


print(ext.mktemp.__code__.co_deferedargcount)

def c():
    mktemp(dir="abc", suffix="abc", prefix="abc")
    ext.mktem(dir="abc", suffix="abc", prefix="abc")
    ext.mktemp(dir="abc", suffix="abc", prefix="abc")
    #tempfile.mktemp(dir="abc", suffix="abc", prefix="abc")
    return 42


print(dis.dis(c))

print(c())
