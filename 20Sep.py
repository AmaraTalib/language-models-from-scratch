

'''def average(marks):
    total=sum(marks)
    count=len(marks)
    print("Count:",count)
    print("Total:",total)
    return total/count

scores=[12,15,17,18,19]
print("Average:",average(scores))'''

def highest(scores):
    return max(scores)

def count_pass(scores):
    print("Score less than 50:")
    for i in scores:
        if i < 50:      #returns the score which is less than 50
           print(i)
        

scores=[23,56,78,19,80,45,71,90]

print("Highest Score:",highest(scores))
count_pass(scores)      #call the function

