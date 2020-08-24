import matplotlib.pyplot as plt 


# atmosphere gas

if __name__ == '__main__':
    plt.style.use('fivethirtyeight')
    p = [38984, 36545, 31363, 24028, 23558, 21180, 17879]
    l = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Bash/Shell/PowerShell', 'C#']
    explode = [0, 0, 0, 0.4, 0, 0 ,0]

    plt.pie(p, labels=l, explode=explode, shadow=True, startangle=90,autopct='%1.1f%%', wedgeprops={'edgecolor':'black'})
    
    plt.tight_layout(rect=(0,0,0,1))
    plt.savefig('pie.png')
    plt.show()
