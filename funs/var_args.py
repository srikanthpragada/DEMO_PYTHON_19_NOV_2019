# keyword only arguments
def process(*, a, b):
    pass


process(b=10, a=20)


def wish(*names, msg="Hello"):
    for n in names:
        print(msg, n)


wish("Tim", "Bill", "Larry")
wish("Ellison", "Elon", msg='Good Morning')
