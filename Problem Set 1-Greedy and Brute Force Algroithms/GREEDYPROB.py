import random
class Food(object):

    def __init__(self,n,c,v):
        self.name=n
        self.value=v
        self.calories=c
    def __str__(self):
        return self.name+"< "+str(self.value)+", "+str(self.calories)+", "+str(self.getratio())+" >"
    def getvalue(self):
        return self.value
    def getname(self):
        return self.name
    def getcalories(self):
        return self.calories
    def getratio(self):
        return self.getvalue()/self.getcalories()


def buildmenu(item,value,cal):
    menu=[]
    print(item)
    print(value)
    print(cal)
    for i in range(len(item)):
        menu.append(Food(item[i],value[i],cal[i]))
    return menu

def greedy(food,maxcost,keyval):
    foodcopy=sorted(food,key=keyval,reverse=True)
    totalval,totalcal=0.0,0.0
    result=[]
    for i in range(len(foodcopy)):
        if(totalcal+foodcopy[i].getcalories()<=maxcost):
            totalcal+=foodcopy[i].getcalories()
            totalval+=foodcopy[i].getvalue()
            result.append(foodcopy[i])
    return (result,totalval,totalcal)

def maxval(foodlist,amountspent):
    if foodlist==[] or amountspent==0:
        result=(0,())
    elif foodlist[0].getcalories()>amountspent:
        return maxval(foodlist[1:],amountspent)
    else:
        item=foodlist[0]
        withval,withtake=maxval(foodlist[1:],amountspent-item.getcalories())
        withval+=item.getvalue()
        withoutval,withouttake=maxval(foodlist[1:],amountspent)
        if withval>withoutval:
            result=(withval,withtake+(item,))
        else:
            result=(withoutval,withouttake)
    return result

def largemenu(n):
    items=[]
    val=[]
    cal=[]
    str="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(n):
        items.append(str[random.randrange(len(str))])
        val.append(random.randrange(1,500))
        cal.append(random.randrange(1,500))
    return buildmenu(items,val,cal)
food=largemenu(10)

foodeaten,values,calories=greedy(food,500,Food.getratio)
for i in range(len(foodeaten)):
    print("<  ",foodeaten[i]," >")

val,taken=maxval(food,1000)
for i in taken:
    print(" ",i)




