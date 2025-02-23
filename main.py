import random
#  Создаём список 
length = random.randint(3, 10)
original_list = [random.randint(1, 100) for _ in range(length)] 

# Выбираем нужные элементы 
new_list = [original_list[0], original_list[2], original_list[-2]]
# Вывод результата 
print(f"Оригінальний список (довжина {len(original_list)}): {original_list}")
print(f"Новий список: {new_list}")
