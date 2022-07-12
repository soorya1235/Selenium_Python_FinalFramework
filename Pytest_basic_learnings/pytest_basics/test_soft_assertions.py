actualtitle = "gmail.com"
expectedtitle = "google.com"
title = "This is gmail website"


#assert actualtitle == expectedtitle,"Acutal/Exepcted did not match"
assert "gmails" in title,"Gmail does not exist in title"
try:
    assert  False,"10 is greater than 9"
except AssertionError as e:
    print(e)

assert 10<1,"Ten is less than 1"