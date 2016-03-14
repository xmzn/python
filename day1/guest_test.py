#Guest lucky number.
LuckyNumber = 19
input_num = -1

while LuckyNumber != input_num:
    input_num = int(raw_input("Please input a lucky number:"))
    if LuckyNumber == input_num:
        print ("Bingo")
    elif input_num > LuckyNumber:
        print ("Please input a litter lucky number!")
    elif input_num < LuckyNumber:
        print ("Please input a big lucky number!")