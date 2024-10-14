#Number 1
x = int(input("How good is performance? ")) #membuat variable x dan input
if x >= (90) :  #Membuat decision making
    print('Excellent Performance!') #Menampilkan output text
elif x >= (80) :
    print('Very Good Performance')
elif x >= (70) :
    print('Good Performance')
elif x >= (60) :
    print('Average Performance')
else:
    print('Bad Performance :<')
