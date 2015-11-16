#coding=utf8
"""
# Author: quheng
# Created Time : Sun Oct 25 11:03:43 2015
"""
import cv2
import numpy as np
import pylab
import pickle
def grab_cut(img, show = 1):
    """
    img Numpy
    """
    mask = np.zeros(img.shape[:2], dtype = np.uint8)
    bgdmodel = np.zeros((1, 65), np.float64)
    fgdmodel = np.zeros((1, 65), np.float64)
    output = np.zeros(img.shape, np.uint8)
    rect = (int(img.shape[1] * 0.02), int(img.shape[1] * 0.02), int(img.shape[1] * 0.98) , int(img.shape[0] * 0.98))
    cv2.grabCut(img, mask, rect, bgdmodel, fgdmodel, 2, cv2.GC_INIT_WITH_RECT)
    mask = np.where( (mask == 1) + (mask == 3), 255, 0).astype('uint8')

    #使用开运算和闭运算去掉图像中的孤立点和空洞
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    output = cv2.bitwise_and(img, img, mask = mask)
    print "finish"
    if (show == 1):
        pylab.imshow(output)
        pylab.show()
    return output, mask

def edge_detec(img):
    print "start edge detect"
    edge_x = []
    edge_y = []
    def check_pix(x, y):
        """
        判断(x, y)是否是背景
        True   是背景
        False  不是背景
        """
        return any((img[x][y] == [0,0,0]))

    def check_edge(x, y):
        """
        判断(x, y)是否是边缘
        判断依据，同时出现背景和前景的点被认为是边缘
        True   是边缘
        False  不是边缘
        """
        #有一个是背景(True) back 便是True
        back = check_pix(x - 1, y - 1) or check_pix(x - 1, y) or check_pix(x - 1, y + 1) or \
                check_pix(x + 1, y - 1) or check_pix(x + 1, y) or check_pix(x + 1, y + 1) or \
                check_pix(x, y - 1) or check_pix(x, y + 1)
        #有一个是前景(False) fore 便是True
        fore = not(check_pix(x - 1, y - 1) and check_pix(x - 1, y) and check_pix(x - 1, y + 1) and \
                check_pix(x + 1, y - 1) and check_pix(x + 1, y) and check_pix(x + 1, y + 1) and \
                check_pix(x, y - 1) and check_pix(x, y + 1))
        return (back and fore) #背景前景同时出现

    width, height = img.shape[:2]
    for i in xrange(1, width - 1):
        for j in xrange(1, height - 1):
            if (check_edge(i, j)):
                edge_x.append(i)
                edge_y.append(j)
    print "finish"
    edge = np.zeros((2, len(edge_x)))
    edge[0,:] = edge_x
    edge[1,:] = edge_y
    pylab.scatter(edge[1, :],edge[0, :])
    pylab.show()
    return edge

def center_detec(edge):
    print edge.shape[1]
    x = np.sum(edge[0,:])/edge.shape[1]
    y = np.sum(edge[1,:])/edge.shape[1]
    return x,y

def work():
    img = cv2.imread("test3.jpg")
    img, mask= grab_cut(img)
    edge = edge_detec(mask)
    #使用pickle保存中间结果， 加快运算
    pickle.dump(img, temfile)
    pickle.dump(mask, temfile)
    pickle.dump(edge, temfile)
    x, y = center_detec(edge)
    #pylab.scatter(y, x)


def read():
    f = open("test_res.txt","w+")
    img = pickle.load(temfile)
    mask = pickle.load(temfile)
    edge = pickle.load(temfile)
    pylab.imshow(img)
    pylab.show()
    np.set_printoptions(threshold='nan')
    print mask
    f.write(mask)
    f.close()

if __name__ == "__main__":
    temfile = open('tem.pkl', 'r+')
    work()

