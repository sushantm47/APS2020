import re

def main():
  patt = re.compile(r'[A-Z]')
  string = input()
  print(len(patt.findall(string))+1)

if __name__ == "__main__":
  main()