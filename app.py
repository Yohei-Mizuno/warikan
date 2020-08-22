total_amount = int(input('合計金額を入力⇨'))

total_number_of_people = int(input('合計人数を入力⇨'))


amount_per_person = total_amount // total_number_of_people

fraction = total_amount % total_number_of_people

print(f'1人当たりの金額⇨{amount_per_person}円\n端数⇨{fraction}円')
