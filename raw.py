row_1 =["🥴", "🥴", "🥴"]
row_2 =["🥴", "🥴", "🥴"]
row_3 =["🥴", "🥴", "🥴"]
map = [row_1, row_2, row_3]

print(f"{row_1}\n{row_2}\n{row_3}")
choice = input ("Enter the colum and row : ")

colum = int(choice[0])
row =int(choice[1])

selected_colum = map[row - 1]
selected_colum [colum - 1] ="🤪"

print(f"{row_1}\n{row_2}\n{row_3}")