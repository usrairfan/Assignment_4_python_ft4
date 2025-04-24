for outer in range(1, 7): #outer loop
    print(f"Multiplication table for {outer}:")
    for inner in range(1, 7): # nested inner loop
        print(f"{outer} * {inner} = { outer * inner}")
    print() # Add a blank  line after each row