import numpy as np

# en ust veri tipini kullanir "dtype"

#x = np.array([2.2 , 3.3 , 16])
#np.save('deneme_1', x)


"""y = np.load('deneme_1.npy')
print(y)"""

"""z = np.array([1, 2, 3], dtype=np.float128)

z = z.astype(np.complex128)

print(z)
"""



#npzeros & npones




"""
x1 = np.zeros(3) #dtype = float64
x2 = np.ones(3)
print(x1)
print(x2)

"""  
"""
y1 = np.zeros((2,3,4),dtype=np.int) #2 liste, 3X4 matrix(3 satir, 4 sutun)
print(y1)
"""
"""
y2= np.full((2,3), 10) # int32(10 dedigimiz icin )
print(y2)

"""

# np.empty() , np.fill
"""
x = np.empty((2,2))

print(x)
"""
# 2, 2 matrix olusturup rasgele deger koydu
"""
x.fill(3)
print(x)
"""
# gelisi duzel degerleri 3 le doldurrdu

# np.eye()  np.identity
"""
x = np.eye(4) # 4X4 luk BIRIM matirx olusturrur

y= np.eye((5,4)) #5X4 luk birim matrix olusturur


z = np.eye(4, k = 1) #matrixi 1 birim diyogenali sag a aldi

c = np.eye(4, k=-2) # matrixin diyogenalini 2 brim sola aldi 

x = np.identity(5) #5X5 lik birim matrix olusturur
"""

# np.diag()
"""
x= np.diag(4,7,11,3 ) #4X4 luk matrixin A11=4 B22=7 c33=11 d44=3 olacak sekilde verir
print(x)


"""


#####################################

#np.arange()

""" 
x = np.arange(5) # 0,1,2,3,4     1X4 luk matrix

y = np.range(4,9) # 4,5,6,7,8   1X5 luk matrix

z= np.range(3,23,4) #3,7,11,15,19 # 23 degerinni alabilir AMA SON DEGER OLDUGU ICIN ALMICAK 


"""

#NP.LINSPACE (BASLANGIC,BITIS,KAC CIKTI ISTEGIMIZI DEGER) varsayilan eleman sayisi N=50
"""
x = np.linspace(0,15,10 ) #0 ve 15 dahil 10 tane deger verir

y = np.linspace(0,15, endpoint=False) #son elemani almaz

"""

#np.reshape()
"""
x = np.arange(20 ) #20 elemanli bos bir 1X20 lik matix 20 dalil degil

y = np.reshape(x, (4,5)) # 4X5 lik matrix olusturur

y = np.reshape(x, (2,5,5)) #iki tane 5X5 lik matrix

y = np.reshape(x,(2,10)) # 2X10 luk matrixe cevirrir

z = np.linspace(0,19.20) .reshape(2,10)
"""


#random.random[0,1)
"""

x = np.random.random((2,3)) #2X3 luk random matrix

x = np.random.randint(3,12, size=(3,2)) #3X2 lik matrix olusturup icini 3ile12 arasi random doldurr




"""
#################

https://youtu.be/M-SOsuaLGe4