import os
from time import time
from matching_algo import main
from verifier import valid_matching, stable_matching

n_size = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

os.makedirs("test_data", exist_ok=True)

algo_time = []
verify_time = []

for n in n_size:
  filename = f"test_data/example_{n}.in"
  with open(filename, "w") as f:
    f.write(f"{n}\n")
    # hospital preferences (first n lines)
    for i in range(n):
      pref_list = [(i + j) % n + 1 for j in range(n)]
      f.write(" ".join(map(str, pref_list)) + "\n")
    # student preferences (next n lines)
    for i in range(n):
      pref_list = [(i + j) % n + 1 for j in range(n)]
      f.write(" ".join(map(str, pref_list)) + "\n")
  
  t0 = time()
  hospital_pref, student_pref, assignments = main(filename)
  t1 = time()
  algo_time.append(t1 - t0)

  t3 = time()
  valid_matching(assignments)
  stable_matching(assignments)
  t4 = time()
  verify_time.append(t4 - t3)

print(algo_time)
print(verify_time)
