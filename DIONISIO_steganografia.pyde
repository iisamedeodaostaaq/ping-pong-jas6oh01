i=0                           
p=0                            
lpixel=50                  
grandezza_img=lpixel*5  

def setup():
    global frase,i,p,lpixel
    i=0
    frase=[]
    size(grandezza_img,grandezza_img)      
    frase = input('scrivi una frase')      
    disegna()

def input(message=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(frame, message)

def disegna():
    global i,p,lpixel
    loadPixels()           

    while i < (len(frase)):      
        if (i<len(frase)):       
            r=ord(frase[i])
        else:
            r=255                
        if (i+1<len(frase)):     
            g=ord(frase[i+1])
        else:
            g=255
        if (i+2<len(frase)):
            b=ord(frase[i+2])
        else:
            b=255
        i=i+3
        cont=0
        for x in range(lpixel):             
            for y in range (lpixel):        
                pixels[p+y+(grandezza_img*x)] = color(r, g, b) 
        p=p+lpixel                                          
        if(p%grandezza_img==0):                
            p=p+(grandezza_img*(lpixel-1))    
        print r                                   
        print g
        print b
    updatePixels()                
    save("out.tiff")               
