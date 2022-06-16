import numpy as np

x = np.array([1, 2, 3, 4, 5])

# We print x
print()
print('x = ', x)
print()

# Let's access some elements with positive indices
print('This is First Element in x:', x[0]) 
print('This is Second Element in x:', x[1])
print('This is Fifth (Last) Element in x:', x[4])
print()

# Let's access the same elements with negative indices
print('This is First Element in x:', x[-5])
print('This is Second Element in x:', x[-4])
print('This is Fifth (Last) Element in x:', x[-1])


x = np.array([[1,2,3],[4,5,6],[7,8,9]])

print()
print('x = \n',x)
print()

print('This is (0,0) Element in x: ', x[0,0])
print('This is (0,1) Element in x: ', x[0,1])
print('This is (2,2) Element in x: ', x[2,2])


x [0,0] = 20
print('Modified:\n x = \n', x)

x = np.array([1, 2, 3, 4, 5])
y = np.array([[1,2,3],[4,5,6],[7,8,9]])

print()
print('Original x = ',x)



x = np.delete(x,[0,4])

print()
print('modified x = ', x)


print()
print('Original y = \n', y)

w = np.delete(y,0,axis=0)
v = np.delete(y,[0],axis=1)

print()
print('w = \n',w)

print()
print('v =\n',v)

x = np.append(x, [7,8])

print()
print('x =',x)


v = np.append(y,[[7,8,9]],axis=0)
q = np.append(y,[[9],[10],[2]], axis=1)

print()
print('v =\n',v)
print()
print('q = \n',q)


x = np.insert(x,2,[3,4])
print()
print('x =',x)

w = np.insert(y,1,[4,5,6],axis = 0)

v = np.insert(y,1,5, axis=1)

print()
print('w = \n', w)

print()
print('v= \n',v)



x = np.array([1,2])
y = np.array([[3,4],[5,6]])

print()
print('x= ', x)

print()
print('y =\n',y)


z = np.vstack((x,y))

w = np.hstack((y,x.reshape(2,1)))

print()
print('z =\n',z)


print()
print('w =\n',w)




#Slicing

x = np.arange(20).reshape(4,5)

print()
print('x =\n',x)
print()

z = x[1:4,2:5]
print('z =\n',z)

w = x[1:,2:5]
print()
print('w =\n',w)

y = x[:3,2:5]


print()
print('y = \n',y)

v = x[2,:]

print()
print('v =',v)

q = x[:,2]
print()
print('q = ',q)

r = x[:,2:3]

print()
print('r = \n',r)



indices = np.array([1,3])

print('indices = ',indices)
print()

y = x[indices,:]

z = x[:,indices]

print()
print('y = \n',y)

print()
print('z =\n', z)



x = np.arange(25).reshape(5,5)
print('z=', np.diag(x))
print()

print('y=', np.diag(x, k=1))
print()

print('w= ',np.diag(x, k =-1))

#Boolean expression

x = np.arange(25).reshape(5,5)

print()
print('original x =\n', x)
print()

#Using boolean indexing to select elements

print('The elements in x that are greater than 10:', x[x > 10])
print('The elements in x that less than or equal to 7:', x[x<= 7])
print('The elements in x that are between 10 and 17:', x[(x>10) & (x<170)])

x[(x>10) & (x<17)] = -1

print()
print('x =\n',x)
print()


# We create a rank 1 ndarray
x = np.array([1,2,3,4,5])

# We create a rank 1 ndarray
y = np.array([6,7,2,8,4])

# We print x
print()
print('x = ', x)

# We print y
print()
print('y = ', y)

# We use set operations to compare x and y:
print()
print('The elements that are both in x and y:', np.intersect1d(x,y))
print('The elements that are in x that are not in y:', np.setdiff1d(x,y))
print('All the elements of x and y:',np.union1d(x,y))

# We create an unsorted rank 1 ndarray
x = np.random.randint(1,11,size=(10,))

# We print x
print()
print('Original x = ', x)

# We sort x and print the sorted array using sort as a function.
print()
print('Sorted x (out of place):', np.sort(x))

# When we sort out of place the original array remains intact. To see this we print x again
print()
print('x after sorting:', x)

print(np.unique(x))

# We create an unsorted rank 1 ndarray
x = np.random.randint(1,11,size=(10,))

# We print x
print()
print('Original x = ', x)

# We sort x and print the sorted array using sort as a method.
x.sort()

# When we sort in place the original array is changed to the sorted array. To see this we print x again
print()
print('x after sorting:', x)


