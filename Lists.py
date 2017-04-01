output = []
# Allowed commands
whitelist = [
    'insert',
    'remove',
    'append',
    'sort',
    'pop',
    'reverse',
    'print'
]
n = int(input())
for i in range(n):
    # It's either an int or a command.
    args = [int(i) if i not in whitelist else i for i in input().split(' ')]
    # The command is first.
    command = args.pop(0)
    # If 'output' has that command...
    if command in dir(output):
        # call it with the other args
        getattr(output, command)(*args)
    elif command == 'print':
        print(output)
    else:
        raise AttributeError("Somethin' done messed up!")