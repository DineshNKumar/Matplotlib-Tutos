import matplotlib.pyplot as plt 

if __name__ == "__main__":
    # print(plt.style.available)
    plt.style.use('fivethirtyeight')

    minuts = [1,2,3,4,5,6,7,8,9]

    p1 = [1,2,3,3,4,4,4,4,5]
    p2 = [1,1,1,1,2,2,2,3,4]
    p3 = [1,1,1,2,2,2,3,3,3]

    labels = ['P1', 'P2', 'P3']
    colors = ['#ade4a4', '#de34a5', '#e45a44']

    plt.stackplot(minuts, p1, p2, p3, labels=labels, colors=colors)
    
    plt.legend(loc='upper left')
    plt.tight_layout()
    plt.title('Stack plot')

    plt.savefig('stack.png')
    plt.show()
