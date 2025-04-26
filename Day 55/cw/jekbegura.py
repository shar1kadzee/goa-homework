# 3) კაპიტანმა ჯეკ ბეღურამ უნდა იყიდოს მისი ეკიპაჟისთვის გემი, თუ ოქროს მონეტების რაოდენობა არის 0, მაშინ აჯანყდება ეკიპაჟი, გავქვს 5 გემი :, 150 ქოროს მონეტიანი, 200 ოქროს მონეტიანი, 250 ოქროს მონეტიანი,  300  ოქროს მონეტიანი, 350 ოქროს მონეტიანი,  თუ კაპიტანმა ჯეკ ბეჟურამ აარჩია სასურველი გემი და არ ყოფნის ოქროს მონეტები მაშინ  ეკიპაჟი აჯანყდება, მონეტების რაოდენობა შემოატანინეთ gold_coin
# def captianjack():

def captianjack(coins):
    if coins == 0:
        return "აჯანყდა ეკიპაჟი"
    if coins == 150:
        return "იყიდა გემი"
    if coins == 200:
        return "იყიდა გემი"
    if coins == 250:
        return "იყიდა გემი"
    if coins == 300:
        return "იყიდა გემი"
    if coins == 350:
        return "იყიდა გემი"
    if coins > 350:
        return "ხურდა"
print(captianjack(0))
print(captianjack(200))
print(captianjack(350))
print(captianjack(125))
print(captianjack(120))