# We create an unsorted rank 2 ndarray
X = np.random.randint(1,11,size=(5,5))

# We print X
print()
print('Original X = \n', X)
print()

# We sort the columns of X and print the sorted array
print()
print('X with sorted columns :\n', np.sort(X, axis = 0))

# We sort the rows of X and print the sorted array
print()
print('X with sorted rows :\n', np.sort(X, axis = 1))



# Create a 5 x 5 ndarray with consecutive integers from 1 to 25 (inclusive).
X = X = np.arange(1,26).reshape(5,5)

# Use Boolean indexing to pick out only the odd numbers in the array
Y = X[X % 2 != 0]
print()
print('Y: \n',Y)




# We create two rank 1 ndarrays
x = np.array([1,2,3,4])
y = np.array([5.5,6.5,7.5,8.5])

# We print x
print()
print('x = ', x)

# We print y
print()
print('y = ', y)
print()

# We perfrom basic element-wise operations using arithmetic symbols and functions
print('x + y = ', x + y)
print('add(x,y) = ', np.add(x,y))
print()
print('x - y = ', x - y)
print('subtract(x,y) = ', np.subtract(x,y))
print()
print('x * y = ', x * y)
print('multiply(x,y) = ', np.multiply(x,y))
print()
print('x / y = ', x / y)
print('divide(x,y) = ', np.divide(x,y))


# We create two rank 2 ndarrays
X = np.array([1,2,3,4]).reshape(2,2)
Y = np.array([5.5,6.5,7.5,8.5]).reshape(2,2)

# We print X
print()
print('X = \n', X)

# We print Y
print()
print('Y = \n', Y)
print()

# We perform basic element-wise operations using arithmetic symbols and functions
print('X + Y = \n', X + Y)
print()
print('add(X,Y) = \n', np.add(X,Y))
print()
print('X - Y = \n', X - Y)
print()
print('subtract(X,Y) = \n', np.subtract(X,Y))
print()
print('X * Y = \n', X * Y)
print()
print('multiply(X,Y) = \n', np.multiply(X,Y))
print()
print('X / Y = \n', X / Y)
print()
print('divide(X,Y) = \n', np.divide(X,Y))



# We create a rank 1 ndarray
x = np.array([1,2,3,4])

# We print x
print()
print('x = ', x)

# We apply different mathematical functions to all elements of x
print()
print('EXP(x) =', np.exp(x))
print()
print('SQRT(x) =',np.sqrt(x))
print()
print('POW(x,2) =',np.power(x,2)) # We raise all elements to the power of 2


# We create a 2 x 2 ndarray
X = np.array([[1,2], [3,4]])

# We print x
print()
print('X = \n', X)
print()

print('Average of all elements in X:', X.mean())
print('Average of all elements in the columns of X:', X.mean(axis=0))
print('Average of all elements in the rows of X:', X.mean(axis=1))
print()
print('Sum of all elements in X:', X.sum())
print('Sum of all elements in the columns of X:', X.sum(axis=0))
print('Sum of all elements in the rows of X:', X.sum(axis=1))
print()
print('Standard Deviation of all elements in X:', X.std())
print('Standard Deviation of all elements in the columns of X:', X.std(axis=0))
print('Standard Deviation of all elements in the rows of X:', X.std(axis=1))
print()
print('Median of all elements in X:', np.median(X))
print('Median of all elements in the columns of X:', np.median(X,axis=0))
print('Median of all elements in the rows of X:', np.median(X,axis=1))
print()
print('Maximum value of all elements in X:', X.max())
print('Maximum value of all elements in the columns of X:', X.max(axis=0))
print('Maximum value of all elements in the rows of X:', X.max(axis=1))
print()
print('Minimum value of all elements in X:', X.min())
print('Minimum value of all elements in the columns of X:', X.min(axis=0))
print('Minimum value of all elements in the rows of X:', X.min(axis=1))


# We create a rank 1 ndarray
x = np.array([1,2,3])

# We create a 3 x 3 ndarray
Y = np.array([[1,2,3],[4,5,6],[7,8,9]])

# We create a 3 x 1 ndarray
Z = np.array([1,2,3]).reshape(3,1)

# We print x
print()
print('x = ', x)
print()

# We print Y
print()
print('Y = \n', Y)
print()

# We print Z
print()
print('Z = \n', Z)
print()

print('x + Y = \n', x + Y)
print()
print('Z + Y = \n',Z + Y)
