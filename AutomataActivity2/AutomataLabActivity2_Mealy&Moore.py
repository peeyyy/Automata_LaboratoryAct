# Mealy and Moore Machines with OOP

class MealyMachine:
    def __init__(self):
        self.state = 'A'

    def transition(self, input_symbol):
        output = ''
        if self.state == 'A':
            if input_symbol == '0':
                self.state = 'B'
                output = 'b'
            else:
                self.state = 'A'
                output = 'b'
        elif self.state == 'B':
            if input_symbol == '0':
                self.state = 'B'
                output = 'b'
            else:
                self.state = 'C'
                output = 'a'
        elif self.state == 'C':
            if input_symbol == '0':
                self.state = 'B'
                output = 'b'
            else:
                self.state = 'A'
                output = 'b'
        return output

    def process(self, input_string, visualize=True):
        self.state = 'A'
        steps = []
        output_total = ''

        for symbol in input_string:
            current_state = self.state
            output = self.transition(symbol)
            output_total += output
            steps.append((symbol, current_state, output))

        if visualize:
            print(f"\nMealy Machine - Input: {input_string}")
            print("+-------+-------+--------+")
            print("| Input | State | Output |")
            print("+-------+-------+--------+")
            for s in steps:
                print(f"| {s[0]:<5} | {s[1]:<5} | {s[2]:<6} |")
            print("+-------+-------+--------+")
            print("Result: Accepted\n")

        return output_total

class MooreMachine:
    def __init__(self):
        self.state = 'A'
        self.output_map = {'A': 'b', 'B': 'b', 'C': 'a'}

    def transition(self, input_symbol):
        if self.state == 'A':
            if input_symbol == '0':
                self.state = 'B'
            else:
                self.state = 'A'
        elif self.state == 'B':
            if input_symbol == '0':
                self.state = 'B'
            else:
                self.state = 'C'
        elif self.state == 'C':
            if input_symbol == '0':
                self.state = 'B'
            else:
                self.state = 'A'

    def process(self, input_string, visualize=True):
        self.state = 'A'
        steps = [(None, self.state, self.output_map[self.state])]  # initial output
        output_total = self.output_map[self.state]

        for symbol in input_string:
            self.transition(symbol)
            steps.append((symbol, self.state, self.output_map[self.state]))
            output_total += self.output_map[self.state]

        if visualize:
            print(f"\nMoore Machine - Input: {input_string}")
            print("+-------+-------+--------+")
            print("| Input | State | Output |")
            print("+-------+-------+--------+")
            for s in steps:
                if s[0] is None:
                    print(f"|  -    | {s[1]:<5} | {s[2]:<6} |")
                else:
                    print(f"| {s[0]:<5} | {s[1]:<5} | {s[2]:<6} |")
            print("+-------+-------+--------+")
            print("Result: Accepted\n")

        return output_total

def main():
    print("Finite State Machine")
    print("===============================")
    print("1. Mealy Machine")
    print("2. Moore Machine")
    print("3. Exit")

    while True:
        choice = input("\nEnter choice (1/2/3): ").strip()

        if choice == '3':
            print("Exiting program. Goodbye and thank you po!")
            break

        elif choice in ['1', '2']:
            input_string = input("Enter a binary string (0s and 1s only): ").strip()
            if not all(c in '01' for c in input_string):
                print("Invalid input! Please enter only 0s and 1s.")
                continue

            if choice == '1':
                machine = MealyMachine()
                machine.process(input_string)
            else:
                machine = MooreMachine()
                machine.process(input_string)

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
