#Guest lucky number.
LuckyNumber = 19
input_num = -1

while LuckyNumber != input_num:
    input_num = int(input("Input the guess num:"))
    #if input_num == LuckyNumber:
    #    print ("bingo!")
    #    break
    if input_num > LuckyNumber:
        print ("the read number is smaller.")
    elif input_num < LuckyNumber:
        print ("the real num is bigger...")

print ("bingo")