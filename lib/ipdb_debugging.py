import ipdb

def plus_two(num):
    num += 2  # Update num to be equal to num + 2
    ipdb.set_trace()  # This will allow you to inspect the value of num in the debugger
    return num  # Return the updated value of num
