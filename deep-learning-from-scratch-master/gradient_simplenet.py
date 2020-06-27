# coding: utf-8
import sys, os

import numpy as np
from common1 import functions as func
from common1 import gradient as grad


class simpleNet:
    def __init__(self):
        self.W = np.random.randn(2,3) # 정규분포로 초기화
        
    def predict(self, x):
        return np.dot(x, self.W)

    def loss(self, x, t):
        z = self.predict(x)
        y = func.softmax(z)
        loss = func.cross_entropy_error(y, t)

        return loss

x = np.array([0.6, 0.9])
t = np.array([0, 0, 1])

net = simpleNet()

f = lambda w: net.loss(x, t)
dW = grad.numerical_gradient(f, net.W)

print(dW)
