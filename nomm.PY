def divide_numbers():
    try:
        num1=float(input("Ievadiet pirmo skaitli: "))
        num2=float(input("Ievadiet pirmo skaitli: "))
        result=num1 / num2
        print(f"Rezultāts: {result}") 
    except ZeroDivisionError:
        print("Nijuhai bebru ZeroDivisionError")
    except ValueError:
        print("Nijuhai bebru ValueError")
    except Exception as e:
        print("Nijuhai bebru Exception")
    finally:
        print("This is end")

divide_numbers()