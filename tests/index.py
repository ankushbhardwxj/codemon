import codemoninitdir

if __name__ == "__main__":
  success, failed = 0, 0
  # test 1
  print("Running test 'Codemon init dir':")
  if codemoninitdir.codemoninitdir() == 0: success += 1
  else: failed += 1

  # print test results 
  print("***** Test results *****")
  print("Total:   ", success + failed)
  print("Success: ", success)
  print("Failed:  ", failed)

