import os
import pandas as pd

table = pd.read_csv('./csvFiles/Acao_e-mail_UG_COB_2203.csv', sep=";")

emails = table['(E-mail) - E-mail']
emailsT = [ ]
cont = 0
for email in emails:
    findedA = email.find('@')
    
    if findedA != -1:
        findedP = email.find('.', findedA)
        sub = email[findedA:findedP]
        
        if findedP != -1: 
            if sub in emailsT:
                cont += 1

            else:
                cont += 1
                emailsT.append(sub)
            
df = pd.DataFrame(emailsT)
            
df.to_csv('teste.csv')