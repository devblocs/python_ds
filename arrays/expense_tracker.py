class Expenses:
    __spends = None
    __months = [
        'january',
        'february',
        'march',
        'april',
        'may',
        'june',
        'july',
        'august',
        'september',
        'october',
        'november',
        'december'
    ]

    def __init__(self, spends: list):
        self.__spends = spends

    def get_spends(self):
        print(self.__spends)

    def compare(self, target_month: str, previous_month: str) -> None:
        if target_month in self.__months and previous_month in self.__months:
            target_value = self.__spends[self.__months.index(target_month)]
            previous_value = self.__spends[self.__months.index(previous_month)]

            if target_value > previous_value:
                diff = target_value - previous_value
                print(f"{target_month} has a higher spending than {previous_month}, with a spending of ${diff}")
            elif target_value < previous_value:
                diff = previous_value - target_value
                print(f"{previous_month} has a higher spending than {target_month}, with a spending of ${diff}")
        else:
            print("Target month or previous month is not in the list. Please check the month values")

    def quarter_wise_expense(self, quarter: int) -> int:
        total_expense = 0

        if quarter == 1:
            quarter_range = 3
        elif quarter == 2:
            quarter_range = 6
        elif quarter == 3:
            quarter_range = 9
        elif quarter == 4:
            quarter_range = 12

        quarter_range = len(self.__spends) if quarter_range > len(self.__spends) else quarter_range

        for index in range(quarter_range):
            total_expense = total_expense + self.__spends[index]

        return total_expense

    def find_amount_spent(self, amount: int) -> None:
        try:
            month = self.__months[self.__spends.index(amount)]
            print(f"${amount} is spent in {month}")
        except ValueError as ve:
            print(f"${amount} not in the expenses list")

    def add_amount(self, month: str, amount: int) -> None:
        if month in self.__months:
            try:
                self.__spends.insert(self.__months.index(month), amount)
            except ValueError as ve:
                print("Month index not available in expenses")

    def add_refund(self, month: str, amount: int):
        if month in self.__months:
            try:
                month_index = self.__months.index(month)
                self.__spends[month_index] = self.__spends[month_index] - amount
            except ValueError as ve:
                print("Month index not available in expenses")


# application starts here

spends = [2200, 2350, 2600, 2130, 2190]

expense = Expenses(spends)
expense.compare('february', 'january')

print(f"Total expense of first quarter: {expense.quarter_wise_expense(1)}")

expense.find_amount_spent(2350)
expense.get_spends()
# expense.add_amount('june', 1980)
expense.add_refund('april', 200)
expense.get_spends()
