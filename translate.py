from googletrans import Translator
import pandas as pd

# create instance 
translater = Translator()
data = pd.read_csv('text.csv', header=None)
data.columns =['text']
en_list = data.text.values.tolist()
translated_text = []
for i in range(len(en_list)):
    # tramslate each record
    translated_text.append(translater.translate(en_list[i], dest='fr').text)
# Adding to dataframe    
data['Urdu_Translation'] = translated_text
# Storing in csv
data.to_csv('French_translated.csv')
