while True:
    try:
        bg=float(input("please enter your budget : "))
        s=bg
    except ValueError as a:
        print("Print Number As A Amount")
        continue
    finally:
        break

a={"item":[],"quantity":[],"price":[]}
b = list(a.values())
na = b[0]

qu = b[1]

pr = b[2]

while True:
    try:
        ch = int(input("1.ADD\n2.EXIT\nEnter your choice : "))
    except ValueError:
        print("\nERROR: Choose only digit from the given option")
        continue
    else:
        if ch == 1 and s > 0:
            pn = input("Enter product Name : ")
            
            q = input("Enter Quantity : ")
            
            p = float(input("Enter Price of the product : "))
            
            if p>s:
                print("\nCAN'T BUY THIS PRODUCT")
                continue
            else:
                if pn in na:
                    ind=na.index(pn)
                    
                    qu.remove (qu[ind])
                    
                    pr.remove(pr[ind])
                    
                    qu.insert(ind,q)
                    
                    pr.insert(ind,p)
                    
                    s=bg-sum(pr)
                    
                    print("\namount left", s )
                else:
                    na.append(pn)
                    
                    qu.append(q)
                    
                    pr.append(p)
                    
                    s=bg-sum(pr)
                    
                    print("\namount left", s)
        elif s<=0:
           print("\nNO BUdget")
        else:
            break
print("\aAMOUNT left : RS. ", s)

if s in pr:
    print("\nAmount left can buy you a", na[pr.index(s)])
print("\n\n\nGROCERY List")
for i in range(len(na)):
    print(na[i], qu[i], pr[i])
    
    
    