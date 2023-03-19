# python3


def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    n = len(data)
    for i in range(x//2, -1, -1):
        siftdown(i, n, data, swaps)

    return swaps
def siftdown(x, n, data, swaps):
    minind = i
    y = 2*i +1
    if y<x and data[y] < data[minind]:
        minind = y
    z = 2*i +2
    if z< n and data[y] < data[minind]:
        minind = z
    if i != minind:
        data[i], data[minind] = data[minind], data[i]
        swaps.append((i, minind))
        siftdown(minind, data, swaps)
        
        
    

def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    try:
        userinput = input("Input I for keyboard input or F for file input -> ")
        if userinput.startswith('I'):
            n = int(input(""))
            data = list(map(int, input().split()))
        elif userinput.startswith('F'):
            file = "tests/"+ input("Input file name -> ")
            with open(file, 'r') as f:
                n = int(f.readline())
                data = list(map(int, f.readline().split()))
                
    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)
except exception as e:
    print(f"Error")
    return


if __name__ == "__main__":
    main()
