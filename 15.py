def matsubi_hyoji(file, gyosu):

        f_list = []
        f_list2 = []

        with open(file, encoding = 'utf-8') as f:
               f_list = f.readlines()
        
        f_list.reverse()

        for i in range(gyosu):
               f_list2.append(f_list[i])

        f_list2.reverse()
        
        return f_list2

test = matsubi_hyoji('hightemp.txt', 3)
print(test)