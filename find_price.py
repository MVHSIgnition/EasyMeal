import numpy as np

#y = mx + b
#contains functions for predicted price of next restaurant given trends
#
#mvhs iot club

def find_m_and_b(xs,ys):
    #finds line of best fit for given set of points
    #
    #xs, numpy array of x values
    #ys, numpy array of corresponding y values
    #returns m and b of line of best fit (lobf)
    m = ( (np.mean(xs)*np.mean(ys) - np.mean(xs*ys)) /
          (np.mean(xs)**2 - np.mean(xs*xs)) )
    b = np.mean(ys) - m*np.mean(xs)
    return m, b

def find_accuracy(xs,ys,m,b):
    #returns accuracy of line of best fit compared to known points
    #xs, numpy array of x values
    #ys, numpy array of corresponding y values
    #m, slope (float/int) of line of best fit
    #b, y-intercept of line of best fit
    mse_flat, mse_lobf = [],[]
    mean_y = np.mean(ys)

    for i,x in enumerate(xs):
        mse_flat.append( (ys[i]-mean_y)**2)
        mse_lobf.append( (ys[i] - (x*m + b)) **2)
    
    acc = 1 - ( np.mean(mse_lobf) / np.mean(mse_flat) )
    if np.isnan(acc):
        acc = 1
    return acc

def find_best_next(xs,ys):
    #finds the line of best fit that would best predict next value
    #xs, numpy array of x values
    #ys, numpy array of corresponding y values
    #xs and ys must have at least 5 indicies
    #returns next predicted value
    best_acc = 0
    best_line = (0,0)
    for current_start in range(xs.size-3, 0, -1):
        m,b = find_m_and_b(xs[current_start:-1],ys[current_start:-1])
        acc = find_accuracy(xs[current_start:-1],ys[current_start:-1],m,b)
        if acc >= best_acc:
            best_acc = acc
            best_line = (m,b)
    pred = (xs.size+1)*best_line[0] + best_line[1]
    if pred < 1:
        pred = 1
    elif pred > 4:
        pred = 4
    pred = round(pred)
    return int(pred)

if __name__ == "__main__":
    x_vals = np.array([1,2,3,4,5,6,7,8,9,10])
    y_vals = np.array([1,2,2,1,1,2,2,3,3,3])
    pred = find_best_next(x_vals,y_vals)
    print(pred)
