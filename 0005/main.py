def remove_repeated_data(data):
    num_elements_in_data = len(data)
    if(num_elements_in_data == 0):
        return data
    unique_data = []
    unique_data.append(data[0])
    for i in range(1, num_elements_in_data):
        num_elements_in_unique_data = len(unique_data)
        data_is_unique = True
        for j in range(0, num_elements_in_unique_data):
            if(data[i] == unique_data[j]):
                data_is_unique = False
                break
        if(data_is_unique == True):
            unique_data.append(data[i])
    return unique_data

#if "a" is a subset of "S", return True
#if "a" is not a subset of "S", return False
#"a" is the event
#"S" is the sample space
def a_is_subset_of_S(a, S):
    a_unique = remove_repeated_data(a)
    S_unique = remove_repeated_data(S)
    num_elements_in_a_unique = len(a_unique)
    num_elements_in_S_unique = len(S_unique)
    for i in range(0, num_elements_in_a_unique):
        current_value_is_in_S = False
        for j in range(0, num_elements_in_S_unique):
            if(a_unique[i] == S_unique[j]):
                current_value_is_in_S = True
                break
        if(current_value_is_in_S == False):
            return False
    return True

#a = event a in S
#b = event b in S
#S = sample space S
def get_probability_of_event(event, sample_space):
    if(a_is_subset_of_S(event, sample_space) == False):
        print("The event is not a subset of the sample space.")
        return None
    return len(event)/len(sample_space)

#returns an array of elements that are in both "a" and "b" at the same time
def get_a_AND_b(a, b):
    a_new = remove_repeated_data(a)
    b_new = remove_repeated_data(b)
    num_elements_in_a_new = len(a_new)
    num_elements_in_b_new = len(b_new)
    a_AND_b = []
    for i in range(0, num_elements_in_a_new):
        for j in range(0, num_elements_in_b_new):
            if(a_new[i] == b_new [j]):
                a_AND_b.append(a_new[i])
                break
    return a_AND_b

#a = event a in S
#b = event b in S
#S = sample space S
def get_probability_of_a_AND_b(a, b, S):
    if(a_is_subset_of_S(b, S) == False):
        print("b is not a subset of S")
        return None
    if(a_is_subset_of_S(a, S) == False):
        print("a is not a subset of S")
        return None
    a_AND_b = get_a_AND_b(a, b)
    return len(a_AND_b)/len(S)

def check_if_a_and_b_are_mutually_exclusive(a, b):
    a_AND_b = get_a_AND_b(a, b)
    if(len(a_AND_b) == 0): #a and b are mutually exclusive  
        return True
    else: #a and b are not mutually exclusive
        return False
    
S = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = [1, 2, 3, 4, 5] 
b = [4, 5, 6, 7, 8]
c = [7, 9]

print("a:", a)
print()
print("b:", b)
print()
print("c:", c)
print()

prob_a = get_probability_of_event(a, S) #probability of event a
print("prob_a:", prob_a)
print()

prob_b = get_probability_of_event(b, S) #probability of event b
print("prob_b:", prob_b) 
print()

prob_c = get_probability_of_event(c, S) #probability of event c
print("prob_c:", prob_c) 
print()

a_AND_b = get_a_AND_b(a, b)
print("a_AND_b:", a_AND_b)
print()

prob_a_AND_b = get_probability_of_event(a_AND_b, S)
print("prob_a_AND_b:", prob_a_AND_b)
print()

a_AND_c = get_a_AND_b(a, c)
print("a_AND_c:", a_AND_c)
print()

prob_a_AND_c = get_probability_of_event(a_AND_c, S)
print("prob_a_AND_c:", prob_a_AND_c)
print()

a_AND_b_are_mutually_exclusive = check_if_a_and_b_are_mutually_exclusive(a, b)
if(a_AND_b_are_mutually_exclusive == True):
    print("a and b are mutually exclusive")
    print()
else:
    print("a and b are not mutually exclusive")
    print()

a_AND_c_are_mutually_exclusive = check_if_a_and_b_are_mutually_exclusive(a, c)
if(a_AND_c_are_mutually_exclusive == True):
    print("a and c are mutually exclusive")
    print()
else:
    print("a and c are not mutually exclusive")
    print()
