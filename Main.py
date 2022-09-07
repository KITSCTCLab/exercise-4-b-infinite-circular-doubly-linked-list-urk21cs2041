length_of_circular_linked_list = int(input())
circular_linked_list = list(map(int,input().strip().split(" ")))
actual_list = []
value = 0
while len(actual_list) < length_of_circular_linked_list and value < len(circular_linked_list):
 element = circular_linked_list[value]
 if element not in actual_list:
 actual_list.append(element)
 value += 1
print(len(actual_list))
print(" ".join(str(num) for num in actual_list))
