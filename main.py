arr = [0, 1, 7, 2, 4, 8]
result = sum(arr[i] for i in range(0, len(arr), 2)) * arr[-1] if arr else 0
print(f"Input: {arr}, Result: {result}")

arr = [1, 3, 5]
result = sum(arr[i] for i in range(0, len(arr), 2)) * arr[-1] if arr else 0
print(f"Input: {arr}, Result: {result}")  

arr = [6]
result = sum(arr[i] for i in range(0, len(arr), 2)) * arr[-1] if arr else 0
print(f"Input: {arr}, Result: {result}")  

arr = []
result = sum(arr[i] for i in range(0, len(arr), 2)) * arr[-1] if arr else 0
print(f"Input: {arr}, Result: {result}") 
