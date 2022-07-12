import pytest

def getdata():
    return [
        ("user1","passowrd1"),
        ("user2", "passowrd2"),
        ("user3", "passowrd3")

    ]

@pytest.mark.parametrize("username,password",getdata())
def test_login(username,password):
    print("Username is --------{}",username)
    print("password is --------{}",password)
