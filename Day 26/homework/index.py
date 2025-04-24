# 1) სამკუთხდები დამიხაზეთ 120 ცალი ოღონდ მხოლოდ კენტი <3 რიცხვებით ფუქნციების გამოყევებეა არ დაგვავიწყდეს
# თუ ჩვენი სამკუთხედი დამეთხვევა კენტ index მაში ნ სამკუთხედი იყოს მწვანე თუ არა და იყოსლურჯი
from turtle import * 
speed(30)
def triangle(a):
    if a % 2 == 0:
        color("red")
    else:
        color("black")
    begin_fill()
    forward(10)
    left(120)
    forward(10)
    left(120)
    forward(10)
    end_fill()
    penup()
    left(30)
    forward(10)
    left(90)

for i in range(50):
    triangle(i)
exitonclick()







# 2) hello_world-როცა დავწერთ გამოვიტანოს print() 

# def hello_world():
#     print("print")

# hello_world()
    

# 3) def-ის გამოყენბით შემქენით ფუქნცია even_or_odd() შევამოწმოთ ჩვენი გამდოცემული არგუმენტი/ მაგალითილითად even_or_odd(23) არის თუ არა კენტი თუ არის დვაწეროთ "კი არის კენტი" თუ არა "არ არის კენტი"
# ***hard level***

# def even_od_odd():
#     num = int(input("sheikvanet raime ricxvi: "))
#     print(f"ar aris kenti" if num % 2 == 0 else "ricxvi kentia" )

# even_od_odd()

# 4) შექმენით ფუქცნია რომელიც 120 ჯერ გამოიტანს შემდეგი სახის ფუქგურები
# ******
# ******
# ******

# def square(arr):
#     for i in range(arr):
#         arr = ["******","******","******"]
#         print(arr[0])
#         print(arr[1])
#         print(arr[2])
    

# square(120)

#      *
#     ***
#   *******
# ***********
#      *
#      *

# def square(arr):
#     for i in range(arr):
#         arr = ["     *","    ***","  *******","***********","     *","     *"]
#         print(arr[0])
#         print(arr[1])
#         print(arr[2])
#         print(arr[3])
#         print(arr[4])
#         print(arr[5])
    
# square(120)


# *******
#  *******
#   ********
#     # ********


# def square(arr):
#     for i in range(arr):
#         arr = ["*******"," *******","  *******","   *******"]
#         print(arr[0])
#         print(arr[1])
#         print(arr[2])
#         print(arr[3])
    

# square(120)