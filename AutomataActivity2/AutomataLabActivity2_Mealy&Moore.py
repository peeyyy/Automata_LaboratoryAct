# Mealy and Moore Machines with OOP

class MealyMachine:
    def __init__(self):
        self.state = 'A'

    def transition(self, input_symbol):
        prev_state = self.state
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

        return prev_state, input_symbol, self.state, output

    def process(self, input_string, visualize=True):
        self.state = 'A'
        output = ''
        steps = []

        for symbol in input_string:
            prev, inp, next_state, out = self.transition(symbol)
            output += out
            steps.append((prev, inp, next_state, out))

        if visualize:
            print("\n=== Mealy Machine ===")
            print(f"{'Prev':<6} {'Input':<6} {'Next':<6} {'Output':<7}")
            print("-" * 30)
            for s in steps:
                print(f"{s[0]:<6} {s[1]:<6} {s[2]:<6} {s[3]:<7}")
            print("-" * 30)
            print(f"Final Output: {output}\n")

        return output


class MooreMachine:
    def __init__(self):
        self.state = 'A'
        self.output_map = {'A': 'b', 'B': 'b', 'C': 'a'}

    def transition(self, input_symbol):
        prev_state = self.state
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

        next_state = self.state
        output = self.output_map[next_state]
        return prev_state, input_symbol, next_state, output

    def process(self, input_string, visualize=True):
        self.state = 'A'
        output = ''
        steps = []

        for symbol in input_string:
            prev, inp, next_state, out = self.transition(symbol)
            output += out
            steps.append((prev, inp, next_state, out))

        if visualize:
            print("\n=== Moore Machine ===")
            print(f"{'Prev':<6} {'Input':<6} {'Next':<6} {'Output':<7}")
            print("-" * 30)
            for s in steps:
                print(f"{s[0]:<6} {s[1]:<6} {s[2]:<6} {s[3]:<7}")
            print("-" * 30)
            print(f"Final Output: {output}\n")

        return output

def main():
    print("Finite State Machine")
    print("===============================")
    print("1. Mealy Machine")
    print("2. Moore Machine")
    print("3. Exit")

    while True:
        choice = input("\nEnter choice (1/2/3): ").strip()

        if choice == '3':
            print("Exiting program. Goodbye and Thank you po!")
            break

        elif choice in ['1', '2']:
            input_string = input("Enter a binary string (0s and 1s only): ").strip()
            if not all(c in '01' for c in input_string):
                print("Invalid input! Please enter only 0s and 1s.")
                continue

            if choice == '1':
                machine = MealyMachine()
                machine.process(input_string, visualize=True)
            else:
                machine = MooreMachine()
                machine.process(input_string, visualize=True)

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
