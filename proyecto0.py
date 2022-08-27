comandos=["M","R","C","B","c","b","P","J","G"]                    #definicion de grupos
instrucciones=["walk","jump","jumpTo","veer","look","drop","grab","get","free","pop","walk"]     
condiciones=["isfacing","isValid","canWalk","not"]
variables=[]


import nltk as tk


def main():
    filename = 'prueba1.txt'
    file = open(filename).read()
    tokens = tk.word_tokenize(file,"",True)
    parser(tokens)
def varsRobot():
    pass


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
                    if tokens[i]!= ",":
                        variables.append(tokens[i])
                    i+=1
                    if tokens[i]== "GORP":
                        print("error de sintaxis")
                        i-=1
                        error=True
                i+=1        
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
                                    if not(("." or "-") not in k or isinstance(k, int)):
                                        print("error de sintaxis")    
                                        error=True
                            i+=1          
                        elif 0==len(param) or len(param)>=2:
                            print("error de sintaxis")
                            error=True

                        else: 
                            if tokens[i-2]=="G":
                                q=0
                                while not(error) and q<2:
                                    if tokens[i]!=",":
                                        if tokens[i].isdigit() or (tokens[i] in variables):
                                            if ("." or "-") not in tokens[i] or isinstance(tokens[i], int):
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
                            else:
                                if tokens[i].isdigit() or (tokens[i] in variables):
                                    if ("." or "-") not in tokens[i] or isinstance(tokens[i], int):
                                        i+=1

                                    else:
                                        print("error de sintaxis")    
                                        error=True



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
