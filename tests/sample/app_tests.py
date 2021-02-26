from app import hello_world


def test_hello_world():
    sut = hello_world()
    assert sut == "Hello, World!"