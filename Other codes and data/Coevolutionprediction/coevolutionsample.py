#this code contains three classes of gentic algorithms, individauls , population and predictors
import math
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA

# import some data to play with




import numpy as np
import urllib
mutation=0.1
maxind=40
input_num=4
class_num=2
opsize=int(math.ceil(math.log(class_num,2))+1+3+math.ceil(math.log(input_num,2)))
individual_size=opsize*maxind

trainersnum=6000
class individual:

    def __init__(self,size1):
        self.set=1
        self.fit=-1
        
        while(1):
            self.item=[]
            for x in range(0, size1):
                while(1):
                    self.newk=[]
                    for zzx in range(0,opsize):
                        self.newk.append(random.randint(0,1))
                    if(decoder.validate2(self.newk)==1):
                        break
                    
                
                self.item.extend(self.newk)
            if(decoder.validate(self)==1):
                break
            
    def __str__( self ):
        return str(self.item)
    def copy( self ):
        hind=individual(self.size()/opsize)
        #hind.fit=self.fit
        for x in range(0, self.size()):
            hind.item[x]=self.item[x]
        
        return hind
    def size( self ):
        return len(self.item)
class population:
    def copy( self ):
        self.hpop=[]
        for x in range(0, self.size()):
            self.hpop.item[x]=self.item[x].copy()
        return self.hpop
    def __init__(self,size):
        self.size1=size
        self.item=[]
        for x in range(0, size):
            print("preparing:  "+str(x)+"%")
            self.item.append(individual(random.randint(1,20)))
            #self.item.append(individual(4))
    def size(self):
        return self.size1
    def __str__( self ):
        k=""
        for x in range(0,self.size()):
            k+=str(self.item[x])
        return k
