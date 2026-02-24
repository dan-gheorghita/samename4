```python
def spam():
    # Attempt to print a variable that hasn't been defined yet
    print(eggs)  # ERROR!
    # Define a local variable called 'eggs'
    eggs = 'spam local'

# Define a global variable called 'eggs'
eggs = 'global'
# Call the function 'spam', which will attempt to print the undefined variable 'eggs'
spam()
```