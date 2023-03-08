def pass_value(boy,girl):
    f=open("love.txt","a+")
    f.write(f"${boy} -> ${girl}")
    f.write("\n")
    f.close()

def find(boy,girl):
    boy_sum = 0
    girl_sum = 0
    for i in boy:
        temp = ord(i)
        if(temp>=65 and temp<=90):
            boy_sum += (temp+32)
        elif(temp>=97 and temp<=122):
            boy_sum += temp
        else:
            boy_sum += 0
    
    for i in girl:
        temp = ord(i)
        if(temp>=65 and temp<=90):
            girl_sum += (temp+32)
        elif(temp>=97 and temp<=122):
            girl_sum += temp
        else:
            girl_sum += 0
    
    return (boy_sum+girl_sum)%101

def message(love):
    if(love>80):
        return "Perfect Match"
    elif love>60:
        return "Good Match"
    elif love>40:
        return "Average Match"
    elif love>20:
        return "Not a Good Match"
    return "Not a Match"