class genteics:
    @classmethod
    def crossover(self,item1,item2):
        hcross=item1.copy()
        kcross= item2.copy()
        
        while(1):
            h1=[]
            k1=[]
            index1=random.randint(0,item1.size()/opsize)
            for i in range(0,5):
                index11=random.randint(index1,item1.size()/opsize)
                if(index11>index1):
                    break
            
            
            index2=random.randint(0,item2.size()/opsize)
            for i in range(0,5):
                index22=random.randint(index2,item2.size()/opsize)
                if(index22>index2):
                    break

            
            for i in range(0,index1*opsize):
                h1.append(item1.item[i])
            for i in range(index2*opsize,index22*opsize):
                h1.append(item2.item[i])
            for i in range(index11*opsize,item1.size()):
                h1.append(item1.item[i])
                
            for i in range(0,index2*opsize):
                k1.append(item2.item[i])
            for i in range(index1*opsize,index11*opsize):
                k1.append(item1.item[i])
            for i in range(index22*opsize,item2.size()):
                k1.append(item2.item[i])
            
            hcross.item=h1
            kcross.item=k1

            if(decoder.validate(hcross)==1 and decoder.validate(kcross)==1):
                break
            else:
                hcross=item1.copy()
                kcross= item2.copy()
        
        return hcross,kcross
    @classmethod
    def fit3(self,item1):
       if(item1.fit!=200):
            sss1,sss4=decoder.calc(item1)
            

            try:
                #fitness=((math.pow(arrayout[x1][0]-sss1[x1][0],2)) for x1 in range(0,len(sss1)))
                fitness=0.0
                for inx10 in range(0,len(sss1)):
                    fitness=(((fitness*inx10)/(1.0+float(inx10)))+(math.fabs(arrayout[inx10][0]-sss1[inx10][0])/(inx10+1.0)))
            except OverflowError:
                print("OOPS")
                print(len(arrayout))
                print(len(sss1))
                print(sss1[:][0])

    
            item1.fit=fitness#(math.fsum(fitness)/(len(sss1)))
       #     item1.fit=(perc+0.0)/len(sa) 
    @classmethod
    def fit4(self,item1):
       if(item1.fit!=200):
            sss1,sss4=decoder.calc2(item1)
            

            try:
                #fitness=((math.pow(arrayout[x1][0]-sss1[x1][0],2)) for x1 in range(0,len(sss1)))
                fitness=0.0
                for inx10 in range(0,len(sss1)):
                    fitness=(((fitness*inx10)/(1.0+float(inx10)))+(math.fabs(arraytestout[inx10][0]-sss1[inx10][0])/(inx10+1.0)))
            except OverflowError:
                print("OOPS")
                print(len(arrayout))
                print(len(sss1))
                print(sss1[:][0])

    
            item1.fit=fitness#(math.fsum(fitness)/(len(sss1)))
       #     item1.fit=(perc+0.0)/len(sa) 
    @classmethod
    def fit5(self,item1):
       if(item1.fit!=200):
            z=np.arange(-3,3,0.01)
            hh=random.sample(range(0,len(z)),200)
            inputsp=[]
            ouputsp=[]
           
                
            for inx20 in range(0,len(hh)):
                temp=[0.0,1.0,2.0,3.0]
                temp[0]=z[hh[inx20]]
                
                inputsp.append(temp)
                ouputsp.append(originalfit(temp[0]))
            sss1,sss4=decoder.calc4(item1,inputsp)
            

            try:
                
                fitness=0.0
                for inx10 in range(0,len(sss1)):
                    fitness=(((fitness*inx10)/(1.0+float(inx10)))+(math.fabs(ouputsp[inx10]-sss1[inx10][0])/(inx10+1.0)))
            except OverflowError:
                print("OOPS")
                print(len(arrayout))
                print(len(sss1))
                print(sss1[:][0])

    
            item1.fit=fitness
        
    @classmethod
    def fit2(self,item1):
       if(item1.fit!=200):
            sss1,sss4=decoder.calc(item1)

           
            fitness=((math.fsum((math.pow(-1,int(arrayout[x]==x1))*sigmoid(sss1[x][x1])) for x1 in range(0,len(sss1[0])))) for x in range(0,len(sss1)))

    
            item1.fit=(math.fsum(fitness)/(len(sss1)))
       
    @classmethod
    def fit(self,item1):
       if(item1.fit!=200):
           sss1,sss4=decoder.calc(item1)

           
            #fitness=((math.fsum((math.pow(-1,int(arrayout[x]==x1))*sigmoid(sss1[x][x1])) for x1 in range(0,len(sss1[0])))) for x in range(0,len(sss1)))
           lss=[]
           for iss in range(0,len(sss1)):
               zss=[]
               zss=function(sss1[iss])
               lss.append(zss)
    
           
    
           perc=0
          # fitness=(math.pow(float(math.pow(2,int(arrayout[x]==x1)-sigmoid(sss1[x][x1]))) for x1 in range(0,len(sss1[0])))) for x in range(0,len(sss1)))

    
           item1.fit=(math.fsum(fitness)/(len(sss1)*len(sss1[0])))
           sa=classifiall(lss)
           #print(len(sa))
           #print(len(trY))
           for ini in range(0,len(sa)):
               if(sa[ini]!=arrayout[ini]):
                   perc=perc+1
    
            #item1.fit=(math.fsum(fitness)/(len(sss1)))
           item1.fit=item1.fit+(perc+0.0)/len(sa) 
    @classmethod
    def fitpop(self,item1):
        for i in range(0,item1.size()):
            genteics.fit3(item1.item[i]) 

    @classmethod
    def statics(self,item1):
        #genteics.fitpop(item1)
        self.mean=0
        self.max=-1000000000
        self.min=1000000000
        self.best=item1.item[0]
        self.var=item1.item[0]
        self.varval=0
        self.sizes=0
        
        for i in range(0,item1.size()):
            if(item1.item[i].fit<=self.min):
                self.best=item1.item[i]
                self.min=item1.item[i].fit
            if(item1.item[i].fit>self.max):
                self.max=item1.item[i].fit
            self.mean=self.mean+item1.item[i].fit
            self.sizes=self.sizes+item1.item[i].size()
        
            
        self.sizes=(self.sizes+0.0)/(item1.size()*(opsize+0.0))
        self.mean=self.mean/item1.size()
        self.varval=math.fabs(self.mean-self.var.fit)
        for i in range(0,item1.size()):
            tempvar=math.fabs(self.mean-item1.item[i].fit)
            if(self.varval<tempvar):
                self.varval=tempvar
                self.var=item1.item[i]
            
        ss11,ss12=decoder.calc(self.best)
        print(ss12[0])                                                                                      
        #print(ss11[0])
        print("Mean:"+str(self.mean)+"MAX:"+str(self.max)+"MIN:"+str(self.min)+"average size:"+str(self.sizes))
        return self.mean,self.max,self.min,ss11,self.best,self.var
        
    @classmethod
    def mut(self,item1):
        hcross2=item1.copy()
       
        for k in range(0,1+int(mutation*item1.size())):
            i=random.randint(0,item1.size()-1)
            hcross2.item[i]=1-hcross2.item[i]
            if(decoder.validate(hcross2)==0):
                hcross2.item[i]=1-hcross2.item[i]   
       
        return hcross2
    @classmethod
    def sort(self,inds):
        for j in range(0,len(inds)-1):
            flgsort=0
            for i in range(0,len(inds)-1):
                if(inds[i].fit>inds[i+1].fit):
                    self.newtemp=inds[i+1]
                    inds[i+1]=inds[i]
                    inds[i]=self.newtemp
                    flgsort=1
            if(flgsort==0):
                break
                
    @classmethod
    def tour(self):
       pop=h1
       self.hselect4=[]
       self.hselect4.index

       
       #genteics.fitpop(pop)        
       l=random.sample(range(0,pop.size()),4)
       for i in range(0,4):
       
           
           self.hselect4.append(pop.item[l[i]])

       genteics.sort(self.hselect4)
       self.isel0,self.isel1=genteics.crossover(self.hselect4[0],self.hselect4[1])
       self.isel0=genteics.mut(self.isel0)
       self.isel1=genteics.mut(self.isel1)
       genteics.fit3(self.isel0)
       genteics.fit3(self.isel1)
       pop.item[pop.item.index(self.hselect4[2])]=self.isel0
       pop.item[pop.item.index(self.hselect4[3])]=self.isel1
    @classmethod
    def tour2(self,predicts):
       pop=predicts
       self.hselect4=[]
       self.hselect4.index

       
       #genteics.fitpop(pop)        
       l=random.sample(range(0,len(pop)),4)
       for i in range(0,4):
       
           
           self.hselect4.append(pop[l[i]])

       genteics.sort(self.hselect4)
       self.isel0=predictor(len(self.hselect4[0].sub),200)
       self.isel1=predictor(len(self.hselect4[0].sub),200)
       self.cpoint=random.randint(0,len(self.hselect4[0].sub)-1)
       for inx16 in range(0,self.cpoint):
           self.isel0.sub[inx16]=self.hselect4[0].sub[inx16]
           self.isel1.sub[inx16]=self.hselect4[1].sub[inx16]
       for inx16 in range(self.cpoint,len(self.hselect4[1].sub)):
           self.isel0.sub[inx16]=self.hselect4[0].sub[inx16]
           self.isel1.sub[inx16]=self.hselect4[1].sub[inx16]
       self.isel0.sub[random.randint(0,len(self.isel0.sub)-1)]=random.randint(0,199)
       self.isel1.sub[random.randint(0,len(self.isel0.sub)-1)]=random.randint(0,199)
       #genteics.fit3(self.isel0)
       #genteics.fit3(self.isel1)
       pop[pop.index(self.hselect4[2])]=self.isel0
       pop[pop.index(self.hselect4[3])]=self.isel1

        
        
        
        
