import numpy as np

def main() :
    Score = np.random.randint(100, size = (10, 4))
    Q1(Score)
    print("-------------------------")
    Q2(Score)
    print("-------------------------")
    Q3(Score)
    print("-------------------------")
    Q4(Score)
    print("-------------------------")
    Q5(Score)

# Difference betweeen (n, ) and (n, 1) : (n, 1) is 2D but (n,) is 1D

def Q1(s) :
    m = np.array(s.mean(axis = 0))  # calculate mean value based on column  
    m = m.reshape(-1, 4) # reshape m to use concatenate func
    res = np.concatenate([s, m], axis = 0)  # axis = 0 >> column
    print(res)

def Q2(s) :
    # ASCII 65 ~ 68(A ~ D)
    # convert value to ASCII integer value
    s = np.where(s < 70, 68, s)
    s = np.where((s >= 70) & (s < 80), 67, s)
    s = np.where((s >= 80) & (s < 90), 66, s)
    s = np.where((s >= 90), 65, s)

    res = []
    # convert int to ASCII by using chr function & double for loop
    for i in range(len(s)) :
        tmp = []
        for j in range(len(s[i])) :
            tmp.append(chr(s[i][j]))    
        res.append(tmp)
    
    # convert array to numpy array
    res = np.array(res)

    print(res)

def Q3(s) :
    # use numpy's  broadcasting 
    m = np.array(s.mean(axis = 0))
    print(s - m)

def Q4(s) :
    # calculate mean value based on column 
    m = np.array(s.mean(axis = 0))  
    # reshape m to use concatenate func 
    m = m.reshape(-1, 4) 
    # concatenate based on column
    res = np.concatenate([s, m], axis = 0)  

    # calculate total by using sum func
    tmp = np.sum(res, axis = 1)
    # reshape tmp to use concatenate func
    tmp = tmp.reshape(11, -1)
    # concatenate based on row
    res2 = np.concatenate([res, tmp], axis = 1)

    print(res2)

def Q5(s) :
    # calculate mean value based on column 
    m = np.array(s.mean(axis = 0))  
    # reshape m to use concatenate func 
    m = m.reshape(-1, 4) 
    # concatenate based on column
    res = np.concatenate([s, m], axis = 0)  

    # calculate total by using sum func
    tmp = np.sum(res, axis = 1)
    # reshape tmp to use concatenate func
    tmp = tmp.reshape(11, -1)
    # concatenate based on row
    res2 = np.concatenate([res, tmp], axis = 1)
    # calculate mean value based on row 
    fin = np.array(res2[:, :-1].mean(axis = 1))
    # reshape fin to use concatenate func
    fin = fin.reshape(11, -1)
    # concatenate based on row
    result = np.concatenate([res2, fin], axis = 1)

    print(result)

main()