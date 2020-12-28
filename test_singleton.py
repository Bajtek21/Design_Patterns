from singleton import Singleton


def test_singleton_init():
    singleton = Singleton()
    assert singleton


def test_three_singleton():
    uniq_id = []
    obj = []
    for i in range(100):
        obj.append(Singleton())
        if id(obj[i]) not in uniq_id:
            uniq_id.append(id(obj[i]))

    assert len(uniq_id) == 3