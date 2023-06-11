from script import addition


def test_add():
    subj = addition(2, 3)
    assert subj == 5
