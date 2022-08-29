from asyncio.windows_events import NULL
from distutils.command.config import config
import nltk as tk

comandos=["M","R","C","B","c","b","P","J","G"]                    #definicion de grupos
instrucciones=["walk","jump","jumpTo","veer","look","drop","grab","get","free","pop","walk", "PROC", "CORP"]     
condiciones=["isfacing","isValid","canWalk","not"]
direcciones1=["left","right","around"]
direcciones2=["left","right","front","back"]
card=["north","south","east","west"]
variables={"x":4}
procedimientos = []

def main():
    filename = 'prueba1.txt'
    file = open(filename).read()
    tokens = tk.word_tokenize(file,"",True)
    parser(tokens)

def errorSintax():
    print("Error de sintaxis")
    exit()

def sintaxChecker(palabra, lista):
    count=0
    for each in lista:
        if palabra == each:
            count+=1

    if count == 1:
        return True
    else:
        return False
    


def explorarparam(num:int, tokens:list,i:int):
    error=False
    q=0
    while not(error) and q<num:
        if tokens[i]!=",":
            if tokens[i].isdigit() or (tokens[i] in variables):
                if ("." or "-") not in tokens[i] and tokens[i].isdigit():
                    i+=1
                    q+=1
                elif isinstance(variables[tokens[i]], int) and (tokens[i] in variables):
                    i+=1
                    q+=1

                else:
                    errorSintax()   
                    error=True
            else:
                errorSintax()    
                error=True  
            if  tokens[i]=="GORP":
                i-=1
                errorSintax()    
                error=True
        elif num==1:
            errorSintax()    
            error=True        
        else:
            i+=1  
            q+=1
    return i,error

def evalins (tokens:list,i:int,error:bool):
    if tokens[i]==";":
        i+=1
        error=True
        errorSintax()
    elif tokens[i]=="(":
         
        i+=1
        v=str(tokens[i])
        param=[]
        p=""
        for e in v:
            if e!="," and e!=" " and e!=")":
                p+=e
            else:
                if p!="":
                    param.append(p) 
                    p=""
        if p!="":
            param.append(p)        

        print (param) 

                        
        if len(param)==2 :  
            if tokens[i-2]=="jumpTo":

                for k in param:
                    if not(k.isdigit()) and not((k in variables)):
                        errorSintax()   
                        error=True
                    elif (("." or "-") in k) and (k not in variables):
                        errorSintax()   
                        error=True
                    elif (k in variables):
                        if not(isinstance(variables[k], int)):
                            errorSintax()   
                            error=True
            elif tokens[i-2]=="walk":

                if not(param[1].isdigit()) and not((param[1] in variables)):
                    errorSintax()   
                    error=True
                elif (("." or "-") in param[1]) and (param[1] not in variables):
                    errorSintax()   
                    error=True
                elif (param[1] in variables):
                    if not(isinstance(variables[param[0]], int)):
                        errorSintax()   
                        error=True 
                if not(param[0] in direcciones2) and not((param[0] in card)):
                    errorSintax()   
                    error=True                                  
            i+=1          
        elif 0==len(param) or len(param)>=2:
            errorSintax()
            error=True

        else: 
            if tokens[i-2]=="jumpTo":
                i,error=explorarparam(2,tokens,i)
            elif  tokens[i-2]=="veer":   
                if not(tokens[i] in direcciones1):
                    errorSintax()   
                    error=True
                else:
                    i+=1
            elif  tokens[i-2]=="look":   
                if not(tokens[i] in card):
                    errorSintax()   
                    error=True
                else:
                    i+=1 
            elif tokens[i-2]=="walk": 
                if tokens[i].isdigit() or (tokens[i] in variables):
                    if ("." or "-") not in tokens[i] and tokens[i].isdigit():
                        i+=1
                    elif isinstance(variables[tokens[i]], int) and (tokens[i] in variables):
                        i+=1
                    else:
                        errorSintax()
                        error=True    
                elif  (tokens[i] in direcciones2) or (tokens[i] in card):
                    i+=1
                    i,error=explorarparam(2,tokens,i)   
                    print(33)     
                else:
                    errorSintax()
                    error=True
            else:
                i,error=explorarparam(1,tokens,i)   
        if tokens[i]==")":
            i+=1
                      
            if tokens[i]==";":
                i+=1
            else:
                errorSintax()
                error=True 
        else:
            errorSintax()
            error=True        
                                         
    else:
        errorSintax()
        error=True             

    return i,error



