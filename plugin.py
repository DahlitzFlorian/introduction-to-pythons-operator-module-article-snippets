# plugin.py
import abc
import operator


class Plugin(abc.ABC):
    @abc.abstractstaticmethod
    def run(self):
        pass


class FirstPlugin(Plugin):
    def run(self):
        print("FirstPlugin here")


class SecondPlugin(Plugin):
    def run(self):
        print("SecondPlugin here")


call_run = operator.methodcaller("run")
call_run(FirstPlugin())
call_run(SecondPlugin())
