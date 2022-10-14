import csv
import random



def get_quote(file = "data/mmotivational_quotes.csv"):
    try:
        #Open csv file
        with open(file) as csvfile:
            quotes = [{'author': line[0],
                        'quote': line[1]} for line in csv.reader(csvfile, delimiter='|')]
    except Exception as e:

            quotes = [{'author': 'Albert Einstein',
                        'quote': 'We cannot solve problems with the kind of thinking we employed when we came up with them.'}]



    return random.choice(quotes)



# quote = get_quote()

# print(f'I got a quote: "{quote["quote"]}" by {quote["author"]} ')



