numbers=[0,5,15,6,-5,9,-1,5,5]



for index, elem in enumerate(numbers) :
    if elem < 0 and elem >= -1 :
        print(f'Найбільший відьємний елемент у списку: {elem}, його індекс {index}')