print("\nNormal Pyramid\n")
for i in range(5):
    x='*'
    x=x*i
    print(f'{x:^10}')


print("\nInvert Pyramid\n")
for i in range(5):
    x='*'
    x=x*(5-i)
    print(f'{x: ^10}')
