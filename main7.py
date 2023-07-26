def numPolindrom(num):
     reverse_num = num[::-1]
     if reverse_num == num:
         return True
     else:
         return False

value = input("Введіть число для перевірки поліндром: ")
print(numPolindrom(value))



