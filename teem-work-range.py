def my_range(*args):
    def cor_range(start_r, finish_r, step_r):#ядро обработки решает шаг + или - получая 3 аргумента
        if step_r >0:
            while start_r < finish_r:
                yield start_r
                start_r += step_r
        elif step_r <0:
            while start_r < finish_r:
                yield start_r
                start_r -= step_r
        else:
            print('ERROR step = 0')

    def number_counter(*args):#счетает количество аргументов
        if len(args) == 3:
            temp_number = cor_range(args)
        yield temp_number

    temp_my_range = number_counter(args)
    yield temp_my_range

      
for i in my_range(1, 10, 2):
    print(i)
