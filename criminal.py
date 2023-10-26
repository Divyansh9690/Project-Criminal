# Sample Criminal Details App

class Criminal:
    def __init__(self, name, age, offenses):
        self.name = name
        self.age = age
        self.offenses = offenses

class CriminalDatabase:
    def __init__(self):
        self.criminals = []

    def add_criminal(self, criminal):
        self.criminals.append(criminal)

    def search_criminal(self, name):
        for criminal in self.criminals:
            if criminal.name == name:
                return criminal
        return None

def main():
    database = CriminalDatabase()

    while True:
        print("Criminal Details App")
        print("1. Add Criminal")
        print("2. Search Criminal")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the name of the criminal: ")
            age = input("Enter the age of the criminal: ")
            offenses = input("Enter offenses (comma-separated): ").split(',')
            criminal = Criminal(name, age, offenses)
            database.add_criminal(criminal)
            print("Criminal added successfully.")

        elif choice == '2':
            name = input("Enter the name of the criminal to search: ")
            criminal = database.search_criminal(name)
            if criminal:
                print("Criminal Details:")
                print(f"Name: {criminal.name}")
                print(f"Age: {criminal.age}")
                print(f"Offenses: {', '.join(criminal.offenses)}")
            else:
                print("Criminal not found.")

        elif choice == '3':
            print("Exiting the app.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
