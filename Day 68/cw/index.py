# 1) შემქნეით lambda-ს ფუნქცია, lambda-ს უნდა ჰქონდეს  3 არგუმენტი და უნდა გამოთვალო მისი საშვალო

average = lambda a, b, c: (a + b + c) / 5
print(average(2, 4, 7))  


# 2) შექმენით lambda-ს ფუნქცია, lambda-ს ჰქონდეს მინიმუმ 2 არგუმენტი და იპოვეთ აქედან ყველაზე ნაკლები

find_min = lambda a, b: a if a < b else b
print(find_min(1, 9))



# 3) შექმენით lambda-ს ფუნქცია, lambda-ს ჰქონდეს მინიმუმ 2 არგუმენტი და იპოვეთ აქედან კენტი

odds = lambda a, b: [x for x in (a, b) if x % 4 != 0]

res = odds(3, 8)
print(res)