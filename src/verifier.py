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

- go through hospital preferences, row by row, pref by pref
- loop through each pref until reaching current match
  - for each pref before current match, check if that student s would prefer this hospital h over their current match h' by going through that student's preference list until reaching their current match h'
    - if that student prefers h over h', then blocking pair found --> unstable
'''

from matching_algo import main

hospital_pref, student_pref, assignments = main()

def valid_matching(assignments):
  # create two empty sets
  h_set = set()
  s_set = set()

  # loop through each tuple in assignments
  for (h, s) in assignments:
    # if h or s already exists in their respective set --> duplicate --> invalid
    if h in h_set or s in s_set:
      print("INVALID: duplicate hospital or student found")
      return False
    # else, add h and s to their respective sets
    else:
      h_set.add(h)
      s_set.add(s)
  return True

def stable_matching(hospital_pref, student_pref, assignments):
  # dictionary for matches
  h_s_dict = {} # key=h, v=s
  s_h_dict = {} # key=s, v=h
  for (h, s) in assignments:
    h_s_dict[h] = s
    s_h_dict[s] = h

  # loop through each hospital in hospital_pref
  for h in hospital_pref:
    # find the hospital's assigned student s
    try:
      s_match = h_s_dict[h.id]
    except KeyError:
      print(f"UNSTABLE: Hospital {h.id} has no match assigned")
      return False

    # loop through each pref for this hospital h
    for s in h.pref_list:
      if s == s_match:
        # reached current match, move to next hospital
        break
      else:
        # this is a student that h prefers over its current match s
        # find this student's current match
        h_match = s_h_dict[s]

        # find the student candidate object
        s_candidate_obj = next((x for x in student_pref if x.id == s), None)


        # check if this student prefers h over its current match h_match
        h_index = s_candidate_obj.pref_list.index(h.id)
        h_match_index = s_candidate_obj.pref_list.index(h_match)
        if h_index < h_match_index:
          # blocking pair --> unstable
          print(f"UNSTABLE: ({h.id}, {s}) is a blocking pair")
          return False
  return True

def main():
  if hospital_pref and student_pref and assignments:
    is_valid = valid_matching(assignments)
    if is_valid: print("VALID")

    is_stable = stable_matching(hospital_pref, student_pref, assignments)
    if is_stable: print("STABLE")
  else:
    return

if __name__ == "__main__":
  main()