class decoder:
   @classmethod
   def validate(self,ind):
       self.dec=decoder.decod(ind)
       if(self.dec[0]==[]):
           return 0
       if(len(self.dec)>maxind):
           return 0
       for ii in range(0,len(self.dec)):
           #print(ii)
           #print(self.dec[ii])
           self.target=decoder.binary(self.dec[ii][1:int(1+math.ceil(math.log(class_num,2)))])
           self.operan=decoder.binary(self.dec[ii][int(1+math.ceil(math.log(class_num,2))+3):int(1+math.ceil(math.log(class_num,2))+3+math.ceil(math.log(input_num,2)))])
           self.operat=decoder.binary(self.dec[ii][int(1+math.ceil(math.log(class_num,2))):int(1+math.ceil(math.log(class_num,2))+3)])
           self.mod=self.dec[ii][0]
       #    print(self.dec[ii][int(1+math.ceil(math.log(class_num,2))+2):int(1+math.ceil(math.log(class_num,2))+2+math.ceil(math.log(input_num,2)))])
        #   print(self.operan)
           if(self.mod==1 and self.operan>=class_num):
               return 0
           if(self.mod==0 and self.operan>=input_num):
               return 0
           if(self.target>=class_num):
               return 0
           
            
       return 1
   @classmethod
   def validate2(self,ind):
       self.dec=[ind]

       if(len(self.dec)>maxind):
           return 0
       for ii in range(0,len(self.dec)):
           self.target=decoder.binary(self.dec[ii][1:int(1+math.ceil(math.log(class_num,2)))])
           self.operan=decoder.binary(self.dec[ii][int(1+math.ceil(math.log(class_num,2))+3):int(1+math.ceil(math.log(class_num,2))+3+math.ceil(math.log(input_num,2)))])
           self.operat=decoder.binary(self.dec[ii][int(1+math.ceil(math.log(class_num,2))):int(1+math.ceil(math.log(class_num,2))+3)])
           self.mod=self.dec[ii][0]
           if(self.target>=class_num):
               return 0
           if(self.mod==1 and self.operan>=class_num):
               return 0
           if(self.mod==0 and self.operan>=input_num):
               return 0
           
            
       return 1
   @classmethod
   def decod(self,ind):
       self.hdecod=[]
       r=c=0
       self.hdecod.append([])
       for i in range (0,ind.size()):
          if(r>=opsize):
               r=0
               self.hdecod.append([])
               c=c+1
          self.hdecod[c].append(ind.item[i])
          r=r+1
         
       return self.hdecod
   @classmethod
   def binary(self,inp):
       self.res=0
       for i in range(0,len(inp)):
           self.res=self.res*2
           self.res=self.res+inp[i]
       return self.res
   @classmethod
   def calc(self,ind):
       self.meenlist=[]
       self.reglist=[]
       
       
 
       for tt in arrayin:
           
           self.inputs=[]
           self.reg=[]
           for iz in range(0,class_num):
               self.reg.append(0)
           self.inputs.extend(tt)
           self.dec=decoder.decod(ind)
           self.meen=[]
           for ii in range(0,len(self.dec)):
               self.target=decoder.binary(self.dec[ii][1:int(1+math.ceil(math.log(class_num,2)))])
               self.operan=decoder.binary(self.dec[ii][int(1+math.ceil(math.log(class_num,2))+3):int(1+math.ceil(math.log(class_num,2))+3+math.ceil(math.log(input_num,2)))])
               self.operat=decoder.binary(self.dec[ii][int(1+math.ceil(math.log(class_num,2))):int(1+math.ceil(math.log(class_num,2))+3)])
               tempstr="R"+str(self.target)+"="+"R"+str(self.target)
               try:

                   if(self.operat==0):                   
                       tempstr=tempstr+"+"
                       if(self.dec[ii][0]==0):
                           self.reg[self.target]=float(self.reg[self.target])+self.inputs[self.operan]
                           tempstr=tempstr+"IP"+str(self.operan)
                       if(self.dec[ii][0]==1):
                           self.reg[self.target]=float(self.reg[self.target])+self.reg[self.operan]
                           tempstr=tempstr+"R"+str(self.operan) 
                   if(self.operat==1):                   
                       tempstr=tempstr+"-"
                       if(self.dec[ii][0]==0):
                           self.reg[self.target]=float(self.reg[self.target])-self.inputs[self.operan]
                           tempstr=tempstr+"IP"+str(self.operan)
                       if(self.dec[ii][0]==1):
                           self.reg[self.target]=float(self.reg[self.target])-self.reg[self.operan]
                           tempstr=tempstr+"R"+str(self.operan)
                   if(self.operat==2):                   
                       tempstr=tempstr+"/"
                       if(self.dec[ii][0]==0):
                           if(self.inputs[self.operan]!=0):
                               self.reg[self.target]=float(self.reg[self.target])/self.inputs[self.operan]
                               tempstr=tempstr+"IP"+str(self.operan)
                           else:
                               self.reg[self.target]=1.0
                               tempstr=tempstr+"IP"+str(self.operan)+"exception=1"
                       if(self.dec[ii][0]==1):
                           if(self.reg[self.operan]!=0):
                               self.reg[self.target]=float(self.reg[self.target])/self.reg[self.operan]
                               tempstr=tempstr+"R"+str(self.operan)
                           else:
                               self.reg[self.target]=1.0
                               tempstr=tempstr+"R"+str(self.operan)+"exception=1"
                   if(self.operat==3):                   
                       tempstr=tempstr+"*"
                       if(self.dec[ii][0]==0):
                           self.reg[self.target]=float(self.reg[self.target])*self.inputs[self.operan]
                           tempstr=tempstr+"IP"+str(self.operan)
                       if(self.dec[ii][0]==1):
                           self.reg[self.target]=float(self.reg[self.target])*self.reg[self.operan]
                           tempstr=tempstr+"R"+str(self.operan)
                   if(self.operat==4):                   
                       tempstr=tempstr+"+exp"
                       if(self.dec[ii][0]==0):
                           if(self.inputs[self.operan]<15):
                               self.reg[self.target]=float(self.reg[self.target])+math.exp(self.inputs[self.operan])
                               tempstr=tempstr+"IP"+str(self.operan)
                           else:
                               self.reg[self.target]=1.0
                               tempstr=tempstr+"IP"+str(self.operan)+"exception=1"
                       if(self.dec[ii][0]==1):
                           if(self.reg[self.operan]<15):
                               self.reg[self.target]=float(self.reg[self.target])+math.exp(self.reg[self.operan])
                               tempstr=tempstr+"R"+str(self.operan)
                           else:
                               self.reg[self.target]=1.0
                               tempstr=tempstr+"R"+str(self.operan)+"exception=1"
                   if(self.operat==5):                   
                       tempstr=tempstr+"+log"
                       if(self.dec[ii][0]==0):
                           if(self.inputs[self.operan]>0):
                               self.reg[self.target]=float(self.reg[self.target])+math.log(self.inputs[self.operan])
                               tempstr=tempstr+"IP"+str(self.operan)
                           else:
                               self.reg[self.target]=1.0
                               tempstr=tempstr+"IP"+str(self.operan)+"exception=1"
                       if(self.dec[ii][0]==1):
                           if(self.reg[self.operan]>0):
                               
                               self.reg[self.target]=float(self.reg[self.target])+math.log(self.reg[self.operan])
                               tempstr=tempstr+"R"+str(self.operan)
                           else:
                               self.reg[self.target]=1.0
                               tempstr=tempstr+"R"+str(self.operan)+"exception=1"
                   if(self.operat==6):
                       tempstr=tempstr+"+sin"
                       if(self.dec[ii][0]==0):
                           self.reg[self.target]=float(self.reg[self.target])+math.sin(math.degrees(self.inputs[self.operan]))
                           tempstr=tempstr+"IP"+str(self.operan)
                       if(self.dec[ii][0]==1):
                           self.reg[self.target]=float(self.reg[self.target])+math.sin(math.degrees(self.reg[self.operan]))
                           tempstr=tempstr+"R"+str(self.operan)
                   if(self.operat==7):                   
                       tempstr=tempstr+"+cos"
                       if(self.dec[ii][0]==0):
                           self.reg[self.target]=float(self.reg[self.target])+math.cos(math.degrees(self.inputs[self.operan]))
                           tempstr=tempstr+"IP"+str(self.operan)
                       if(self.dec[ii][0]==1):
                           self.reg[self.target]=float(self.reg[self.target])+math.cos(math.degrees(self.reg[self.operan]))
                           tempstr=tempstr+"R"+str(self.operan)
               except ValueError:
                   tempstr=tempstr+"exception=1"
                   print(self.reg[self.target])
                   print(self.reg[self.operan])
                   self.reg[self.target]=1
                   self.reg[self.operan]=1
               
               self.meen.append(tempstr)
           self.meenlist.append(self.meen)
           self.reglist.append(self.reg)
       return self.reglist,self.meenlist 
   @classmethod
   def calc3(self,ind,inside):
       self.meenlist=[]
       self.reglist=[]
       self.arraytin=[]
       for inx15 in range(0,len(inside.sub)):
           
           self.arraytin.append(arraytestin[inside.sub[inx15]])
 
       for tt in self.arraytin:
           
           self.inputs=[]
           self.reg=[]
           for iz in range(0,class_num):
               self.reg.append(0)
           self.inputs.extend(tt)
           self.dec=decoder.decod(ind)
           self.meen=[]
           for ii in range(0,len(self.dec)):
               self.target=decoder.binary(self.dec[ii][1:int(1+math.ceil(math.log(class_num,2)))])
               self.operan=decoder.binary(self.dec[ii][int(1+math.ceil(math.log(class_num,2))+3):int(1+math.ceil(math.log(class_num,2))+3+math.ceil(math.log(input_num,2)))])
               self.operat=decoder.binary(self.dec[ii][int(1+math.ceil(math.log(class_num,2))):int(1+math.ceil(math.log(class_num,2))+3)])
               tempstr="R"+str(self.target)+"="+"R"+str(self.target)     
               try:
                   if(self.operat==0):                   
                       tempstr=tempstr+"+"
                       if(self.dec[ii][0]==0):
                           self.reg[self.target]=float(self.reg[self.target])+self.inputs[self.operan]
                           tempstr=tempstr+"IP"+str(self.operan)
                       if(self.dec[ii][0]==1):
                           self.reg[self.target]=float(self.reg[self.target])+self.reg[self.operan]
                           tempstr=tempstr+"R"+str(self.operan) 
                   if(self.operat==1):                   
                       tempstr=tempstr+"-"
                       if(self.dec[ii][0]==0):
                           self.reg[self.target]=float(self.reg[self.target])-self.inputs[self.operan]
                           tempstr=tempstr+"IP"+str(self.operan)
                       if(self.dec[ii][0]==1):
                           self.reg[self.target]=float(self.reg[self.target])-self.reg[self.operan]
                           tempstr=tempstr+"R"+str(self.operan)
                   if(self.operat==2):                   
                       tempstr=tempstr+"/"
                       if(self.dec[ii][0]==0):
                           if(self.inputs[self.operan]!=0):
                               self.reg[self.target]=float(self.reg[self.target])/self.inputs[self.operan]
                               tempstr=tempstr+"IP"+str(self.operan)
                           else:
                               self.reg[self.target]=1.0
                               tempstr=tempstr+"IP"+str(self.operan)+"exception=1"
                       if(self.dec[ii][0]==1):
                           if(self.reg[self.operan]!=0):
                               self.reg[self.target]=float(self.reg[self.target])/self.reg[self.operan]
                               tempstr=tempstr+"R"+str(self.operan)
                           else:
                               self.reg[self.target]=1.0
                               tempstr=tempstr+"R"+str(self.operan)+"exception=1"
                   if(self.operat==3):                   
                       tempstr=tempstr+"*"
                       if(self.dec[ii][0]==0):
                           self.reg[self.target]=float(self.reg[self.target])*self.inputs[self.operan]
                           tempstr=tempstr+"IP"+str(self.operan)
                       if(self.dec[ii][0]==1):
                           self.reg[self.target]=float(self.reg[self.target])*self.reg[self.operan]
                           tempstr=tempstr+"R"+str(self.operan)
                   if(self.operat==4):                   
                       tempstr=tempstr+"exp"
                       if(self.dec[ii][0]==0):
                           if(self.inputs[self.operan]<15):
                               self.reg[self.target]=float(self.reg[self.target])+math.exp(self.inputs[self.operan])
                               tempstr=tempstr+"IP"+str(self.operan)
                           else:
                               self.reg[self.target]=1.0
                               tempstr=tempstr+"IP"+str(self.operan)+"exception=1"
                       if(self.dec[ii][0]==1):
                           if(self.reg[self.operan]<15):
                               self.reg[self.target]=float(self.reg[self.target])+math.exp(self.reg[self.operan])
                               tempstr=tempstr+"R"+str(self.operan)
                           else:
                               self.reg[self.target]=1.0
                               tempstr=tempstr+"R"+str(self.operan)+"exception=1"
                   if(self.operat==5):                   
                       tempstr=tempstr+"log"
                       if(self.dec[ii][0]==0):
                           if(self.inputs[self.operan]>0):
                               self.reg[self.target]=float(self.reg[self.target])+math.log(self.inputs[self.operan])
                               tempstr=tempstr+"IP"+str(self.operan)
                           else:
                               self.reg[self.target]=1.0
                               tempstr=tempstr+"IP"+str(self.operan)+"exception=1"
                       if(self.dec[ii][0]==1):
                           if(self.reg[self.operan]>0):
                               
                               self.reg[self.target]=float(self.reg[self.target])+math.log(self.reg[self.operan])
                               tempstr=tempstr+"R"+str(self.operan)
                           else:
                               self.reg[self.target]=1.0
                               tempstr=tempstr+"R"+str(self.operan)+"exception=1"
                   if(self.operat==6):
                       tempstr=tempstr+"sin"
                       if(self.dec[ii][0]==0):
                           self.reg[self.target]=float(self.reg[self.target])+math.sin(math.degrees(self.inputs[self.operan]))
                           tempstr=tempstr+"IP"+str(self.operan)
                       if(self.dec[ii][0]==1):
                           self.reg[self.target]=float(self.reg[self.target])+math.sin(math.degrees(self.reg[self.operan]))
                           tempstr=tempstr+"R"+str(self.operan)
                   if(self.operat==7):                   
                       tempstr=tempstr+"cos"
                       if(self.dec[ii][0]==0):
                           self.reg[self.target]=float(self.reg[self.target])+math.cos(math.degrees(self.inputs[self.operan]))
                           tempstr=tempstr+"IP"+str(self.operan)
                       if(self.dec[ii][0]==1):
                           self.reg[self.target]=float(self.reg[self.target])+math.cos(math.degrees(self.reg[self.operan]))
                           tempstr=tempstr+"R"+str(self.operan)
               except ValueError:
                   tempstr=tempstr+"exception=1"
                   print(self.reg[self.target])
                   print(self.reg[self.operan])
                   self.reg[self.target]=1
                   self.reg[self.operan]=1
               
               self.meen.append(tempstr)
           self.meenlist.append(self.meen)
           self.reglist.append(self.reg)
       return self.reglist,self.meenlist
   @classmethod
   def calc4(self,ind,inside):
       self.meenlist=[]
       self.reglist=[]
       self.arraytin=[]
       for inx15 in range(0,len(inside)):
           
           self.arraytin.append(inside[inx15])
 
       for tt in self.arraytin:
           
           self.inputs=[]
           self.reg=[]
           for iz in range(0,class_num):
               self.reg.append(0)
           self.inputs.extend(tt)
           self.dec=decoder.decod(ind)
           self.meen=[]
           for ii in range(0,len(self.dec)):
               self.target=decoder.binary(self.dec[ii][1:int(1+math.ceil(math.log(class_num,2)))])
               self.operan=decoder.binary(self.dec[ii][int(1+math.ceil(math.log(class_num,2))+3):int(1+math.ceil(math.log(class_num,2))+3+math.ceil(math.log(input_num,2)))])
               self.operat=decoder.binary(self.dec[ii][int(1+math.ceil(math.log(class_num,2))):int(1+math.ceil(math.log(class_num,2))+3)])
               tempstr="R"+str(self.target)+"="+"R"+str(self.target)     
               try:
                   if(self.operat==0):                   
                       tempstr=tempstr+"+"
                       if(self.dec[ii][0]==0):
                           self.reg[self.target]=float(self.reg[self.target])+self.inputs[self.operan]
                           tempstr=tempstr+"IP"+str(self.operan)
                       if(self.dec[ii][0]==1):
                           self.reg[self.target]=float(self.reg[self.target])+self.reg[self.operan]
                           tempstr=tempstr+"R"+str(self.operan) 
                   if(self.operat==1):                   
                       tempstr=tempstr+"-"
                       if(self.dec[ii][0]==0):
                           self.reg[self.target]=float(self.reg[self.target])-self.inputs[self.operan]
                           tempstr=tempstr+"IP"+str(self.operan)
                       if(self.dec[ii][0]==1):
                           self.reg[self.target]=float(self.reg[self.target])-self.reg[self.operan]
                           tempstr=tempstr+"R"+str(self.operan)
                   if(self.operat==2):                   
                       tempstr=tempstr+"/"
                       if(self.dec[ii][0]==0):
                           if(self.inputs[self.operan]!=0):
                               self.reg[self.target]=float(self.reg[self.target])/self.inputs[self.operan]
                               tempstr=tempstr+"IP"+str(self.operan)
                           else:
                               self.reg[self.target]=1.0
                               tempstr=tempstr+"IP"+str(self.operan)+"exception=1"
                       if(self.dec[ii][0]==1):
                           if(self.reg[self.operan]!=0):
                               self.reg[self.target]=float(self.reg[self.target])/self.reg[self.operan]
                               tempstr=tempstr+"R"+str(self.operan)
                           else:
                               self.reg[self.target]=1.0
                               tempstr=tempstr+"R"+str(self.operan)+"exception=1"
                   if(self.operat==3):                   
                       tempstr=tempstr+"*"
                       if(self.dec[ii][0]==0):
                           self.reg[self.target]=float(self.reg[self.target])*self.inputs[self.operan]
                           tempstr=tempstr+"IP"+str(self.operan)
                       if(self.dec[ii][0]==1):
                           self.reg[self.target]=float(self.reg[self.target])*self.reg[self.operan]
                           tempstr=tempstr+"R"+str(self.operan)
                   if(self.operat==4):                   
                       tempstr=tempstr+"exp"
                       if(self.dec[ii][0]==0):
                           if(self.inputs[self.operan]<15):
                               self.reg[self.target]=float(self.reg[self.target])+math.exp(self.inputs[self.operan])
                               tempstr=tempstr+"IP"+str(self.operan)
                           else:
                               self.reg[self.target]=1.0
                               tempstr=tempstr+"IP"+str(self.operan)+"exception=1"
                       if(self.dec[ii][0]==1):
                           if(self.reg[self.operan]<15):
                               self.reg[self.target]=float(self.reg[self.target])+math.exp(self.reg[self.operan])
                               tempstr=tempstr+"R"+str(self.operan)
                           else:
                               self.reg[self.target]=1.0
                               tempstr=tempstr+"R"+str(self.operan)+"exception=1"
                   if(self.operat==5):                   
                       tempstr=tempstr+"log"
                       if(self.dec[ii][0]==0):
                           if(self.inputs[self.operan]>0):
                               self.reg[self.target]=float(self.reg[self.target])+math.log(self.inputs[self.operan])
                               tempstr=tempstr+"IP"+str(self.operan)
                           else:
                               self.reg[self.target]=1.0
                               tempstr=tempstr+"IP"+str(self.operan)+"exception=1"
                       if(self.dec[ii][0]==1):
                           if(self.reg[self.operan]>0):
                               
                               self.reg[self.target]=float(self.reg[self.target])+math.log(self.reg[self.operan])
                               tempstr=tempstr+"R"+str(self.operan)
                           else:
                               self.reg[self.target]=1.0
                               tempstr=tempstr+"R"+str(self.operan)+"exception=1"
                   if(self.operat==6):
                       tempstr=tempstr+"sin"
                       if(self.dec[ii][0]==0):
                           self.reg[self.target]=float(self.reg[self.target])+math.sin(math.degrees(self.inputs[self.operan]))
                           tempstr=tempstr+"IP"+str(self.operan)
                       if(self.dec[ii][0]==1):
                           self.reg[self.target]=float(self.reg[self.target])+math.sin(math.degrees(self.reg[self.operan]))
                           tempstr=tempstr+"R"+str(self.operan)
                   if(self.operat==7):                   
                       tempstr=tempstr+"cos"
                       if(self.dec[ii][0]==0):
                           self.reg[self.target]=float(self.reg[self.target])+math.cos(math.degrees(self.inputs[self.operan]))
                           tempstr=tempstr+"IP"+str(self.operan)
                       if(self.dec[ii][0]==1):
                           self.reg[self.target]=float(self.reg[self.target])+math.cos(math.degrees(self.reg[self.operan]))
                           tempstr=tempstr+"R"+str(self.operan)
               except ValueError:
                   tempstr=tempstr+"exception=1"
                   print(self.reg[self.target])
                   print(self.reg[self.operan])
                   self.reg[self.target]=1
                   self.reg[self.operan]=1
               
               self.meen.append(tempstr)
           self.meenlist.append(self.meen)
           self.reglist.append(self.reg)
       return self.reglist,self.meenlist
   @classmethod
   def calc2(self,ind):
       self.meenlist=[]
       self.reglist=[]
 
       for tt in arraytestin:
           
           self.inputs=[]
           self.reg=[]
           for iz in range(0,class_num):
               self.reg.append(0)
           self.inputs.extend(tt)
           self.dec=decoder.decod(ind)
           self.meen=[]
           for ii in range(0,len(self.dec)):
               self.target=decoder.binary(self.dec[ii][1:int(1+math.ceil(math.log(class_num,2)))])
               self.operan=decoder.binary(self.dec[ii][int(1+math.ceil(math.log(class_num,2))+3):int(1+math.ceil(math.log(class_num,2))+3+math.ceil(math.log(input_num,2)))])
               self.operat=decoder.binary(self.dec[ii][int(1+math.ceil(math.log(class_num,2))):int(1+math.ceil(math.log(class_num,2))+3)])
               tempstr="R"+str(self.target)+"="+"R"+str(self.target)     
               try:
                   if(self.operat==0):                   
                       tempstr=tempstr+"+"
                       if(self.dec[ii][0]==0):
                           self.reg[self.target]=float(self.reg[self.target])+self.inputs[self.operan]
                           tempstr=tempstr+"IP"+str(self.operan)
                       if(self.dec[ii][0]==1):
                           self.reg[self.target]=float(self.reg[self.target])+self.reg[self.operan]
                           tempstr=tempstr+"R"+str(self.operan) 
                   if(self.operat==1):                   
                       tempstr=tempstr+"-"
                       if(self.dec[ii][0]==0):
                           self.reg[self.target]=float(self.reg[self.target])-self.inputs[self.operan]
                           tempstr=tempstr+"IP"+str(self.operan)
                       if(self.dec[ii][0]==1):
                           self.reg[self.target]=float(self.reg[self.target])-self.reg[self.operan]
                           tempstr=tempstr+"R"+str(self.operan)
                   if(self.operat==2):                   
                       tempstr=tempstr+"/"
                       if(self.dec[ii][0]==0):
                           if(self.inputs[self.operan]!=0):
                               self.reg[self.target]=float(self.reg[self.target])/self.inputs[self.operan]
                               tempstr=tempstr+"IP"+str(self.operan)
                           else:
                               self.reg[self.target]=1.0
                               tempstr=tempstr+"IP"+str(self.operan)+"exception=1"
                       if(self.dec[ii][0]==1):
                           if(self.reg[self.operan]!=0):
                               self.reg[self.target]=float(self.reg[self.target])/self.reg[self.operan]
                               tempstr=tempstr+"R"+str(self.operan)
                           else:
                               self.reg[self.target]=1.0
                               tempstr=tempstr+"R"+str(self.operan)+"exception=1"
                   if(self.operat==3):                   
                       tempstr=tempstr+"*"
                       if(self.dec[ii][0]==0):
                           self.reg[self.target]=float(self.reg[self.target])*self.inputs[self.operan]
                           tempstr=tempstr+"IP"+str(self.operan)
                       if(self.dec[ii][0]==1):
                           self.reg[self.target]=float(self.reg[self.target])*self.reg[self.operan]
                           tempstr=tempstr+"R"+str(self.operan)
                   if(self.operat==4):                   
                       tempstr=tempstr+"exp"
                       if(self.dec[ii][0]==0):
                           if(self.inputs[self.operan]<15):
                               self.reg[self.target]=float(self.reg[self.target])+math.exp(self.inputs[self.operan])
                               tempstr=tempstr+"IP"+str(self.operan)
                           else:
                               self.reg[self.target]=1.0
                               tempstr=tempstr+"IP"+str(self.operan)+"exception=1"
                       if(self.dec[ii][0]==1):
                           if(self.reg[self.operan]<15):
                               self.reg[self.target]=float(self.reg[self.target])+math.exp(self.reg[self.operan])
                               tempstr=tempstr+"R"+str(self.operan)
                           else:
                               self.reg[self.target]=1.0
                               tempstr=tempstr+"R"+str(self.operan)+"exception=1"
                   if(self.operat==5):                   
                       tempstr=tempstr+"log"
                       if(self.dec[ii][0]==0):
                           if(self.inputs[self.operan]>0):
                               self.reg[self.target]=float(self.reg[self.target])+math.log(self.inputs[self.operan])
                               tempstr=tempstr+"IP"+str(self.operan)
                           else:
                               self.reg[self.target]=1.0
                               tempstr=tempstr+"IP"+str(self.operan)+"exception=1"
                       if(self.dec[ii][0]==1):
                           if(self.reg[self.operan]>0):
                               
                               self.reg[self.target]=float(self.reg[self.target])+math.log(self.reg[self.operan])
                               tempstr=tempstr+"R"+str(self.operan)
                           else:
                               self.reg[self.target]=1.0
                               tempstr=tempstr+"R"+str(self.operan)+"exception=1"
                   if(self.operat==6):
                       tempstr=tempstr+"sin"
                       if(self.dec[ii][0]==0):
                           self.reg[self.target]=float(self.reg[self.target])+math.sin(math.degrees(self.inputs[self.operan]))
                           tempstr=tempstr+"IP"+str(self.operan)
                       if(self.dec[ii][0]==1):
                           self.reg[self.target]=float(self.reg[self.target])+math.sin(math.degrees(self.reg[self.operan]))
                           tempstr=tempstr+"R"+str(self.operan)
                   if(self.operat==7):                   
                       tempstr=tempstr+"cos"
                       if(self.dec[ii][0]==0):
                           self.reg[self.target]=float(self.reg[self.target])+math.cos(math.degrees(self.inputs[self.operan]))
                           tempstr=tempstr+"IP"+str(self.operan)
                       if(self.dec[ii][0]==1):
                           self.reg[self.target]=float(self.reg[self.target])+math.cos(math.degrees(self.reg[self.operan]))
                           tempstr=tempstr+"R"+str(self.operan)
               except ValueError:
                   tempstr=tempstr+"exception=1"
                   print(self.reg[self.target])
                   print(self.reg[self.operan])
                   self.reg[self.target]=1
                   self.reg[self.operan]=1
               
               self.meen.append(tempstr)
           self.meenlist.append(self.meen)
           self.reglist.append(self.reg)
       return self.reglist,self.meenlist 
       
