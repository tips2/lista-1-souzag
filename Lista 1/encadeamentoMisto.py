PC = False
GPU = False
CPU = False
RAM = False
PC_casual = False
PC_mid = False
PC_high = False

def Base_Fatos():
  global PC
  PC = True

if __name__ == "__main__":
  Base_Fatos()
  lim = range(0, 10)

  for i in lim:
    if(PC and CPU):
      PC_casual = True

    if(PC and RAM):
      PC_high = True

    if(PC_high):
      GPU = True

    if(PC_mid):
      print(f'(PC_mid) = Sim\n')
      break

    if(PC_casual and GPU):
      PC_mid = True

    if(PC):
      CPU = True
      RAM = True

  else:
    print(f'(PC_mid) = Não\n')