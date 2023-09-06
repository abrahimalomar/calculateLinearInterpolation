
import numpy as np

data=np.array(
    [
        [-6, -7],
        [-2, -1],
        [ 2,  5],
        [ 8,  14],
        [ 16, 26]
    ]
)


def calculateLinearInterpolation(data):
    while True:
        Xinput = int(input("Enter your x: "))
        Xvalues = data[:, 0]
        Yvalues = data[:, 1]
        y1 = Yvalues[-2]
        y2 = Yvalues[-1]
        y = y2 - y1
        x1 = Xvalues[-2]
        x2 = Xvalues[-1]
        x = x2 - x1

        slope = y / x

        intercept = Yvalues[-1] - slope * Xvalues[-1]

        result_y = slope * Xinput + intercept
        print('Result: ', result_y)
        if Xinput == 0:
            break

calculateLinearInterpolation(data)
