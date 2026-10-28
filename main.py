""" A Python program that introduces the head-tail pattern in lists, showing how the first element becomes the head, 
the remaining elements become the tail, and an empty list acts as the base case."""

l = [1,2,5,8,6]

def headTail(list):
    if not list:
        print("Base case reached")

    head = list[0]
    tail = list[1:]

    print(f"Head: {head}")
    print(f"Tail: {tail}")

headTail(l)