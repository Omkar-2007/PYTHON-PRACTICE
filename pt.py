print("Printing previous number and current number sum in range (10)")
previous_num = 0

for i in range (10):
    x_sum = previous_num + i
    print(f"current num : {i} previous num : {previous_num} sum :{x_sum}")
    previous_num=i
