from Zadacha_vtoraya.izm_dict_namest import set_

def test_set_f_eq_one():
    assert set_(path=["a", "b", "c"], coll={"a": {"b": {"c": 3}}}, value=4) ==

def test_set_f_eq_two():
    assert set_(path=['x', 'y', 'z'], coll={"a": {"b": {"c": 4}}}, value=5) ==

def test_set_f_eq_three():
    assert set_(path=["a", "b", "z"], coll={"a": {"b": {"z": 5}}}, value=6) ==