def parser(tokens):
    if tokens[0] == 'PROG' and tokens[-1] == 'GORP':
        # Elimina la palabra prog y gorp para hacer testeos
        tokens.remove(tokens[0])
        i=0
        error=False

        while tokens[i]!= 'GORP' and not(error):
            print(tokens[i])
            if tokens[i]=="VAR":
                i+=1
                while tokens[i]!= ";" and not(error):
                    if tokens[i][0].isdigit():
                        errorSintax()
                        error=True
                    elif tokens[i]!= ",":
                        variables[tokens[i]]= " "
                    i+=1
                    if tokens[i]== "GORP":
                        errorSintax()
                        i-=1
                        error=True
                i+=1
                variables["x"]=4        
            elif tokens[i] in comandos:
                i+=1
                if tokens[i]==";" and tokens[i-1]!="G" and tokens[i-1]!="J":
                    i+=1
                    print("t")
                else:
                    if tokens[i]=="(" :
                        i+=1
                        v=str(tokens[i])
                        param=[]
                        p=""
                        for e in v:
                            if e!="," and e!=" " and e!=")":
                                p+=e
                            else:
                                if p!="":
                                    param.append(p) 
                                    p=""
                        if p!="":
                            param.append(p)        

                        print (param) 

                        
                        if len(param)==2 and tokens[i-2]=="G":  

                            for k in param:
                                if not(k.isdigit()) and not((k in variables)):
                                    errorSintax()   
                                    error=True
                                elif (("." or "-") in k) and (k not in variables):
                                    errorSintax()   
                                    error=True
                                elif (k in variables):
                                    if not(isinstance(variables[k], int)):
                                        errorSintax()   
                                        error=True      
                            i+=1          
                        elif 0==len(param) or len(param)>=2:
                            errorSintax()
                            error=True

                        else: 
                            if tokens[i-2]=="G":
                                i,error=explorarparam(3,tokens,i)
                                
                            else:
                                i,error=explorarparam(1,tokens,i)

                        if tokens[i]==")":
                            i+=1
                      
                            if tokens[i]==";":
                                i+=1
                            else:
                                errorSintax()
                                error=True 
                        else:
                            errorSintax()
                            error=True        
                                         
                    else:
                        errorSintax()
                        error=True    


            ##PROCESOS Y BLOQUE DE INSTRUCCIONES##
            elif tokens[i] == 'PROC':
                if tokens[i] in instrucciones:
                    ins = []
                    count = 0
                    procedimientos = []
                    while tokens[i] != 'CORP' and not(error):
                        if tokens[i] == 'PROC':
                            i+=1
                            while tokens[i] != '}' and not(error):
                                procedimientos.append(tokens[i])
                                i+=1
                            if procedimientos[1] != '(':
                                errorSintax()
                                error = True

                            #Chequea bracket al inicio del bloque#
                            sintaxBrackets = sintaxChecker('{', procedimientos)
                            if sintaxBrackets != True:
                                errorSintax()

                            for each in procedimientos:
                                if each in instrucciones:
                                    ins.append(each)
                                
                                
                            #Chequea si las instrucciones tienen variable dentro y ambos parentesis#
                            while count < len(ins):
                                pos = procedimientos.index(ins[count])
                                if procedimientos[pos+1] != '(':
                                    errorSintax()
                                if procedimientos[pos+3] != ')':
                                    errorSintax()
                                else:
                                    count+=1
                        
                        else:
                            error = True
            elif tokens[i] in instrucciones:
                i+=1
                print(tokens)
                i,error=evalins(tokens,i,error)
                

           
            else:
                errorSintax()



        #print(tokens)

    ##Si no empieza por PROG y termina en GORP       
    else:
        errorSintax()  





if __name__ == "__main__":
    main()
