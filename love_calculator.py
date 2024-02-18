print('welcome to love calculator')
name1=input('enter your name')
name2=input('enter your lover name')

combined_string=name1+name2
lowercase_string=combined_string.lower()

t=lowercase_string.count('t')
r=lowercase_string.count('r')
u=lowercase_string.count('u')
e=lowercase_string.count('e')

true=t+r+u+e

l=lowercase_string.count('l')
o=lowercase_string.count('o')
v=lowercase_string.count('v')
e=lowercase_string.count('e')

love=l+o+v+e

final_result=(int(true)+int(love))



if((final_result)>12):
    print(f'your love score is {final_result},your love is wonder')
elif(final_result)>7 and (final_result)<=12:
    print(f'your love score is {final_result},your love is pure ')

elif((final_result)>4 and  (final_result)<=7):
    print(f'your  love score is {final_result},your love Is little bit good')

else:
    print('fake love')
          
    
