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


# csv in class
def addcsvRow(info_list: list, filename: str = "employees.csv"):
    f = open(filename, mode='a', newline='')
    csv.writer(f).writerow(info_list)
    f.close()


def addEmployee(employee_informations: list):
    name = employee_informations[0]
    date_of_birth = employee_informations[1]
    salary = employee_informations[2]
    bonus = employee_informations[3]
    email = employee_informations[4]
    if int(salary) < 0:
        raise Exception("Salary must be positive")
    if int(bonus) < 0:
        raise Exception("Bonus must be positive")
    if '@' not in email:
        raise Exception('Must be a valid email')
    addcsvRow([name, date_of_birth, salary, bonus, email])
    print("successfully added employee")


def change_database_field(filename: str, column_name: str, left_row: str, right_row: str, newfield):
    file = pandas.read_csv(filename)
    file.loc[file[column_name] == left_row, right_row] = newfield
    file.to_csv(filename, index=False)


def changeEmployeeSalary(name: str, new_salary: int):
    if new_salary < 0:
        raise Exception("Salary must be positive")
    change_database_field("employees.csv", "name", name, "salary", new_salary)


def changeEmployeeBonus(name: str, new_bonus: int):
    if new_bonus < 0:
        raise Exception("Salary must be positive")
    change_database_field("employees.csv", "name", name, "bonus", new_bonus)


def changeEmployeeDOB(name: str, new_DOB: int):
    change_database_field("employees.csv", "name", name, "date_of_birth", new_DOB)


if __name__ == "__main__":
    changeEmployeeSalary('Citlaly', 303030)
    changeEmployeeBonus('Justin', 0)
    changeEmployeeDOB('Pham', '24/10-1960')
    addcsvRow(['Bob2', '24/1-1922', str(3000), str(100), 'somemail@ss.com'])
