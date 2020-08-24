import pandas as pd 
import matplotlib.pyplot as plt

if __name__ == '__main__':

    data = pd.read_csv('fills plots\data.csv')
    ages = data.Age
    all_devs = data.All_Devs
    python = data.Python
    javascript = data.JavaScript

    plt.plot(ages, all_devs, color='#444444', linestyle='--', label='All Devs')
    medium = 42000

    plt.fill_between(ages, python, all_devs, where=(python > all_devs), alpha=0.5, interpolate=True, label='Above avg')
    plt.fill_between(ages, python, all_devs, where=(python<= all_devs), alpha=0.35, color='red', interpolate=True, label='Below avg')
    plt.plot(ages, python, label='Python')

    plt.legend()

    plt.xlabel('Ages')
    plt.ylabel('Medium salary')
    plt.title('Developers salary')
    
    plt.tight_layout()

    plt.show()
