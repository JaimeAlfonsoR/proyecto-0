comandos=["M","R","C","B","c","b","P","J","G"]                    #definicion de grupos
instrucciones=["walk","jump","jumpTo","veer","look","drop","grab","get","free","pop","walk"]     
condiciones=["isfacing","isValid","canWalk","not"]
variables={"x":4}


from asyncio.windows_events import NULL
from distutils.command.config import config
import nltk as tk


def main():
    filename = 'prueba1.txt'
    file = open(filename).read()
    tokens = tk.word_tokenize(file,"",True)
    parser(tokens)
def varsRobot():
    pass
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
                    print("error de sintaxis")    
                    error=True
            else:
                print("error de sintaxis")    
                error=True  
            if  tokens[i]=="GORP":
                i-=1
                print("error de sintaxis")    
                error=True
        else:
            i+=1  
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
                        print ("error de sintaxis")
                        error=True
                    elif tokens[i]!= ",":
                        variables[tokens[i]]=" "
                    i+=1
                    if tokens[i]== "GORP":
                        print("error de sintaxis")
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
                                    print("error de sintaxis")    
                                    error=True
                                elif (("." or "-") in k) and (k not in variables):
                                    print("error de sintaxis")    
                                    error=True
                                elif (k in variables):
                                    if not(isinstance(variables[k], int)):
                                        print("error de sintaxis")    
                                        error=True      
                            i+=1          
                        elif 0==len(param) or len(param)>=2:
                            print("error de sintaxis")
                            error=True

                        else: 
                            if tokens[i-2]=="G":
                                i,error=explorarparam(2,tokens,i)
                                
                            else:
                                i,error=explorarparam(1,tokens,i)

                        if tokens[i]==")":
                            i+=1
                      
                            if tokens[i]==";":
                                i+=1
                            else:
                                print("error de sintaxis")
                                error=True 
                        else:
                            print("error de sintaxis")
                            error=True        
                                         
                    else:
                        print("error de sintaxis")
                        error=True             
            elif tokens[i] in instrucciones:
                i+=1
                

            
            
        print(tokens)  





if __name__ == "__main__":
    main()
