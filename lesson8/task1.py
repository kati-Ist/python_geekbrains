class Data:
    def __init__(self, data_string):
        self.data_string = data_string

    @classmethod
    def data_format(cls, data):
        try:
            cls.my_data = list(map(int, data.split('-')))
            print(cls.my_data)
        except ValueError:
            print("В дате должны быть только цифры")

    @staticmethod
    def data_validation(string):
        try:
            my_date = list(map(int, Data(string).data_string.split('-')))
            print(string) if (my_date[0] <= 31 and my_date[1] <= 12) else print("Date is invalid")
        except ValueError:
            print("В дате должны быть только цифры")


a = Data("12-01-2020")
Data.data_format("12-03-2020")
a.data_format("13-04-2020")
a.data_validation("64-06-2020")
