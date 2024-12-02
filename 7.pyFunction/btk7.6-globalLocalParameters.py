x  = 'global x '                        # defined global scope working area 

def function():
        x = 'local x '                  # defined local scope working area
        print(x)

function()                              # working on global area, it does not change the output as 'local x'
print(x)



name = 'global string'

def greeting():
        #name = 'mehmet'

        def hello():
                #name = 'cengiz'
                print(f'hello {name}')  #The value 'name' calls the function in the upper indent
        
        hello()

greeting()



x = 50
def test(x):
        print(f'x: {x}')

        x = 100
        print(f'changed x to {x}')
        return x 

test(x)
print(x)