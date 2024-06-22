# def sum_tuple(t):
#     return sum(t)

# # Test the function
# t1 = (5, 10, 15)
# print(sum_tuple(t1))  # Output: 30


t1 = (5, 10, 15)
t2 = ('January', 'February', 'March')
t3 = (30, 40)
t4 = ('July', 'August')

print(t1 * 2)      # Output: (5, 10, 15, 5, 10, 15)
print(t2 * 2)      # Output: ('January', 'February', 'March', 'January', 'February', 'March')
print(t1 + t2)     # Output: (5, 10, 15, 'January', 'February', 'March')
print(t1 + t3)     # Output: (5, 10, 15, 30, 40)
print(t3 + t4)     # Output: (30, 40, 'July', 'August')

