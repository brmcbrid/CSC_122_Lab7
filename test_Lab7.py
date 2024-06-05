# Tests for Lab7
# Substitution Cipher

import os.path
import sys
from Lab7 import main
from tud_tests import *

def test_Lab7():

    try:
        exists = os.path.exists("Lab7.py")
        assert exists == True
    except:
        sys.exit()

    # Test 1
    set_keyboard_input(["zebra","}heud"])
    main()
    output = get_display_output()

    assert output == [
        "Enter the message to be encrypted: ",
        "Encrypted message = }heud\n",
        "Enter the cipher to be decrypted: ",
        "Decrypted message = zebra\n"
        ]
