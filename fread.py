def read_file():
    try:
        filename = input("Ievadiet nosaukumu: ")
        with open(filename, 'r') as file:
            content = file.read()
            print('Faila saturs: ')
            print(content)
    except FileNotFoundError:
        print("Nijuhai bebru FileNotFoundError")
    except PermissionError:
        print("Nijuhai bebru PermissionError")
    except Exception as e:
        print("Nijuhai bebru Exception")
    finally:
        print("Viss pastradai malacit")

read_file()