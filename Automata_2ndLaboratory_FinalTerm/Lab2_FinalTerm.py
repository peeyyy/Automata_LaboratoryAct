from tabulate import tabulate

# --------------------------------------
# Mealy Machine definition
# --------------------------------------
mealy_machine = {
    'A': {'0': ('A', 'A'), '1': ('B', 'B')},
    'B': {'0': ('C', 'A'), '1': ('D', 'B')},
    'C': {'0': ('D', 'C'), '1': ('B', 'B')},
    'D': {'0': ('B', 'B'), '1': ('C', 'C')},
    'E': {'0': ('D', 'C'), '1': ('E', 'C')}
}

# --------------------------------------
# Mealy → Moore Machine conversion
# --------------------------------------
def convert_mealy_to_moore(mealy_machine):
    moore_states = {}
    for state, transitions in mealy_machine.items():
        for inp, (next_state, output) in transitions.items():
            moore_state = f"{next_state}_{output}"
            if moore_state not in moore_states:
                moore_states[moore_state] = {'output': output, 'transitions': {}}
            for symbol in ['0', '1']:
                if symbol in mealy_machine[next_state]:
                    ns, no = mealy_machine[next_state][symbol]
                    moore_states[moore_state]['transitions'][symbol] = f"{ns}_{no}"
    return moore_states

# --------------------------------------
# Process Mealy Machine
# --------------------------------------
def trace_mealy(machine, start_state, input_string):
    current_state = start_state
    trace = []
    for bit in input_string:
        next_state, out = machine[current_state][bit]
        trace.append([current_state, bit, next_state, out])
        current_state = next_state
    return trace

# --------------------------------------
# Process Moore Machine
# --------------------------------------
def trace_moore(machine, start_state, input_string):
    current_state = start_state
    trace = [[current_state, '-', machine[current_state]['output']]]
    for bit in input_string:
        next_state = machine[current_state]['transitions'][bit]
        trace.append([next_state, bit, machine[next_state]['output']])
        current_state = next_state
    return trace


# --------------------------------------
# Main Program
# --------------------------------------
def main():
    moore_machine = convert_mealy_to_moore(mealy_machine)

    # Default test inputs
    test_inputs = ["00110", "11001", "1010110", "101111"]

    for i in test_inputs:
        print(f"\n📘 Mealy Machine Trace for Input: {i}")
        mealy_trace = trace_mealy(mealy_machine, 'A', i)
        print(tabulate(mealy_trace, headers=["Current State", "Input", "Next State", "Output"], tablefmt="grid"))

        print(f"\n📗 Moore Machine Trace for Input: {i}")
        moore_trace = trace_moore(moore_machine, "A_A", i)
        print(tabulate(moore_trace, headers=["State", "Input", "Output"], tablefmt="grid"))

    # --------------------------------------
    # The user can input their own strings here
    # --------------------------------------
    while True:
        user_input = input("\nNow, you can try input your own strings:\nEnter your own input string (0s and 1s only, or 'exit' to quit): ").strip()
        if user_input.lower() == 'exit':
            print("Thanks for trying this program. Program ended. Goodbye!")
            break

        if not all(ch in '01' for ch in user_input):
            print("⚠️ Invalid input. Please enter only 0s and 1s.")
            continue

        print(f"\n📘 Mealy Machine Trace for Input: {user_input}")
        mealy_trace = trace_mealy(mealy_machine, 'A', user_input)
        print(tabulate(mealy_trace, headers=["Current State", "Input", "Next State", "Output"], tablefmt="grid"))

        print(f"\n📗 Moore Machine Trace for Input: {user_input}")
        moore_trace = trace_moore(moore_machine, "A_A", user_input)
        print(tabulate(moore_trace, headers=["State", "Input", "Output"], tablefmt="grid"))


# Run the program
if __name__ == "__main__":
    main()
