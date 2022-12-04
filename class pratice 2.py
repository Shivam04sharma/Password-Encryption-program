#----------------- encrypted code generator ------------------
def code(passwd):
    size=len(passwd)
    add=0
    pro=1
    for i in passwd:
        add=add+ord(i)
        pro=pro*(ord(i)+add)
    list1=[]
    for j in passwd:
        value100=(pro+(ord(j)/len(passwd))/ord(j))*(ord(j)/add)
        n=str(int(value100))
        listvalue=n[-1]
        if 0<=int(listvalue)<10:
            list1.append(listvalue)
        else:
            a=str(listvalue)
            b=a[-1]
            list1.append(abs(int(b)))
    key="0123456789"
    value=["!","@","#","$","%","&","*","?","|","/"]
    result=""
    for k in list1:
        b=key.find(k)
        result=result+value[b]
    return result
#-------------------- parameter check ----------------------
def para(passwd):
    if 6<=len(passwd)<=14:
        check1="abcdefghijklmnopqrstuvwxyz"
        check2="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        check3="0123456789@#&*%"
        result="valid"
        for i in passwd:
            if i in check1 or i in check2 or i in check3:
                continue
            else:
                result="invalid"
                break
    else:
        result="invalid"
    return result
#---------------------- Input program -----------------------
print("#"*60)
print(" "*20,"..... WELCOME .....")
print()
print(" "*20,"Password Encryptor")
while True:
    print("*"*60)
    print("""# Press:
> P or p for password
> E or e for exit""")
    print("-"*30)
    cmd=input(">>> Enter the command: ")
    if cmd in "Pp":
        print("-"*60)
        print("""# Password Parameter:
> a-z and A-Z
> 0-9 and @ # & * %
> 6<= length <=14""")
        print("-"*35)
        passwd=input(">>> Enter Password: ")
        if para(passwd)=="valid":
            print("-"*60)
            print("# Encrypted Password:",code(passwd))
        else:
            print("-"*60)
            print(" "*10,"! Invalid Password, Check Parameters...")
    elif cmd in "Ee":
        print("-"*60)
        print(" "*25,"Visit Again")
        print("#"*60)
        break
    else:
        print("-"*60)
        print(" "*23,"Invalid input")
#---------------------- End of code -------------------------