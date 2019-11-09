f = open("instructions.txt", "a")
f.close()

f = open("instructions.txt", "r")
exe = open("execute.py", "w").close()
exe = open("execute.py", "r+")

commands = f.readlines()

exe.write("def main():")

for instr in commands:
  printer = 0
  for comm in range(0, len(instr.split())):
    if printer:
      if comm < len(instr.split()) - 1:
        exe.write(instr.split()[comm]+" ")
        continue
      else:
        exe.write(instr.split()[comm]+'")')
        
        break
    
    if instr.split()[comm].lower() == "exit":
      exe.write("\n\tquit()")
      break
    
    elif instr.split()[comm].lower() == "print":
      printer = 1
      exe.write('\n\tprint("')
      continue
    
    
    
    
    
    
  


exe.close()
f.close()

print("Code writtern successfully. Please run 'execute.py' to complete.")