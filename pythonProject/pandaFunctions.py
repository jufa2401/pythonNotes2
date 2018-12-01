import pandas, csv


def sortUsersDesc():
    names = pandas.read_csv("users.csv")
    asc_names = names.sort_values("name", ascending=True)
    asc_names.to_csv("userssorted.csv", index=False)
    print("Written to file!")
    print("Displaying....")


def sortUsersAsc():
    names = pandas.read_csv("users.csv")
    desc_names = names.sort_values("name", ascending=False)
    desc_names.to_csv("userssorted.csv", index=False)
    print("Written to file!")
    print("Displaying....")


def add_database_row(filename: str, name: str, date_of_birth: str, salary: int, bonus: int):
    file = pandas.read_csv(filename)
    # file.loc[file[column_name] == left_row, right_row] = newfield

    file.to_csv(filename, mode='a', index=False, header=False)


# csv in class
def writeInClassExercise3(infoList: list, filename: str = "default.csv"):
    f = open(filename, mode='a', newline='')
    csv.writer(f).writerow(infoList)
    f.close()


def change_database_field(filename: str, column_name: str, left_row: str, right_row: str, newfield):
    file = pandas.read_csv(filename)
    file.loc[file[column_name] == left_row, right_row] = newfield
    file.to_csv(filename, index=False)


def changeEmployeeSalary(name: str, new_salary: int):
    change_database_field("employees.csv", "name", name, "salary", new_salary)


def changeEmployeeBonus(name: str, new_bonus: int):
    change_database_field("employees.csv", "name", name, "bonus", new_bonus)


def changeEmployeeDOB(name: str, new_DOB: int):
    change_database_field("employees.csv", "name", name, "date_of_birth", new_DOB)


changeEmployeeSalary('Citlaly', 303030)
changeEmployeeBonus('Justin', 0)
changeEmployeeDOB('Pham','24/10-1960')
