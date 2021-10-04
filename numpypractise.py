import numpy as np


# We can create the Numpy using Collections of python(List,Tuple ,Dictionary Etc...)
# creating 0 dimension Array
a=np.array(10)
print(a)
# creatin 1 dimension Array (collection of zero dimension Array nothing but One Dimension Array)
oneDimension=np.array([10,20,30,40])
print(f"Slicing {oneDimension[:2]}")
print(f"One dimension {oneDimension}")
print(f"Accession {oneDimension[2]}")
#creating 2 demension Array (Collection of one dimension Array nothing But One dimention Array)
twoDimension= np.array([[10,20],[33,56]])
print(f"Two Dimension {twoDimension}")
print(f"Accessing Two Dimension {twoDimension[0][1]}")
#creating 3 demension Array (Collection of one dimension Array nothing But Two dimention Array)
threeDimension=np.array([[[10,20],[33,56]],[[10,20],[33,56]]])
print(f"Three Dimension Array {threeDimension}")
print(f"Accessing element {threeDimension[0][1][0]}")

# using AsArray function having three param 1st one collection 2nd datat type 3rd one order(row major order or coloumn major order)
lis=[1,2,3]
print(np.asarray(lis,dtype=float))
# using Order it either it should be F=Column Major Order or C=row Major Order
olic=[[2,3],[1,2]]
print(np.asarray(olic,order="C")) # it wont show the difference we need to use nditer() then we will find the Difference
print("Row major Orer")
for i in np.nditer(np.asarray(olic,order="C")):
    print(i)
print("Coloumn major Orer")
for i in np.nditer(np.asarray(olic,order="F")):
    print(i)

# use Frombuffer() function if we need to consider String as buffer add "b" in front like below
str=b"Abhishek is good"
print(np.frombuffer(str,dtype="S1")) # need to use S1 as dtype for String

print(np.frombuffer(str,dtype="S1",count=2,offset=8)) # count how many letters it should consider in buffer and offset is where to start

# fromIter()
fromiterlist=[1,2,3]
print(np.fromiter(fromiterlist,dtype=int,count=3))


#Initializing Arrays
# we functions like zeros() all will be filled with zeros
print(np.zeros(3,dtype=int))
print(np.zeros([2,3])) # two dimensional
print(np.zeros([2,3,4])) # three dimensional
# full function to fill the array with the value
print(np.full(3,1,dtype=int)) # first aur dimensional value
print(np.full([1,2],2,dtype=int))

# random.rand() fill the array with random values
print(np.random.rand(2)) # default fload
print(np.random.randint(3,10,size=(2,3))) # int random param low,hign, size=(2,3) diemsion ,dtype=int "it will print random numbers between 3 and 10

#like as zeros function onesfunction
print("****************Using ones() function******************")
print(np.ones(3,dtype=int))
print(np.ones([2,3],dtype=int))

#eye function diagnal element will be one and remaining will be zero if it is square else rows can also be declared
print("*******************Using eye() function ******************")
print(np.eye(2,dtype=int))
print(np.eye(2,dtype=int))

# *********************Numarical Ranges Fucntions ************
print("********** Using arange() function**********")
print(np.arange(10,20,2,dtype=int)) # start stop step like range()
print("**** using reshape*******")
reshapearray=np.arange(10,20,2,dtype=int)
print(reshapearray.reshape(5,1)) #reshaping to 5 rows one coloumn

#********** Line Space Function *************
print("*****************linespace()*************")
print(np.linspace(1,20,2)) # start and stop and nmber of elemts so that  it will divide numbers into equal intervel
print(np.linspace(10,100,10,endpoint=False,dtype=int)) # ignoring the stop element by default end point false
print(np.linspace(10,100,10,endpoint=False,dtype=int,retstep=True)) # to know the intervel



#********** Log Space Function *************
print("*****************logspace()*************")
print(np.logspace(1,10,2,base=2)) # same as linespace but log value will get and base by default 10

