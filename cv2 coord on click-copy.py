import cv2
import matplotlib.pyplot as plt
import pandas as pd
# function to display the coordinates of
# of the points clicked on the image
xv,yv=[],[]
varb0='BB0_2022-12-02-100945-0000-1'
varb=varb0[:]
pth='P:/Hak Molecular/HA452_Molecular/Microscopy/PC/Contour/Analysed/2_12_22/BB/0/'+str(varb) 
print(pth+'-anot.jpg')#15-anot-py.jpg'

def click_event(event, x, y, flags, params):
    
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
 
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)
        xv.append(x)
        yv.append(y)
 
        # displaying the coordinates
        # on the image window
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        #font = cv2.FONT_HERSHEY_SIMPLEX
        #cv2.putText(img, str(x) + ',' +
         #           str(y), (x,y), font,
          #          1, (255, 0, 0), 2)
        
        cv2.imshow('image', img)
        cv2.imwrite(pth+'-anot.jpg',img)
 
    # checking for right mouse clicks    
    if event==cv2.EVENT_RBUTTONDOWN:
        #xv,yv=[],[]
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)
        xv.append(x)
        yv.append(y)
 
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        cv2.putText(img, str(b) + ',' +
                    str(g) + ',' + str(r),
                    (x,y), font, 1,
                    (255, 255, 0), 2)
        cv2.imshow('image', img)
    #return(xv,yv)
    

# driver function
if __name__=="__main__":
 
    # reading the image
    img = cv2.imread(pth+'.jpg')
    scale_percent = 200 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    
    
    img = cv2.resize(img, dim) 
    img = img[:,:]
    # displaying the image
    cv2.imshow('image', img)
 
    # setting mouse handler for the image
    # and calling the click_event() function
    cv2.setMouseCallback('image', click_event)
 
    # wait for a key to be pressed to exit
    cv2.waitKey(0)
 
    # close the window
    cv2.destroyAllWindows()
df=pd.DataFrame(list(zip(xv,yv)),columns=['X','Y'])
df.to_csv(pth+'.csv')
























'''
img = cv2.imread('P:/Hak Molecular/HA452_Molecular/Microscopy/PC/Contour/Analysed/4_11_22/Top/0/15.jpg',)
scale_percent = 200 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)


img = cv2.resize(img, dim) 
img = img[:500,:500]
#cv2.rectangle(img,(142,130),(313,278),(0,255,0),3)
# displaying the image
cv2.imshow('image', img)

cv2.waitKey(0)
 
    # close the window
cv2.destroyAllWindows()
'''
#print(img/256)