def calculate_blocks(n):
    number_of_rows = n
    total_pyramid_blocks = 0
    for row in range(number_of_rows):
        total_pyramid_blocks += number_of_rows
        number_of_rows -= 1
        print(number_of_rows)
    print(total_pyramid_blocks, "Total blocks should be 21")


def calculate_blocks_recursively(n):
    if n <= 0:
        return 0
    else:
        return n + calculate_blocks_recursively(n-1)


# calculate_blocks(6)
print(calculate_blocks_recursively(6), "should be 21")
