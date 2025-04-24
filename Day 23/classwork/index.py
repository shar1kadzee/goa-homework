# 1) List-ის შექმნა და ელემენტების გამოტანა
# შექმენით სია, რომელიც შეიცავს 5 რიცხვს. შემდეგ გამოიტანეთ პირველი, ბოლო და შუათანაში მყოფი ელემენტები.

# 2) List-ის შეცვლა
# შეასწორეთ შეცდომები რასაც ხედავთ არასწორს ჩაასწორედ აუციელბლად  num = [1, 3, 3, 4, 5, 6, 6, 8, 9, 12]


# 3)მიწარმოეთ რამდენიმე სიტყვა  HELLOWEN იდან 

# 4) შეაერთე სიტყვა რომ გამოვიდეს GOA IS THE BEST ACADEMY

# ["GOA" , "MAGARIA", "NOVATORI","IS","THE", "VIRGIN", "CHAD" ,"BEST" ,"ACADEMY"



# 1
num =[1, 2, 3, 4, 5]
  #  0  1  2  3  4
print(num[0])
print(num[2])
print(num[4])

# 2
num = [1, 3, 3, 4, 5, 6, 6, 8, 9, 12] 
#     #  0  1  2  3  4  5  6  7  8  9
num[1] = 2 
num[6] = 7 
num[9] = 10
print(num)

something = "helloween"
print(something[0:5])
print(something[5] + something[6] + something[2] + something[3])
print(something[8] + something[4])
print(something[8] + something[4] + something[5])

list = ["GOA" , "MAGARIA", "NOVATORI","IS","THE", "VIRGIN", "CHAD" ,"BEST" ,"ACADEMY"]
#      0         1          2          3     4      5       6       7         8
print( list[0], list[3], list[4], list[7], list[8])
