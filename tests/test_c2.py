import random
from caeser.caeser import * 


def test_cipher():
    pins = [
        "azy",
        "MANAR" ,
        "MANAR LIKES FOOTBALL9"
  
    ]
    
    actual = []
    for pin in pins:
        key = random.randint(1, 26)
        encrypted_pin = encrypt2(pin, key)
        decrypted_pin = decrypt(encrypted_pin,key)
        actual.append(decrypted_pin)
    expected = [ "azy",
        "MANAR" ,
        "MANAR LIKES FOOTBALL9"]
    assert actual == expected

def test_cipher_cracker():
    word =  "It was ,the best"
    key = random.randint(1, 26)
    encrypted = encrypt2(word, key)
    actual = decrypt_without_key(encrypted)
    expected = word

  
  
    assert actual == expected