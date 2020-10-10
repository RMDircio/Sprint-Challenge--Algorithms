#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The worse case Big O here is O(n) 
```python 
   a = 0 # O(1)
    while (a < n * n * n): # O(n)
      a = a + n * n # O(n)
```

b) The worse case Big O here is O(n^2)
```python
    sum = 0 # O(1)
    for i in range(n): # O(n)
      j = 1 # O(1)
      while j < n: # O(j * n)
        j *= 2 # O(1)
        sum += 1 # O(1)
```

c) The worse case Big O here is O(n) 
```python
    def bunnyEars(bunnies): # O(1)
      if bunnies == 0: # O(1)
        return 0 # O(1)

      return 2 + bunnyEars(bunnies-1) # O(1)
```

## Exercise II


I think the question is asking how would I find out what floor 'f' actually is, while breaking as little eggs as possible. 

First guess is to do a binary tree. I would choose a random number since the building can be 'n' stories tall. The left node would be 'Does not Break = True' and the right node would be 'Does not Break = False'. I would do a depth traversal to see exactly where the breaking ends and starts on the next highest floor. 