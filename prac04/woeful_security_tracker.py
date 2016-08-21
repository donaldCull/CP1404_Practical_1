__author__ = 'Donald Cull'
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username_entry = input("what is your username: ")
if username_entry in usernames:
    print("Access granted")
else:
    print("Access denied")

