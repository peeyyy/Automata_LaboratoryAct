from tabulate import tabulate

# --------------------------------------
# Given Mealy Machine Transition Table
# --------------------------------------
mealy_machine = {
    'A': {'0': ('A', 'A'), '1': ('B', 'B')},
    'B': {'0': ('C', 'A'), '1': ('D', 'B')},
    'C': {'0': ('D', 'C'), '1': ('B', 'B')},
    'D': {'0': ('B', 'B'), '1': ('C', 'C')},
    'E': {'0': ('D', 'C'), '1': ('E', 'C')}
}

# --------------------------------------
# Convert Mealy → Moore Machine
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
# Process the Moore Machine
# --------------------------------------
def trace_moore(machine, start_state, input_string):
    current_state = start_state
    trace = [[current_state.replace("_", "/"), '-', machine[current_state]['output']]]
    output_sequence = machine[current_state]['output']

    for bit in input_string:
        next_state = machine[current_state]['transitions'][bit]
        output_sequence += machine[next_state]['output']
        trace.append([next_state.replace("_", "/"), bit, machine[next_state]['output']])
        current_state = next_state

    return trace, output_sequence


# --------------------------------------
# Run the Converted Moore Machine
# --------------------------------------
def main():
    moore_machine = convert_mealy_to_moore(mealy_machine)

    # Default test inputs
    test_inputs = ["00110", "11001", "1010110", "101111"]

    # Process given inputs
    for input_str in test_inputs:
        print(f"\n📗 Moore Machine Trace for Input: {input_str}")
        moore_trace, output_seq = trace_moore(moore_machine, "A_A", input_str)
        print(tabulate(moore_trace, headers=["State", "Input", "Output"], tablefmt="grid"))
        print(f"➡️ Output Sequence: {output_seq}")

    # Allow user to try their own inputs
    while True:
        user_input = input("\nEnter your own input string (0s and 1s only) or type 'exit' to quit: ").strip()
        if user_input.lower() == 'exit':
            print("\nThanks for using this program. Program ended. Goodbye!")
            break

        if not user_input or any(ch not in '01' for ch in user_input):
            print("⚠️ Invalid input. Please enter only 0s and 1s.")
            continue

        print(f"\n📗 Moore Machine Trace for Input: {user_input}")
        moore_trace, output_seq = trace_moore(moore_machine, "A_A", user_input)
        print(tabulate(moore_trace, headers=["State", "Input", "Output"], tablefmt="grid"))
        print(f"➡️ Output Sequence: {output_seq}")


# Run the program
if __name__ == "__main__":
    main()
