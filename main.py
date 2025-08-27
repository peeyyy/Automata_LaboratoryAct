# Laboratory 1 (Activity 1)
def automatalab1(input_string):
    current_state = start_state1
    for symbol in input_string:
        if (current_state, symbol) not in transitions:
            return "Rejected"
        current_state = transitions[(current_state, symbol)]
    if current_state in acceptingState1:
        return "Accepted"
    return "Rejected"

states = {'a', 'b', 'goal'}
alphabet = {'0','1'}
transitions = {
    ('a', '0'): 'a',
    ('a', '1'): 'b',
    ('b', '0'): 'goal',
    ('b', '1'): 'a',
    ('goal', '0'): 'b',
    ('goal', '1'): 'goal'
}
start_state1 = 'a'
acceptingState1 = {'goal'}

print("Activity 1:")
# 3 Accepted
print("Accepted Strings: ")
print(f"1. ('1001101'): {automatalab1('1001101')}")
print(f"2. ('1011010101'): {automatalab1('1011010101')}")
print(f"3. ('10000000'): {automatalab1('10000000')}")

# 3 Rejected
print("Rejected Strings: ")
print(f"1. ('10011'): {automatalab1('10011')}")
print(f"2. ('1011000'): {automatalab1('1011000')}")
print(f"3. ('1010'): {automatalab1('1010')}")



# Laboratory 1 (Activity 2)
def automatalab2(input_string):
    current_state = start_state2
    for symbol in input_string:
        if (current_state, symbol) not in transitions2:
            return "Rejected"
        current_state = transitions2[(current_state, symbol)]
    if current_state in acceptingState2:
        return "Accepted"
    return "Rejected"

states2 = {'q0', 'q1', 'q2', 'q3'}
alphabet2 = {'a','b'}
transitions2 = {
    ('q0', 'a'): 'q1',
    ('q0', 'b'): 'q2',
    ('q1', 'a'): 'q0',
    ('q1', 'b'): 'q3',
    ('q2', 'a'): 'q3',
    ('q2', 'b'): 'q0',
    ('q3', 'a'): 'q2',
    ('q3', 'b'): 'q1'
}
start_state2 = 'q0'
acceptingState2 = {'q0', 'q3'}


print("\nActivity 2:")
# 3 Accepted
print("Accepted Strings: ")
print(f"1. ('aababb'): {automatalab2('aababb')}")
print(f"2. ('bbbaaabb'): {automatalab2('bbbaaabb')}")
print(f"3. ('aaaabbba'): {automatalab2('aaaabbba')}")

# 3 Rejected
print("Rejected Strings: ")
print(f"1. ('bba'): {automatalab2('bba')}")
print(f"2. ('aba'): {automatalab2('aba')}")
print(f"3. ('babab'): {automatalab2('babab')}")