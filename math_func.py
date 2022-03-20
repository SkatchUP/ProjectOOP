def imt():
    weight = int(input('Введите свой вес в кг: '))
    height = int(input('Введите свой рост в см: ')) 
    imt_result = weight / (height / 100) ** 2
    print(f'{imt_result:.1f}')


imt()
