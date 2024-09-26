note = int(input("Enter the Amount of Money:"))
note1000 = note//1000
note%= 1000

note500 = note//500
note%= 500

note200 = note//200
note%= 200

note100 = note//100
note%= 100
print("1000 Taka's Note: " , note1000)
print("500 Taka's Note: " , note500)
print("200 Taka's Note: " , note200)
print("100 Taka's Note: " , note100)
