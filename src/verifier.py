'''
if output is given as:

1 2
2 3
3 1

'''

'''
(a) Checks validity: each hospital and each student is matched to exactly one partner, with no duplicates.

1. create two empty sets
2. loop through each row in output
3. add h to first set, add s to second set
4. if already exists in either set, then not valid
5. else return valid
'''

'''
(b) Checks stability: confirms there is no blocking pair.

- would have to look through both input and output files
- ??
'''

from matching_algo import main

hospital_pref, student_pref, assignements = main()
print(type(assignements[0]))

def valid_matching(assignments):
  # create two empty sets
  h_set = set()
  s_set = set()

  # loop through each tuple in assignments
  for (h, s) in assignments:
    # if h or s already exists in their respective set --> duplicate --> invalid
    if h in h_set or s in s_set:
      return False
    # else, add h and s to their respective sets
    else:
      h_set.add(h)
      s_set.add(s)
  return True

def main():
  is_valid = valid_matching(assignements)
  print("VALID") if is_valid else print("INVALID")

if __name__ == "__main__":
  main()