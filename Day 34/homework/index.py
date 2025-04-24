# 1) შექმენით tuple, საიდანაც დაპრინტავთ პირველ ორ ელემენტს 

# 2) numbers = (2, 56, 99, 22, 15, 23, 66, 11, 134, 23, 66, 91, 22, 2, 23)

#    numbers tuple-ში დაპრინტეთ რამდენჯერ მეორდება ციფრი 23 count-ის გამოყენებით

# 3) aura = (10, 25, 5, 80, 70, 20) 

#    aura tuple-დან for loop-ის გამოყენებით დაბეჭდეთ მხოლოდ 10-ზე დიდი რიცხვები

# 4) კომენტარის სახით ახსენით, რა განსხვავებაა list-სა და tuple-ს შორის

# 5) კომენტარის სახით ახსენით, რას ნიშნავს immutable და mutable



tuflebi = (1,2,3,4,5)
print(tuflebi[0])
print(tuflebi[1])

numbers = (2, 56, 99, 22, 15, 23, 66, 11, 134, 23, 66, 91, 22, 2, 23)
print(numbers.count(23))

aura = (10, 25, 5, 80, 70, 20)
for i in aura:
    if i > 10:
        print(i)
    
# listi aris sia romlis shecvlac chven shegvilia xolo tuplebshi chven ar shegvilia elementi shevcvalot

#ummutable = tuple
#mutable - list