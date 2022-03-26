def fiborabbit(month, age):

    generation = [0]*age                    
    generation[0], generation[1] = 0,1          # number of rabbit live during a generation

    for x in range(2,month): 
        temp = list(generation)
        generation[0] = sum(generation[1:])     # number of new born rabbit
        for i in range(1,age): 
            generation[i] = temp[i-1]
    return sum(generation)                      # sum of all the rabit

out =  fiborabbit(85,19)
print(out)