def originalfit(x):
    #print(x)    
    return math.exp(math.fabs(x))*math.sin(math.degrees(x))
def predictor_fitness(pop_predicts,trainers):
    for inx13 in range(len(pop_predicts)):
        sum=0
        for inx14 in range(0,len(trainers)):
            regs,meens=decoder.calc3(trainers[inx14][0],pop_predicts[inx13])
            try:
                #fitness=((math.pow(arrayout[x1][0]-sss1[x1][0],2)) for x1 in range(0,len(sss1)))
                fitness=0.0
                for inx10 in range(0,len(regs)):
                    fitness=(((fitness*inx10)/(1.0+float(inx10)))+(math.fabs(arraytestout[pop_predicts[inx13].sub[inx10]][0]-regs[inx10][0])/(inx10+1.0)))
            except OverflowError:
                print("OOPS")
                

    
            sum+=math.fabs(fitness-trainers[inx14][1])
        pop_predicts[inx13].fit=sum
    return pop_predicts
        
            
            
    
class predictor:
    
    def __init__(self,ssize,rsize):
        self.sub=1
        self.fit=-1
        
        self.sub=[]
        for inx12 in range(0,ssize):
            self.sub.append(random.randint(0,rsize-1))
            
    def __str__( self ):
        return str(self.item)
    def copy( self ):
        hind=predictor(len(self.sub),10)
        #hind.fit=self.fit
        for x in range(0, len(self.sub)):
            hind.sub[x]=self.sub[x]
        
        return hind
    
