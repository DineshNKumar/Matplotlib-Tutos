import csv
import matplotlib.pyplot as plt 
import numpy as np 
from collections import Counter

if __name__ == "__main__":
    with open('barcharts\dev_data.csv') as csv_file:
        f = csv.DictReader(csv_file)
        lang_count = Counter()
        for data in f:
            lang_count.update(data['LanguagesWorkedWith'].split(';'))        
    
    languages = []
    popularity = []

    for item in lang_count.most_common(15):
        languages.append(item[0])
        popularity.append(item[1])
    
    # plt.bar(languages, popularity)

    languages.reverse()
    popularity.reverse()

    plt.xlabel('Languages')
    # plt.ylabel('Number of pupile who use')
    plt.title('Popular languages')

    plt.barh(languages, popularity, color='#004f35')

    plt.savefig('barcharts\programmer.png')
    plt.tight_layout()
    plt.show()
