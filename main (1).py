flower = input("Type a flower name: ")

#here is the conditions according to the input
if flower == 'Spathiphyllum':
    print("Spathiphyllum is the best plant ever!")
elif flower == 'spathiphyllum':
    print('No, I want a big Spathiphyllum!')
elif flower != 'Spathiphyllum' and flower != 'spathiphyllum':
    print('Spathiphyllum! Not ', flower, ' ! ')