predictorsamples=8

def ML(inp):
    global arrayin,arrayout,h1,mins,arraytestin,arraytestout
    arrayin=[]
    arrayout=[]
    arraytestin=[]
    arraytestout=[]
    testpoint=1.0
    predictpoint=1.0
    h1=population(128)
    
    generations=2373000
    # equal to 10^7 point evaluation
    trainers=[]
    for ij in range(0,len(inp)):
       temp=[0.0,1.0,2.0,3.0]
       temp[0]=inp[ij]
       arraytestin.append(temp)
       
       arraytestout.append([originalfit(inp[ij])])
    preds=[]
    for inx13 in range(0,5):
        preds.append(predictor(predictorsamples,len(arraytestin)))
    arrayin=[]
    arrayout=[]
    
    for inx11 in range(0,predictorsamples):
   
       arrayin.append(arraytestin[preds[0].sub[inx11]])
       arrayout.append(arraytestout[preds[0].sub[inx11]])
    genteics.fitpop(h1)
    mins=[]
    temin=0
    cycle=10
    for i in range(0,generations):
        
        
        
        
        
        genteics.tour()
        if(i/predictpoint==int(i/predictpoint)):
            cycle-=1
            predictpoint+=400
            preds=predictor_fitness(preds,trainers)
            genteics.tour2(preds)
            arrayin=[]
            arrayout=[]
    
            for inx11 in range(0,predictorsamples):
   
               arrayin.append(arraytestin[preds[0].sub[inx11]])
               arrayout.append(arraytestout[preds[0].sub[inx11]])
            
            
        if(i/testpoint==int(i/testpoint)):
            mean1,max1,min1,ss12,bes,var=genteics.statics(h1)
            testpoint+=1000.0
            if(cycle<0):
                cycle=10
                test1=var.copy()
                genteics.fit4(test1)
                trainers.append([test1,test1.fit])
                if(len(trainers)>predictorsamples):
                    trainers.remove(trainers[0])
        
    
            test=bes.copy()
           
            genteics.fit5(test)
            temin=test.fit
            
            mins.append(-temin)
            print("generation "+str(i)+":"+str(temin))
           ins
def MLresult(value,bes):
    global arraytestin    
    arraytestin=[]
    for ij in range(0,len(value)):
       temp=[0.0]
       temp[0]=value[ij]
       arraytestin.append(temp)
       
    zz1,zz2=decoder.calc2(bes)
    outpu=[]
    for indexou in zz1:
        outpu.append(indexou[0])
    return outpu

kl50=[]

traials=4
temos,genss,minha=ML(np.arange(-3,3,0.03))
printarray=[]
for inx18 in minha:
    printarray.append(inx18)
for inx7 in range(0,traials-1):
    temos,genss,minha=ML(np.arange(-3,3,0.03))
    for inx18 in range(0,len(minha)):
        printarray[inx18]+=minha[inx18]
for inx18 in range(0,len(printarray)):
        printarray[inx18]/=float(traials)



xs=np.arange(0,len(printarray)*16850,16850)

plt.plot(xs,printarray,'-r')
    
f = open('/home/arash/GApro/ficoevolvesample.txt', 'w')
for inx2 in range(0,len(printarray)):
    f.write(str(printarray[inx2])+'\n')  
f.close()
###############################################GA PART comes Here it can use MLresult to use the developed model





    