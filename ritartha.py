
import os
def InitiateKAGGLE(kaggle_api):
  check = 0
  c = os.system('wget -O kaggle.json https://drive.google.com/u/0/uc?id=1y-EADUNoADz3n1A-PEH2_8zjbK1kZGVY&export=download')
  if c == 0:
    check = check+1
    print('#### 1.LOADED kaggle.json FROM G-DRIVE---->')
  c = os.system('pip install -q kaggle')
  if c == 0:
    check = check+1
    print('#### 2. INSTALLED KAGGLE---->')
  c = os.system('mkdir ~/.kaggle')
  if c == 0:
    check = check+1
    print('#### 3. kaggle DIR CREATED---->')
  c = os.system('cp /content/kaggle.json ~/.kaggle/')
  if c == 0:
    check = check+1
    print('#### 4. kaggle.json MOVED TO .kaggle DIR---->')
  c = os.system('chmod 600 ~/.kaggle/kaggle.json')
  if c == 0:
    check = check+1
    print('#### 5. kaggle.json PERMISSION CHANGED---->')
  c = os.system(kaggle_api)
  if c == 0:
    check = check+1
    print('#### 6. DOWNLOADED DATASET AS .zip file FROM KAGGLE---->')
  if check == 6:
    print('DATA DOWNLOADED FROM KAGGLE SUCCESSFULLY') 
  else:
    print('KAGGLE DATA NOT DOWNLOADED....CHECK THE STEPS')   
  return None

s = '''
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
█░░║║║╠─║─║─║║║║║╠─░░█
█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
'''
print(s)
