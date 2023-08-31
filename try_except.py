##### first runs the try code, if it raises an error, it runs the except code, 
##### we can have more tan one except, always tarting from specific to general
##### if the try does not raise an error, it runs the else block
##### finally is ran no matter what
try:
    f= open('test.txt')
    file = f.read()
    if f.name =='test.txt':
        raise Exception

except FileNotFoundError as e:
    print(e)
except Exception:
    print('Something went wrong!')

else :
    print(file)
    f.close()
    
finally:
    print('Thank you!')