class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    my_list = []
    while True:
        user_number = input("Enter a number, for break - enter 'stop': ")
        if user_number == "stop":
            print(my_list)
            raise OwnError("You exit!")
        else:
            try:
                my_list.append(int(user_number))
            except:
                print("Enter something else")
except OwnError as err:
    print(err)
