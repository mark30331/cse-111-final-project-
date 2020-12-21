from caesar_cipher import*
import pytest

def test_encrypt():
    assert encrypt("i love to code everyday", 3) == "l oryh wr frgh hyhubgdb"
    assert encrypt("my hobby is to code in python", 6) == "se nuhhe oy zu iujk ot veznut"
    assert encrypt("i am a super programmer", 57) == "n fr f xzujw uwtlwfrrjw"
    

def test_decrypt():
    assert decrypt("l oryh wr frgh hyhubgdb", 3,"love") == "i love to code everyday"
    assert decrypt("se nuhhe oy zu iujk ot veznut", 6, "code") == "my hobby is to code in python" 
    assert decrypt("n fr f xzujw uwtlwfrrjw", 57, "super") == "i am a super programmer"
    


pytest.main(["test_caesar_cipher.py"])
