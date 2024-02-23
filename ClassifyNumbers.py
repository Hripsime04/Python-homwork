def classify_numbers(numbers):
    even=[]
    odd=[]
    for num in numbers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return odd,even
   
u_input = input ("Enter numbers separated by space: ")
input = u_input.split()
numbers = list(map(int, input))
odd, even = classify_numbers(numbers)
print(f"even,{even}")
print(f"odd,{odd}")