#PF-Prac-1
def add_string(str1):
 length=len(str1)
 if(length>2):
     if(str1[-3:]=='ing):
         str1+='ly'
    else:
        str1+='ing'
  return str1

print(add_string('sleep'))
print(add_string('amazing'))
print(add_string('is'))


#PF-Prac-2
def bracket_pattern(input_str):
    length=len(input_str)
    if(length%2!=0):
        return False
    elif(input_str[0]==')'or input_str[-1:]=='('):
        return False
    else:
        return True 
print(bracket_pattern(')()((()()))'))
print(bracket_pattern('()((())())'))


#PF-Prac-3
def create_new_dictionary(prices):
    new_dic={}
    for key in prices:
        if(prices[key]>200):
            new_dic.__setitem__(key,prices[key])
    
    return new_dic

prices = { 'ACME': 45.23,'AAPL': 612.78,'IBM': 205.55,'HPQ': 37.20,'FB': 10.75}
print(create_new_dictionary(prices)) 
	
	



#PF-Prac-4
def find_nine(nums):
    for i in range(0,len(nums)):
        if(nums[i]==9 and i<4):
            return True
            break
        
    return False
    
nums=[1,9,4,5,6]
print(find_nine(nums))


#PF-Prac-5
def count_digits_letters(sentence):
    result_list=[]
    c1=0
    c2=0
    for i in sentence:
        if(i.isalpha()):
            c1+=1
        if(i.isdigit()):
            c2+=1
    result_list.append(c1)
    result_list.append(c2)
    return result_list

sentence="Infosys Mysore 570027"
print(count_digits_letters(sentence))


#PF-Prac-6
def list123(nums):
    needed=[1,2,3]
    if str(needed)[1:-1] in str(nums):
        return True
    return False

    

nums=[1,2,3,4,5]
print(list123(nums))


#PF-Prac-7
def seed_no(number,ref_no):
    temp=number
    while number>0:
        digit=number%10
        temp=temp*digit
        number=number//10
    if(temp==ref_no):
        return True
    return False
    
    
number=123
ref_no=738
print(seed_no(number,ref_no))


#PF-Prac-8
def calculate_net_amount(trans_list):
    net_amount=0
    for i in trans_list:
        a=[]
        a=i.split(":")
        if(a[0]=='D'):
            net_amount+=int(a[1])
        else:
            net_amount-=int(a[1])
    
    return net_amount

trans_list=["D:300","D:200","W:200","D:100"]
print(calculate_net_amount(trans_list))

#PF-Prac-9
def generate_dict(number):
	new_dict={}
	for i in range(1,number+1):
	    new_dict[i]=i**2
	
	return new_dict

number=20
print(generate_dict(number))


#PF-Prac-10
def string_both_ends(input_string):
	length=len(input_string)
	if(length<2):
	    return -1
	else:
	    newstr=""
	    newstr=input_string[0:2]+input_string[-2:]
	return newstr
	    
input_string="w3w"
print(string_both_ends(input_string))


#PF-Prac-11
def find_upper_and_lower(sentence):
    #start writing your code here
    up=0
    lo=0
    for i in sentence:
        if(i.islower()):
            lo+=1
        if(i.isupper()):
            up+=1
    result_list=[]
    result_list.append(up)
    result_list.append(lo)

    return result_list

sentence="Come Here"
print(find_upper_and_lower(sentence))


#PF-Prac-12
def generate_sentences(subjects,verbs,objects):
    sentence_list=[]
    for i in subjects:
        for j in verbs:
	        for k in objects:
	            sentence_list.append(i+" "+j+" "+k)
    return sentence_list

subjects=["I","You"]
verbs=["love", "play"]
objects=["Hockey","Football"]
print(generate_sentences(subjects,verbs,objects))

#PF-Prac-14
def find_five_digit():
    num2=0
    num3=0
    num4=0
    num5=0
    for i in range(9,-1,-1):
        num2=int(i-2)
        num3=int(num2-2)
        num4=int(num3-2)
        num5=int(num3)
        if(num3+num4+num5==i and num2+num3+num4+num5+i==19):
            break
    s=str(i)+str(num2)+str(num3)+str(num4)+str(num5)
    print(s)

find_five_digit()


#PF-Prac-15
def check_22(num_list):
    for i in range(0,len(num_list)-1):
        if(num_list[i]==2 and num_list[i+1]==2):
            return True
    return False
        
print(check_22([3,2,5,1,2,1,2,2]))


#PF-Tryout 22
def diagonal_stars(number):
   #start writing your code here
    for i in range(0,number):
        for j in range(i):
            print(".",end="")
        print("*")

number=6    
diagonal_stars(number)


#PF-Prac-23
def divisible_by_sum(number):
    temp=number
    sum=0
    while(number>0):
        rem=number%10
        number=number//10
        sum+=rem
    if(temp%sum==0):
        return True
    else:
        return False
	
#PF-Prac-24	
def gcd_of(a,b):
    if(b==0):
        return a
    else:
        return gcd_of(b,a%b)


num1=14
num2=35
print(gcd_of(num1,num2))


#PF-Prac-25
def get_length(word):
    length=[]
    for i in word:
        length.append(len(i))
    return length


word=['cat','Come']
print(get_length(word))


#PF-Prac-26
def check_occurence(string):
    string=string.lower()
    c=string.count("mat")
    cc=string.count("jet")
    if(c==cc):
        return True
    else:
        return False
        
string="Jet on the Mat but mat is too long"
print(check_occurence(string))



#PF-Prac-27
def sum_num(a,b):
    if(a==10 or b==10):
        return True
    elif((a+b)==10):
        return True
    else:
        return False
    
    
num1=3
num2=9
print(sum_num(num1,num2))



#PF-Tryout28
def sing_99_bottles():
   for i in range(99,0,-1):
    print(i,end="")
    print("bottles of beer on the wall,",end="")
    print(i,end=" ")
    print("Take one down, pass it around," ,end=" ")
    print(int(i-1),end="")
    print("bottles of beer on the wall.")
   
sing_99_bottles()



#PF-Prac-29
def exchange_list(number_list):
    #start writing your code here
    d=len(number_list)
    a=len(number_list)//2
    b=a//2+a
    k=0
    for i in range(a,b):
        c=number_list[i]
        number_list[i]=number_list[d-k-1]
        number_list[d-k-1]=c
        k=k+1
    for i in range(a):
        temp=number_list[i]
        number_list[i]=number_list[i+a]
        number_list[i+a]=temp
    return number_list

    
     
number_list=[1,2,3,4,5,6]
print(exchange_list(number_list))

#PF-Prac-31
def sum_of_elements(num_list,number):
    a=len(num_list)
    result_sum=0
    for i in range(1,a-1):
        if(num_list[i-1]!=number and num_list[i+1]!=number and num_list[i]!=number):
            result_sum+=num_list[i]
    if(num_list[1]!=number and num_list[0]!=number):
        result_sum+=num_list[0]
    if(num_list[a-2]!=number and num_list[a-1]!=number):
        result_sum+=num_list[a-1]
    return result_sum
      
num_list=[1,2,1,2]
number=2
print(sum_of_elements(num_list, number))

	
#PF-Prac-37
def sum_of_list(num_list):
    if(len(num_list)>1):
        return num_list[0] + sum_of_list(num_list[1:])
    else:
        return num_list[0]
num_list=[44,23,77,11,89,3]
result=sum_of_list(num_list)
print("Sum of the elements:",result)

	
#PF-Prac-38
r,c=map(int,input().split())
l=[]
for i in range(0,r):
    n=[]
    for j in range(0,c):
        temp=str(i)+','+str(j)
        n.append(temp)
    l.append(n)
    print("[",end="")
    print(*l,sep='\n',end="")
    print("]")
	
	
#PF-tryout 46	
n=list(map(int,input().split()))
print(0,end="")
for i in range(1,len(n)):
    print(n[i-1]*2,end="")

	
#PF-Tryout 46

def doublePreceding (values):
    if len(values) > 0:
        previous = values[0]
        values[0] = 0
        for idx in range(1, len(values)):
            previous1 = values[idx]
            values[idx] = 2 * previous
            previous=previous1
    return values
    
print(doublePreceding([3,8,2]))


#46_hackerrank
b=input()
b=b.split(" ")
def double(v):
    if len(v) > 0:
        pre = int(v[0])
        v[0] = 0
        for i in range(1, len(v)):
            temp=int(v[i])
            v[i] = 2 * int(pre)
            pre = temp
    return v
bb=double(b)
for i in bb:
    print(i,end=" ")

	
