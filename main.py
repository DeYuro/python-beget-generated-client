# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from client.client import Test

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press Ctrl+F8 to toggle the breakpoint.

def test_auth():
    test = Test("dshash1i", "Iddqd3797916")
    test.run()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_auth()
    print_hi('PyCharm')

