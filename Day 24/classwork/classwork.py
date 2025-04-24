# 1) შექვნათ წინადადება fomrat mehtod გამოყენებით
# "წლითელი ვაშლი გაგორდა 50ml

# new_message = "witeli vashli gagorda {0} {1} " .format(50, "ml")
# print(new_message)


# 2) ხელთგვაქვს წინადადება "იხვის ტოლმა არ არის ბატის ტიოლმა"(ან მოიფიქრეთ)
# გამოვიყენოთ მეთოდი "split"
#  და გამოვიყენოთ 
# "join" მეთოდი
# და ამ წინადადებას როგორც კი გავსპილავთ ჯოინებით დავაბრუნოთ სასურველი ტექსტი (რაც გინდათ)

name = "იხვის ტოლმა არ არის ბატის ტიოლმა"
split_name = name.split(" ")
joined_name = " ! ".join(split_name)

print(joined_name)
print(split_name)