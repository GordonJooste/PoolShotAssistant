import cv2
import numpy as np
import matplotlib.pyplot as plt # import
import matplotlib.cm

img = cv2.imread('s13.jpg')
imgBGR = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
imgHSV = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
#plt.imshow(imgHSV) #load
#plt.show()  # show the window
#ImgH - 0, 179
#ImgS - 0, 255

imgH = imgHSV[:,:,0]
imgS = imgHSV[:,:,1]

#tel = {'jack': 4098, 'sape': 4139}
#1920 = x  1280 = y

HueBin = {'bin1':0, 'bin2':0, 'bin3':0, 'bin4':0, 'bin5':0, 'bin6':0, 'bin7':0, 'bin8':0, 'bin9':0, 'bin10':0, 'bin11':0, 'bin12':0}
SatBin = {'bin1':0, 'bin2':0, 'bin3':0, 'bin4':0, 'bin5':0, 'bin6':0, 'bin7':0, 'bin8':0, 'bin9':0, 'bin10':0, 'bin11':0, 'bin12':0}

#for y in range(len(imgH)):
#    for x in range(len(imgH[0])):
#      if(imgH[y][x]<15): # && imgS[y][x] < 21 etc and so on.
#            HueBin['bin1'] = HueBin['bin1'] + 1
#        elif (imgH[y][x] < 30):
#            HueBin['bin2'] = HueBin['bin2'] + 1
#        elif (imgH[y][x] < 45):
#            HueBin['bin3'] = HueBin['bin3'] + 1
#        elif (imgH[y][x] < 60):
#            HueBin['bin4'] = HueBin['bin4'] + 1
#        elif (imgH[y][x] < 75):
#            HueBin['bin5'] = HueBin['bin5'] + 1
#        elif (imgH[y][x] < 90):
#            HueBin['bin6'] = HueBin['bin6'] + 1
#        elif (imgH[y][x] < 105):
#            HueBin['bin7'] = HueBin['bin7'] + 1
#        elif (imgH[y][x] < 120):
#            HueBin['bin8'] = HueBin['bin8'] + 1
#        elif (imgH[y][x] < 135):
##            HueBin['bin9'] = HueBin['bin9'] + 1
#        elif (imgH[y][x] < 150):
##            HueBin['bin10'] = HueBin['bin10'] + 1
 #       elif (imgH[y][x] < 165):
#            HueBin['bin11'] = HueBin['bin11'] + 1
#        elif (imgH[y][x] < 180):
#            HueBin['bin12'] = HueBin['bin12'] + 1

#for y in range(len(imgS)):
#    for x in range(len(imgS[0])):
#        if(imgH[y][x]<21):
#            SatBin['bin1'] = SatBin['bin1'] + 1
#        elif (imgH[y][x] < 42):
#            SatBin['bin2'] = SatBin['bin2'] + 1
#        elif (imgH[y][x] < 63):
#            SatBin['bin3'] = SatBin['bin3'] + 1
#        elif (imgH[y][x] < 84):
#            SatBin['bin4'] = SatBin['bin4'] + 1
#        elif (imgH[y][x] < 105):
#            SatBin['bin5'] = SatBin['bin5'] + 1
#        elif (imgH[y][x] < 126):
#            SatBin['bin6'] = SatBin['bin6'] + 1
#        elif (imgH[y][x] < 147):
#            SatBin['bin7'] = SatBin['bin7'] + 1
#        elif (imgH[y][x] < 168):
##            SatBin['bin8'] = SatBin['bin8'] + 1
 #       elif (imgH[y][x] < 189):
#            SatBin['bin9'] = SatBin['bin9'] + 1
#        elif (imgH[y][x] < 210):
#            SatBin['bin10'] = SatBin['bin10'] + 1
#        elif (imgH[y][x] < 231):
#            SatBin['bin11'] = SatBin['bin11'] + 1
 #       elif (imgH[y][x] < 255):
#            SatBin['bin12'] = SatBin['bin12'] + 1


#print('Hue ')
#print(HueBin)
#print('Saturation ')
#print(SatBin)


#plt.bar(range(len(HueBin)), list(HueBin.values()), align='center')
#plt.xticks(range(len(HueBin)), list(HueBin.keys()))
#plt.bar(range(len(SatBin)), list(SatBin.values()), align='center')
#plt.xticks(range(len(SatBin)), list(SatBin.keys()))
#plt.show()

def incRep(list,pos):
  #  print(list)
  #  print(pos)
  #  print()
    tmp = list
    val = list[pos] +1
    tmp.insert(pos,val)
    tmp.remove(pos+1)
    return tmp