#************* size(),shape(),dype()
arraylelem=np.arange(10,100,10)
print(arraylelem)
arraylelem=arraylelem.reshape(3,3)
print(f"with Size function  : {np.size(arraylelem)}")
print(f"with Shape function  : {np.shape(arraylelem)}")
print(f"with dtype function : {arraylelem.dtype}")

# ****** Array Operations*******"

# copy function
print("**********Using copy()******")
realarray=np.array((1,2,6,5,3,8))
copiedarray=np.copy(realarray)
print(f"coppied arry {copiedarray}")
# view funciton
print("**********Using view()******")
viewdarray=realarray.view()  # if real array changes viewdarray will change realarray reference will be given to viewd array
print(f"view Array {viewdarray}")
# sort
print(f"print sorted array {np.sort(realarray)}")
print(f"sort two dimension array{np.sort(twoDimension,axis=1)}") # axis 1 means row wise 0 means coloumn wise default value 1

d=np.dtype([('name','S1'),('perc',int)])
marks=np.array([("sare",12),("abhi",564),("hello",5858)],dtype=d)
print(np.sort(marks,order="name"))

#reshape already done

#append means
print(f"appedn {np.append(realarray,copiedarray)}") #output will be single dimension even if we use multi dimension

#insert
print(np.insert(realarray,2,35)) # if multiple elememnts use [12,45] out put single dimension
#delete 
print(np.delete(twoDimension,3)) # deleted and form single dimension out put is a single dimension array
#concatenate
print(np.concatenate((realarray,copiedarray))) # use paranthesis

print(np.concatenate((twoDimension,twoDimension),axis=1))

#stack

print(np.stack((realarray,copiedarray))) # into seperate concatenation it will not merge  Axis here it will be concate based on row and col

#vstack
print(np.vstack((realarray,copiedarray))) # concatenate with respective to coloumn

#hstack
print(np.hstack((realarray,copiedarray))) # concatenate with respective to row
twoDimension1= [[56, 59],
  [365, 5556]]
#dstack
print(np.dstack((twoDimension,twoDimension1)))

#split
print(np.split(realarray,2)) #splitting array into number givven output list of splitted array
# we can split into multi demension also 
print(np.split(realarray,(2,3)))

#where to check the element
print(np.where(realarray==6))
print(np.where(realarray%2==0))

#searchSoretd
print(np.searchsorted(realarray,6)) # apply binary search
print(np.searchsorted(realarray,[1,6])) #multiple elements can search

#"Arthematic opearions" To perform Both should be same Dimension
#add()
print("********************Addition******************************")
print(np.add(twoDimension,twoDimension1))
#multiply()
print("********************Addition******************************")
print(np.multiply(twoDimension,twoDimension1))
#subtract()
print("********************subtract******************************")
print(np.subtract(twoDimension,twoDimension1))
#divide()
print("********************Divide******************************")
print(np.divide(twoDimension,twoDimension1))
#exp()
print("********************Exponential******************************")
print(np.exp(twoDimension))
#sqrt()
print("********************Square root******************************")
print(np.sqrt(twoDimension))
#array_equal()
print("********************ArrayEquals ******************************")
print(np.array_equal(twoDimension,twoDimension1))

# Array Functions sum,min,max,mean,median,var,std(standard deviation)

#sum()
print("********************sum *****************************")
print(np.sum(twoDimension)) # we can use axis also

#min()
print("********************min *****************************")
print(np.min(twoDimension)) # we can use axis also

#max()
print("********************max *****************************")
print(np.max(twoDimension)) # we can use axis also

#mean()
print("********************mean *****************************")
print(np.mean(twoDimension)) # we can use axis also

#meadian()
print("********************median *****************************")
print(np.median(twoDimension)) # we can use axis also

#var()
print("********************var *****************************")
print(np.var(twoDimension)) # we can use axis also
#std()
print("********************std *****************************")
print(np.std(twoDimension)) # we can use axis also



