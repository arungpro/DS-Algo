class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
lc = None
def findLCA(root, v1, v2):
    global lc
    if root == None:
        return
    # if root.info > v1 and root.info <= v2:
    #     lc = root
    
    if root.info > v1 and root.info > v2:
        findLCA(root.left, v1, v2)
    elif(root.info < v1 and root.info < v2):
        findLCA(root.right, v1, v2)
    else:
        lc = root
        return
    
def lca(root, v1, v2):
    global lc
    lc = root
    findLCA(root, v1, v2)
    return lc

tree = BinarySearchTree()
# t = int(input())
t = 9

# arr = list(map(int, input().split()))
# arr = [8, 4, 9, 1, 2, 3, 6, 5]
arr = [8, 6, 5, 7, 11, 12, 13, 10, 9]

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print (ans.info)
