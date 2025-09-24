def swap(x, y):
    # Check if both x and y are numeric
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1
    
    # Swap using only x and y
    x = x + y
    y = x - y
    x = x - y
    
    # Print swapped values
    print("x =", x, "y =", y)
