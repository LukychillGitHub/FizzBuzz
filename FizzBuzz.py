for i in range(1, 101):  # El rango debe ser del 1 al 100
  if i % 15 == 0:
    print("FizzBuzz")
  elif i % 3 == 0:
    print("Fizz")
  elif i % 5 == 0:
    print("Buzz")
  else:
    print(i)