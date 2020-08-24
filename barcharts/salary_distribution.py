import matplotlib.pyplot as plt 
import numpy as np 

if __name__ == '__main__':
    indexs = np.arange(0,10)
    w = 0.25  # this is use for separate bars


    pro_sal = [21762, 14996, 24938, 14110, 16830, 19933, 47714, 23363, 30585, 10091]
    plt.style.use('fivethirtyeight')
    plt.bar(indexs - w, pro_sal, width=w, color='c', label='Programmer salary')

    dev_sal = [48844, 38678, 25683, 35732, 44448, 26494, 49038, 20994, 12354, 10269]
    plt.bar(indexs, dev_sal, width=w, color='#111111', label='Developer salary')

    eng_sal = [37220, 46064, 43766, 37016, 39230, 28315, 28751, 46875, 37049, 39443]
    plt.bar(indexs + w, eng_sal, color='g', width=w, label='Engineer salary')

    plt.xlabel('Indexes')
    plt.ylabel('Salary')
    plt.title('Salary distribution')

    plt.xticks(ticks=indexs, labels=[(x* 2 + 2000) for x in indexs]) # to replace old indexs
    plt.legend()
    plt.tight_layout()
    plt.grid(True)

    plt.savefig('salary.png')

    plt.show() 
