forkbomb = 0

print("fastcount command")
forkstart = input("What do you want to do ")

if forkstart == "fastcount":
  timelimit = int(input("How long "))
  start = input("start with y ")

  if start == "y":
    while forkbomb < timelimit:
      print(forkbomb)
      forkbomb += 1

else:
  print("lmao wow")
