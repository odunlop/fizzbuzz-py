def generate(upto):
    list = []
    for n in range(1, upto + 1):
      if n % 3 == 0 and n % 5 == 0:
        list.append("FizzBuzz")
      elif n % 3 == 0:
        list.append("Fizz")
      elif n % 5 == 0:
        list.append("Buzz")
      else:
        list.append(str(n))
    string = ', '.join(list)
    return string