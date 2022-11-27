from hello.hello_f_test import get_val

def test_get_val_first():
    assert get_val(key='hello', collection={"hello": "world"}) == 'world'


def test_get_val_second():
    assert get_val(key='hello', collection={"hello": "world"}, default='python') == 'world'


def test_get_val_emp():
    assert get_val(key='hello', default='python', collection={}) == 'python'

