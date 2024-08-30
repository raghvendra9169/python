def execute_commands(command):
    try:
        subprocess.run(command.split())
    except Exception:
        print("psh: command not found: {}".format(command))


def main():
    while True:
        command = input("$ ")
        if command == "exit":
            break
        elif command == "help":
            print("psh: a simple shell written in Python")
        else:
            execute_commands(command)

main()