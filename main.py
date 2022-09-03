import pandas as pd

data = pd.read_csv('test_data.csv')

data['greeting']=''
data['introducing']=''
data['company']=''
data['goodbye']=''

#greeting
for dlg_id in range(max(data['dlg_id'])+1):
 for ind in data[(data['role']=='manager') & (data['dlg_id']==dlg_id)].index:
  if 'здравствуйте'  in data['text'].iloc[ind].lower() or 'добрый день' in data['text'].iloc[ind].lower():
    print(data['text'].iloc[ind])
    #data['greeting'].iloc[ind]=True
    data.loc[ind,['greeting']] = True
    print(data['greeting'].iloc[ind])

print(data[data['greeting']==True][['text','greeting']])

#introduce
for dlg_id in range(max(data['dlg_id'])+1):
 for ind in data[(data['role']=='manager') & (data['dlg_id']==dlg_id)].index:
  if 'зовут'  in data['text'].iloc[ind].lower():
    print(data['text'].iloc[ind])
    data.loc[ind,['introducing']]=True
    print(data['introducing'].iloc[ind])

print(data[data['introducing']==True][['text','introducing']])

#company
for dlg_id in range(max(data['dlg_id'])+1):
 for ind in data[(data['role']=='manager') & (data['dlg_id']==dlg_id)].index:
  if ('компания'  in data['text'].iloc[ind].lower()) & (data['line_n'].iloc[ind]<10):
    print(data['text'].iloc[ind])
    data.loc[ind,['company']]=True
    print(data['company'].iloc[ind])

print(data[data['company']==True][['text','company']])

#goodbye
for dlg_id in range(max(data['dlg_id'])+1):
 for ind in data[(data['role']=='manager') & (data['dlg_id']==dlg_id)].index:
  if 'до свидания'  in data['text'].iloc[ind].lower() or 'всего доброго'  in data['text'].iloc[ind].lower():
    print(data['text'].iloc[ind])
    data.loc[ind,['goodbye']]=True
    print(data['goodbye'].iloc[ind])

print(data[data['goodbye']==True][['text','goodbye']])

data.to_csv('result.csv', index=False)