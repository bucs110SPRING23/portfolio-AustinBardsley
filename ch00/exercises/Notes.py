def foo(x = 9):
  y = x + 1
  return y # ends the function, and goes back to where the function was called
  print("This will never print")

var = foo()  # return here the call when function complete

print(var)