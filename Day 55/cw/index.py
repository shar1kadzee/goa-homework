# დავალება ნუგზარ ჩუბინძიე
# ნუგზარ ჩუბინიძე ამობობს სადღეგრძელოს

# ჩვენი ამოცანა მდებაროებს შემდეგში:
# შევქმანთ ფუქნცია nugzar_chubinidze() რომელსაც 2 პარამეტრი , sadgerdzelo, limit

# თუ ნუგზარს limit -ზე მეტი ექნება დალეული ჩვენმა ფუქნციამ უნდა გამოგვიტანოს რომ იგი ლუიზა: ნუგზარი აღარ დალიო მეტი! 
# ხოლო თუ არ ცდება limit -ს მაგ შემთხვევაში დაგვიბრუნოს მოდი ახლა მართლა, დამილოცნიე! 
# 

def nugzar_chubinidze(sadgegrdzelo, limit):
    if sadgegrdzelo > limit:
        return "ლუიზა: ნუგზარი აღარ დალიო მეტი! "
    else:
        return"ნუზარი: მოდი ახლა მართლა, დამილოცნიე!"