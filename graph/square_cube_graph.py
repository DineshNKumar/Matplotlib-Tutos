import matplotlib.pyplot as plt

if __name__ == '__main__':

    plt.style.use('fivethirtyeight')

    a = [x for x in range(1,11)]
    b = [x**2 for x in a]

    plt.plot(a, b,color='#244332', linestyle='--',linewidth='2', marker='o', label='Square')

    c = [x ** 3 for x in a]
    plt.plot(a, c, color='c', marker='o', linewidth = '1' ,label='Cube')

    plt.xlabel('Numbers')
    plt.ylabel('Square and Cube')
    plt.title('Mathematics operation')

    plt.legend()
    plt.tight_layout()
    plt.grid(True)
    plt.savefig('name.png') # save the graph in png image
    plt.show()
