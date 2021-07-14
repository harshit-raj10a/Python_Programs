"""
We can do it by converting the unsorted array into binary search tree. 
rule of BST:-{In this tree every left elemten of the node will be less than the node value and every right value will be greater 
than the node value.}
After converting it into BST we'll apply Inorder traversal on the tree and finally get the sorted array (in this program I've done inorder 
traversal usin recursion so can't store it in different array, for storing sorted element into an array we need to use stack).
And finally we'll print the sorted element uing inorder traversal.
"""

class binary:
  def __init__(self,data):
    self.data=data
    self.left=None
    self.right=None


class tree:
  def __init__(self):
    self.root=None


def insert(val,temp):      #Inserting element in binary tree according to rule of BST
  #print("val = ",val)
  if temp==None:
    #print(temp)
    temp=binary(val)
    #print("in if",temp.data)
  elif temp.data>val:
    #print("in less",temp.data)
    temp.left=insert(val,temp.left)
  elif temp.data<=val:
    #print("in more",temp.data)
    temp.right=insert(val,temp.right)
  return temp


def inorder(temp): #performing Inorder traversal
  if temp==None:
    return
  inorder(temp.left)
  print(temp.data,end=" ")
  inorder(temp.right)


a=[4,3,6,7,33,22,6,5,7,12,34,56,62,16,88,45,98]
bst=tree()
bst.root=binary(a[0])
temp=bst.root
for i in range(1,len(a)): #converting array into BST
  insert(a[i],temp)
inorder(temp)
