# დავალება  იური გაგარიზნე
# შევქმნათ ფუნქცია yuri_gagarini()
# იური გაგარინის წნევა აღწვევდა 120-გულის წნევას პულსი 80-ს თქვენი დავალეება რომ შექმნათ ფუქნცია რომელიც 
# მომახარებელს user -ს შეეკითხება თუ რამდენი აქვს გულის წნევა და პუსლი თუ დაემთხვევა პულსი იურინი გაგარინს პულს მაშინ Ture გამოიტანოს წინააღმდეგ შემთხვევაში Falase

def iuri_gagarini():
    heart_rate = int(input("enter your heart rate: "))
    pulse_rate = int(input("enter your pulse rate: "))

    if (heart_rate == 120 and pulse_rate == 80):
        return True
    return False