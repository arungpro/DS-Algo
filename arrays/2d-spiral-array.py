'''
Question 1: 2D Spiral Array
Find the pattern and complete the function:
int[][] spiral(int n);
where n is the size of the 2D array.
Sample Result
input = 3
123
894
765

input = 4
01 02 03 04
12 13 14 05
11 16 15 06
10 09 08 07

input = 8
1  2  3  4  5  6  7  8
28 29 30 31 32 33 34 9
27 48 49 50 51 52 35 10
26 47 60 61 62 53 36 11
25 46 59 64 63 54 37 12
24 45 58 57 56 55 38 13
23 44 43 42 41 40 39 14
22 21 20 19 18 17 16 15
'''
n = 6
toRight = {'x1': 0, 'y1': 0, 'x2': 0, 'y2': n-1}
toBottom = {'x1': 1, 'y1': n-1, 'x2': n-1, 'y2': n-1}
toLeft = {'x1': n-1, 'y1': n-2, 'x2': n-1, 'y2': 0}
toTop = {'x1': n-2, 'y1': 0, 'x2': 1, 'y2': 0}

arr = [[0 for _ in range(n)] for _ in range(n)]
start = 1
stop = n*n
def generateRightToLeft():
    # import pdb;pdb.set_trace()
    print(toRight)
    for i in range(toRight['y1'], toRight['y2']+1):
        global start
        arr[toRight['x1']][i] = start
        start = start + 1
    display()
    print("----")
    toRight['x1'] = toRight['x1'] + 1
    toRight['y1'] = toRight['y1'] + 1
    toRight['x2'] = toRight['x2'] + 1
    toRight['y2'] = toRight['y2'] - 1

def generateTopToBottom():
    # import pdb;pdb.set_trace()
    for i in range(toBottom['x1'], toBottom['x2']+1):
        global start
        arr[i][toBottom['y1']] = start
        start = start + 1
    display()
    print("----")
    toBottom['x1'] = toBottom['x1'] + 1
    toBottom['y1'] = toBottom['y1'] - 1
    toBottom['x2'] = toBottom['x2'] - 1
    toBottom['y2'] = toBottom['y2'] - 1

def generateLeftToRight():
    # import pdb;pdb.set_trace()
    for i in range(toLeft['y1'], toLeft['y2']-1, -1):
        global start
        arr[toLeft['x1']][i] = start
        start = start + 1
    display()
    print("----")
    toLeft['x1'] = toLeft['x1'] - 1
    toLeft['y1'] = toLeft['y1'] - 1
    toLeft['x2'] = toLeft['x2'] - 1
    toLeft['y2'] = toLeft['y2'] + 1

def generateBottomToTop():
    # import pdb;pdb.set_trace()
    for i in range(toTop['x1'], toTop['x2']-1, -1):
        global start
        arr[i][toTop['y1']] = start
        start = start + 1
    display()
    print("----")
    toTop['x1'] = toTop['x1'] - 1
    toTop['y1'] = toTop['y1'] + 1
    toTop['x2'] = toTop['x2'] + 1
    toTop['y2'] = toTop['y2'] + 1

def display():
    for i in range(0, n):
        print(arr[i])

def spiralArray():
    # print(toLeft)
    # generateLeftToRight()
    # print(toLeft)
    # generateLeftToRight()
    # print(toLeft)
    while(start <= stop):
        generateRightToLeft() 
        generateTopToBottom()
        generateLeftToRight()
        generateBottomToTop()

spiralArray()