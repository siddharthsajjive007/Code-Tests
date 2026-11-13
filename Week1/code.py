
import os

def num_of_steps(mpp,capacity):
    number_of_plants = len(mpp)
    full_capacity = capacity
    current_capacity = full_capacity
    step = 0
    for i in range(number_of_plants):
        if i == 0:
            current_capacity -= mpp[i]
        elif mpp[i] <= current_capacity:
            current_capacity -= mpp[i]
            step += 1
            continue
        else: 
            current_capacity = full_capacity
            step += 2*i 
            current_capacity -= mpp[i]
            step += 1

    return step


filepath =  "C:/Users/siddh/Downloads/Week-1/Week-1/data_input.txt"
correct = 0
num_exp=0
with open("evaluation_cases.txt", "r") as file:
    
    
    for line in file:
        num_exp+=1
        # Split the line using |
        parts = line.strip().split("|")
        # Extract the three values
        input_list = eval(parts[0])
        input_number = int(parts[1])
        expected_output = int(parts[2])

        # print("Input list:", input_list)
        # print("Input number:", input_number)
        # print("Expected output:", expected_output)

        steps = num_of_steps(input_list , input_number)

        if steps == expected_output:
            correct += 1

    if num_exp == correct :
        print(f"All {correct}/{num_exp} correct")
    else:
        print(f"Only {correct}/{num_exp} correct")
        
    



# # mpp = moisture required per plant
# mpp1 = [5,8,9,3,8,9,4,2,10,11,4,14,14,12,5,14,13,9,11,14,13,12,9,11,3,3,6,1,1,14]
# capacity1 = 14
# mpp2 = [13,11,3,13,14,1,7,9,10,2,6,1,15,3,14,11,1,13,3,4,1,9] 
# capacity2 = 34
# mpp3 = [14,15,14,10,4,10,11,12,2,12,8,4,15,2,4,1,12,6,5,14,3,7,12,12]
# capacity3 = 32


