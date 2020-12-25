from singleton import Singleton


def test_singleton_init():
    singleton = Singleton()
    assert singleton


def test_two_singleton_has_same_id_class():
    singleton1 = Singleton()
    singleton2 = Singleton()

    assert id(singleton1) == id(singleton2)