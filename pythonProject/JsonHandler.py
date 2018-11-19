import json


class JsonHandler:

    def default_write_employees(self):
        data = {'employees': []}
        data['employees'].append({
            'name': 'Scott',
            'date_of_birth': '24/3-1980',
            'salary': '1000',
            'bonus': '100'
        })
        data['employees'].append({
            'name': 'Larry',
            'date_of_birth': '12/4-1960',
            'salary': '2000',
            'bonus': '300'
        })
        data['employees'].append({
            'name': 'Tim',
            'date_of_birth': '13/1-1997',
            'salary': '3000',
            'bonus': '300'
        })

        with open('employees.json', 'w') as outfile:
            json.dump(data, outfile, indent=4)

    def add_employee(self, name: str, date_of_birth: str, salary: str, bonus: str):
        information = {
            'name': name,
            'date_of_birth': date_of_birth,
            'salary': salary,
            'bonus': bonus
        }

        with open('employees.json') as json_file:
            data = json.load(json_file)
        data['employees'].append(information)
        with open('employees.json', 'w') as json_file:
            json.dump(data, json_file, indent=4)

    def read_employees(self):
        with open('employees.json') as json_file:
            data = json.load(json_file)
            for dictionary in data['employees']:
                print('Name: ' + dictionary['name'])
                print('Date of Birth: ' + dictionary['date_of_birth'])
                print('Salary: ' + dictionary['salary'])
                print('Bonus: ' + dictionary['bonus'])
                print('')
        print(data)
        return data
