
colors = ['azul', 'amarelo', 'vermelho','preto', 'branco', 'verde']
#iterate over a list keeping track of the index
for index, item in enumerate(colors, start=4):
    print(index, item)

lusofonia = {"AmÃ©rica do Sul": "Brasil", "Europa": "Portugual", "Ãfrica":"Angola", "Ãsia":"Macau" }

for  key, region in lusofonia.items():
    print(f'the region is {key} and {region}')

### an easy function to generate squares
def square():
    i=1
    while i<10:
        yield i*i
        i+=1

for value in square():
    print(value)

#break gets out of the loop and continues to the following code
# continue goes directly to the next iteration
#yield returns a value but saves the state where it left the function for the next time it will start running from where it stopped
