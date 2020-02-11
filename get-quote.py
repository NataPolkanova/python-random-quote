import random
def main_proc():
  #  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = 13
  numb = random.randint(0,13)
  print(quotes[numb])

if __name__== "__main__":
  main_proc()
