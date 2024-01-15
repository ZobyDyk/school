import xml.etree.ElementTree as ET

class Employee:
    def __init__(self, name, position, branch):
        self.name = name
        self.position = position
        self.branch = branch

class EmployeeDatabase:
    def __init__(self):
        try:
            self.tree = ET.parse('employees.xml')
            self.root = self.tree.getroot()
        except FileNotFoundError:
            self.root = ET.Element('employees')
            self.tree = ET.ElementTree(self.root)
            self.save()

    def save(self):
        try:
            self.tree.write('employees.xml')
        except Exception as e:
            print(f"Chyba při ukládání souboru: {e}")

    def create_branch(self, name):
        if not self.root.find(f"./branch[@name='{name}']"):
            ET.SubElement(self.root, 'branch', name=name)
            self.save()
            print(f"Pobočka '{name}' byla vytvořena.")
        else:
            print(f"Pobočka '{name}' již existuje.")

    def list_branches(self):
        return [branch.get('name') for branch in self.root.findall('branch')]

    def create_position(self, position_name):
        if not self.root.find(f"./position[@name='{position_name}']"):
            for branch in self.root.findall('branch'):
                ET.SubElement(branch, 'position', name=position_name)
            self.save()
            print(f"Pozice '{position_name}' byla vytvořena pro všechny pobočky.")
        else:
            print(f"Pozice '{position_name}' již existuje.")

    def list_positions(self):
        positions = set()
        for branch in self.root.findall('branch'):
            for position in branch.findall('position'):
                positions.add(position.get('name'))
        return list(positions)

    def add_employee(self, branch_name, position_name, employee_name):
        branch = self.root.find(f"./branch[@name='{branch_name}']")
        if branch is not None:
            position = branch.find(f"./position[@name='{position_name}']")
            if position is not None:
                if not any(employee.text == employee_name for employee in position.findall('employee')):
                    ET.SubElement(position, 'employee', name=employee_name)
                    self.save()
                    print(f"Zaměstnanec '{employee_name}' byl přidán na pozici '{position_name}' v pobočce '{branch_name}'.")
                else:
                    print(f"Zaměstnanec '{employee_name}' již existuje na pozici '{position_name}'.")
            else:
                print(f"Pozice '{position_name}' neexistuje v pobočce '{branch_name}'.")
        else:
            print(f"Pobočka '{branch_name}' neexistuje.")

    def list_employees(self):
        employees = []
        for branch in self.root.findall('branch'):
            branch_name = branch.get('name')
            for position in branch.findall('position'):
                position_name = position.get('name')
                for employee in position.findall('employee'):
                    employees.append(Employee(employee.get('name'), position_name, branch_name))
        return employees

    # Metody pro správu zaměstnanců
    # TODO: Implementujte tyto metody podle vašich specifikací

# Funkce pro zobrazení a ovládání hlavního menu
def main_menu(database):
    while True:
        print("\nHlavní menu")
        print("1. Vytvořit pobočku")
        print("2. Vytvořit pozici")
        print("3. Přidat zaměstnance")
        print("4. Zobrazit pobočky")
        print("5. Zobrazit pozice")
        print("6. Zobrazit zaměstance")
        print("0. Konec programu")
        choice = input("Zvolte možnost: ")

        if choice == '1':
            branch_name = input("Zadejte název pobočky: ")
            database.create_branch(branch_name)

        elif choice == '2':
            position_name = input("Zadejte název pozice: ")
            database.create_position(position_name)

        elif choice == '3':
            branch_name = input("Zadejte název pobočky, kde zaměstnanec pracuje: ")
            if branch_name in database.list_branches():
                position_name = input("Zadejte název pozice zaměstnance: ")
                if position_name in database.list_positions():
                    employee_name = input("Zadejte jméno zaměstnance: ")
                    database.add_employee(branch_name, position_name, employee_name)
                else:
                    print("Zadaná pozice neexistuje.")
            else:
                print("Zadaná pobočka neexistuje.")

        elif choice == '4':
            print("Seznam poboček:")
            for branch in database.list_branches():
                print(branch)

        elif choice == '5':
            print("Seznam pozic:")
            for position in database.list_positions():
                print(position)

        elif choice == '6':
            print("Seznam zaměstnanců:")
            employees = database.list_employees()
            for emp in employees:
                print(f"{emp.name} - {emp.position} - {emp.branch}")

        elif choice == '0':
            break

        else:
            print("Neplatná volba, zkuste to znovu.")

# Hlavní spouštěcí bod programu
if __name__ == '__main__':
    db = EmployeeDatabase()
    main_menu(db)