#          0  1  2  3  4   5   6   7   8   9   10  11
SatLbl = [21,42,63,84,105,126,147,168,189,210,231,255]
#          0  1  2  3  4  5  6   7   8   9   10  11
HueLbl = [15,30,45,60,75,90,105,120,135,150,165,180]
# 12 x 12, ie each list is 12 long because each list is the saturation values
Hist = {'h1': {'s1':0,'s2':0,'s3':0,'s4':0,'s5':0,'s6':0,'s7':0,'s8':0,'s9':0,'s10':0,'s11':0,'s12':0,}, 'h2':{'s1':0,'s2':0,'s3':0,'s4':0,'s5':0,'s6':0,'s7':0,'s8':0,'s9':0,'s10':0,'s11':0,'s12':0,}, 'h3':{'s1':0,'s2':0,'s3':0,'s4':0,'s5':0,'s6':0,'s7':0,'s8':0,'s9':0,'s10':0,'s11':0,'s12':0,}, 'h4':{'s1':0,'s2':0,'s3':0,'s4':0,'s5':0,'s6':0,'s7':0,'s8':0,'s9':0,'s10':0,'s11':0,'s12':0,}, 'h5':{'s1':0,'s2':0,'s3':0,'s4':0,'s5':0,'s6':0,'s7':0,'s8':0,'s9':0,'s10':0,'s11':0,'s12':0,}, 'h6':{'s1':0,'s2':0,'s3':0,'s4':0,'s5':0,'s6':0,'s7':0,'s8':0,'s9':0,'s10':0,'s11':0,'s12':0,}, 'h7':{'s1':0,'s2':0,'s3':0,'s4':0,'s5':0,'s6':0,'s7':0,'s8':0,'s9':0,'s10':0,'s11':0,'s12':0,},'h8':{'s1':0,'s2':0,'s3':0,'s4':0,'s5':0,'s6':0,'s7':0,'s8':0,'s9':0,'s10':0,'s11':0,'s12':0,},'h9':{'s1':0,'s2':0,'s3':0,'s4':0,'s5':0,'s6':0,'s7':0,'s8':0,'s9':0,'s10':0,'s11':0,'s12':0,},'h10':{'s1':0,'s2':0,'s3':0,'s4':0,'s5':0,'s6':0,'s7':0,'s8':0,'s9':0,'s10':0,'s11':0,'s12':0,}, 'h11':{'s1':0,'s2':0,'s3':0,'s4':0,'s5':0,'s6':0,'s7':0,'s8':0,'s9':0,'s10':0,'s11':0,'s12':0,}, 'h12':{'s1':0,'s2':0,'s3':0,'s4':0,'s5':0,'s6':0,'s7':0,'s8':0,'s9':0,'s10':0,'s11':0,'s12':0,},}

for y in range(len(imgH)):
    for x in range(len(imgH[0])):
        if(imgH[y][x]<15):
            if (imgS[y][x] < 21):
                cur = Hist['h1']['s1']
                Hist['h1']['s1'] = cur+1
            elif (imgS[y][x] < 42):
                cur = Hist['h1']['s2']
                Hist['h1']['s1'] = cur+1
            elif (imgS[y][x] < 63):
                cur = Hist['h1']['s3']
                Hist['h1']['s1'] = cur+1
            elif (imgS[y][x] < 84):
                cur = Hist['h1']['s4']
                Hist['h1']['s1'] = cur + 1
            elif (imgS[y][x] < 105):
                cur = Hist['h1']['s5']
                Hist['h1']['s1'] = cur + 1
            elif (imgS[y][x] < 126):
                cur = Hist['h1']['s6']
                Hist['h1']['s1'] = cur + 1
            elif (imgS[y][x] < 147):
                cur = Hist['h1']['s7']
                Hist['h1']['s1'] = cur + 1
            elif (imgS[y][x] < 168):
                cur = Hist['h1']['s8']
                Hist['h1']['s1'] = cur + 1
            elif (imgS[y][x] < 189):
                cur = Hist['h1']['s9']
                Hist['h1']['s1'] = cur + 1
            elif (imgS[y][x] < 210):
                cur = Hist['h1']['s10']
                Hist['h1']['s1'] = cur + 1
            elif (imgS[y][x] < 231):
                cur = Hist['h1']['s11']
                Hist['h1']['s1'] = cur + 1
            elif (imgS[y][x] < 255):
                cur = Hist['h1']['s12']
                Hist['h1']['s1'] = cur + 1
        elif (imgH[y][x] < 30):
            if (imgS[y][x] < 21):
                cur = Hist['h2']['s1']
                Hist['h2']['s1'] = cur+1
            elif (imgS[y][x] < 42):
                cur = Hist['h2']['s2']
                Hist['h2']['s1'] = cur+1
            elif (imgS[y][x] < 63):
                cur = Hist['h2']['s3']
                Hist['h2']['s1'] = cur+1
            elif (imgS[y][x] < 84):
                cur = Hist['h2']['s4']
                Hist['h2']['s1'] = cur + 1
            elif (imgS[y][x] < 105):
                cur = Hist['h2']['s5']
                Hist['h2']['s1'] = cur + 1
            elif (imgS[y][x] < 126):
                cur = Hist['h2']['s6']
                Hist['h2']['s1'] = cur + 1
            elif (imgS[y][x] < 147):
                cur = Hist['h2']['s7']
                Hist['h2']['s1'] = cur + 1
            elif (imgS[y][x] < 168):
                cur = Hist['h2']['s8']
                Hist['h2']['s1'] = cur + 1
            elif (imgS[y][x] < 189):
                cur = Hist['h2']['s9']
                Hist['h2']['s1'] = cur + 1
            elif (imgS[y][x] < 210):
                cur = Hist['h2']['s10']
                Hist['h2']['s1'] = cur + 1
            elif (imgS[y][x] < 231):
                cur = Hist['h2']['s11']
                Hist['h2']['s1'] = cur + 1
            elif (imgS[y][x] < 255):
                cur = Hist['h2']['s12']
                Hist['h2']['s1'] = cur + 1

print(Hist)
#clamped_hue = map(lambda h: max(hue_min, min(h, hue_max)), im_hue)
#mask = (imgH < 20) & (imgS > 200)
#imgHSV[mask] = 0
#print(np.max(imgS))
#plt.imshow(imgHSV)
#plt.show()