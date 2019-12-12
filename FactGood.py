print("Factorial")

def FactInput():
    global num
    num=0    
    num = input("enter interger number: ")
    if not num.isdigit():
        FactInput()
           
def Fact(num):
    f=1
    while num > 1:
        f=f*num
        num-=1
    return(f)

more='y'
while more == 'y':
    FactInput()
    num=int(num)
    f=Fact(num)
    print('Factorial of: ',num,' is ',f)
    more = input("enter y to continue: ")


    
        
    
   
    
    

