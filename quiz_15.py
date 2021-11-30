def Reverse_Mode(Input):
    digit1=int(Input[10])
    digit2=int(Input[9])
    digit3=int(Input[8])
    digit4=int(Input[6])
    digit5=int(Input[5])
    digit6=int(Input[4])
    digit7=int(Input[2])
    digit8=int(Input[1])
    digit9=int(Input[0])
    Output=digit1 + digit2*2 + digit3*4 + digit4*10+digit5*20 + digit6*40 + digit7*100+digit8*200 + digit9*400
    return Output
    
print(Reverse_Mode("100!000!111"))


