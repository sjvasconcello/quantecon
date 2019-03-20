
# Data
x_vals = [3,5,2,6,2]
y_vals = [4,7,3,2,3]
pairs = ((2, 5), (4, 2), (9, 8), (12, 10))

def exercise1_1(xv,yv):
    return print(sum([x*y for x,y in zip(xv,yv)]))

def exercise1_2():
    return print(sum([x % 2 == 0 for x in range(100)]))

def exercise1_3(pairs):
    return print(sum([ x % 2 == 0 and y % 2 == 0 for x,y in pairs]))

def polynomial(x, coeff):
    return print(sum(a * x**i for i,a in enumerate(coeff) ))

def capitals_letters(word):
    capital = 0
    for letter in word:
        if letter == letter.upper() and letter.isalpha():
            capital += 1
        return capital

def seq(seq_a, seq_b):
    is_subset = True
    for a in seq_a:
        if a not in seq_b:
            is_subset = False
    return is_subset
#== test ==#

def seq2(seq_a, seq_b):
    return set(seq_a).issubset(set(seq_b))

def linapprox(f,a,b,n,x):
    length_of_interval = b - a
    num_subintervals = n - 1
    step = length_of_interval / num_subintervals
    point = a
    while point <= x:
        point += step
    u, v = point - step, point


exercise1_1(x_vals, y_vals)
exercise1_2()
exercise1_3(pairs)
polynomial(3,(2,4))
capitals_letters('geragERQHerwgWQEFqweGWERqfer')

print(seq([1,3],[1,3,4]))
print(seq([1,3,6],[1,4]))
