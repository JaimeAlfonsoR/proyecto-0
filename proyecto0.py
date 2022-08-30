from asyncio.windows_events import NULL
from distutils.command.config import config
from xmlrpc.client import boolean
from inspect import currentframe, getframeinfo
import nltk as tk

comandos=["M","R","C","B","c","b","P","J","G"]                    #definicion de grupos
instrucciones=["walk","jump","jumpTo","veer","look","drop","grab","get","free","pop","walk", "PROC", "CORP"]  
ins2=["walk", "jump", "grab", "pop", "pick", "free","drop"]   
condiciones=["isfacing","isValid","canWalk","not"]
condicionales = ["while", "do", "if", "od", "fi", "else"]
condicions2param = ["isValid", "canWalk"]
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

def errorSintax(frameinfo):
    print("Error de sintaxis detectado en la linea de codigo:", frameinfo.lineno)
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
                    errorSintax(getframeinfo(currentframe()))   
                    error=True
            else:
                errorSintax(getframeinfo(currentframe()))   
                error=True  
            if  tokens[i]=="GORP":
                i-=1
                errorSintax(getframeinfo(currentframe()))   
                error=True
        elif num==1:
            errorSintax(getframeinfo(currentframe()))   
            error=True        
        else:
            i+=1  
            q+=1
    return i,error

def evalins (tokens:list,i:int,error:bool, fin:bool):
    if tokens[i]==";":
        i+=1
        error=True
        errorSintax(getframeinfo(currentframe()))
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
                        errorSintax(getframeinfo(currentframe()))   
                        error=True
                    elif (("." or "-") in k) and (k not in variables):
                        errorSintax(getframeinfo(currentframe()))   
                        error=True
                    elif (k in variables):
                        if not(isinstance(variables[k], int)):
                            errorSintax(getframeinfo(currentframe()))   
                            error=True
            elif tokens[i-2]=="walk":

                if not(param[1].isdigit()) and not((param[1] in variables)):
                    errorSintax(getframeinfo(currentframe()))  
                    error=True
                elif (("." or "-") in param[1]) and (param[1] not in variables):
                    errorSintax(getframeinfo(currentframe()))   
                    error=True
                elif (param[1] in variables):
                    if not(isinstance(variables[param[0]], int)):
                        errorSintax(getframeinfo(currentframe()))   
                        error=True 
                if not(param[0] in direcciones2) and not((param[0] in card)):
                    errorSintax(getframeinfo(currentframe()))   
                    error=True                                  
            i+=1          
        elif 0==len(param) or len(param)>=2:
            errorSintax(getframeinfo(currentframe()))
            error=True

        else: 
            if tokens[i-2]=="jumpTo":
                i,error=explorarparam(2,tokens,i)
            elif  tokens[i-2]=="veer":   
                if not(tokens[i] in direcciones1):
                    errorSintax(getframeinfo(currentframe()))   
                    error=True
                else:
                    i+=1
            elif  tokens[i-2]=="look":   
                if not(tokens[i] in card):
                    errorSintax(getframeinfo(currentframe()))   
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
                        errorSintax(getframeinfo(currentframe()))
                        error=True    
                elif  (tokens[i] in direcciones2) or (tokens[i] in card):
                    i+=1
                    i,error=explorarparam(2,tokens,i)   
                    print(33)     
                else:
                    errorSintax(getframeinfo(currentframe()))
                    error=True
            else:
                i,error=explorarparam(1,tokens,i)   
        if tokens[i]==")":
            i+=1
            if fin:
                      
                if tokens[i]==";":
                    i+=1
                else:
                    errorSintax(getframeinfo(currentframe()))
                    error=True 
        else:
            errorSintax(getframeinfo(currentframe()))
            error=True        
                                         
    else:
        errorSintax(getframeinfo(currentframe()))
        error=True             
                                  
    return i,error

def evalcond (i:int,tokens:list,error:bool):
    if tokens[i] in condiciones:
        if tokens[i]=="isfacing":
            i+=1
            if tokens[i]=="(":
                i+=1
                if tokens[i] in card:
                    i+=1
                    if tokens[i] ==")":
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
            else:
                errorSintax()
                error=True
        elif  tokens[i]=="isValid":
            i+=1
            if tokens[i]=="(":
                i+=1
                if tokens[i] in ins2:
                    i+=1
                    if tokens[i]==",":
                        i+=1
                        if tokens[i].isdigit() or (tokens[i] in variables):
                            if ("." or "-") not in tokens[i] and tokens[i].isdigit():
                                i+=1                   
                            elif isinstance(variables[tokens[i]], int) and (tokens[i] in variables):
                                i+=1
                            else:
                                errorSintax()   
                                error=True
                        else:
                            errorSintax()    
                            error=True
                        d,error=evalins([tokens[i-3],"(",tokens[i-1],")"],1,error,False)    
                    elif  tokens[i][0]==",":
                        if tokens[i][1:].isdigit() and not (("." or "-") in tokens[i]):
                            i+=1
                            d,error=evalins([tokens[i-3],"(",tokens[i-1][1:],")"],1,error,False)
                        else:
                            errorSintax()    
                            error=True    
                    else:
                        errorSintax()    
                        error=True 
        elif tokens[i]=="canWalk":
            i+=1
            if tokens[i]=="(":              
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
                if param=="2":

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
                else:          
                    if  (tokens[i] in direcciones2) or (tokens[i] in card):
                        i+=1
                        i,error=explorarparam(2,tokens,i)        
                    else:
                        errorSintax()
                        error=True   
        elif tokens[i]=="not":
            i+=1
            if tokens[i]=="(":
                i+=1 
                i,error=evalcond(i,tokens,error)                                  
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
                        errorSintax(getframeinfo(currentframe()))
                        error=True
                    elif tokens[i]!= ",":
                        variables[tokens[i]]= " "
                    i+=1
                    if tokens[i]== "GORP":
                        errorSintax(getframeinfo(currentframe()))
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
                                    errorSintax(getframeinfo(currentframe()))  
                                    error=True
                                elif (("." or "-") in k) and (k not in variables):
                                    errorSintax(getframeinfo(currentframe()))   
                                    error=True
                                elif (k in variables):
                                    if not(isinstance(variables[k], int)):
                                        errorSintax(getframeinfo(currentframe()))   
                                        error=True      
                            i+=1          
                        elif 0==len(param) or len(param)>=2:
                            errorSintax(getframeinfo(currentframe()))
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
                                errorSintax(getframeinfo(currentframe()))
                                error=True 
                        else:
                            errorSintax(getframeinfo(currentframe()))
                            error=True        
                                         
                    else:
                        errorSintax(getframeinfo(currentframe()))
                        error=True    


            ##PROCESOS Y BLOQUE DE INSTRUCCIONES##
            elif tokens[i] == 'PROC':
                if tokens[i] in instrucciones:  
                    ins = []
                    count = 0
                    procedimientos = []
                    estControl = []
                    while tokens[i] != 'CORP' and not(error):
                        if tokens[i] == 'PROC' and tokens[i+3] == ')': 
                            ##Estructuras de control
                            while tokens[i] != '}':
                                estControl.append(tokens[i])
                                i+=1
                            if estControl[2] != '(':
                                errorSintax(getframeinfo(currentframe()))
                            if estControl[3] != ')':
                                errorSintax(getframeinfo(currentframe()))
                            if estControl[4] != '{':
                                errorSintax(getframeinfo(currentframe()))
                            if estControl[5] in condicionales:
                                condicionalx = estControl[5]
                                if condicionalx == 'while':
                                    try:
                                        if estControl[6] != '(':
                                            errorSintax(getframeinfo(currentframe()))
                                        if estControl[7] == ' ':
                                            errorSintax(getframeinfo(currentframe()))
                                        if estControl[8] != ')':
                                            errorSintax(getframeinfo(currentframe()))
                                        if estControl[9] != 'do':
                                            errorSintax(getframeinfo(currentframe()))
                                        if estControl[10] == ' ':
                                            errorSintax(getframeinfo(currentframe()))
                                        if estControl[11] != 'od':
                                            errorSintax(getframeinfo(currentframe()))
                                    except:
                                        errorSintax(getframeinfo(currentframe()))

                                if condicionalx == 'repeatTimes':
                                    print(1) ##Falta este entero


                                if condicionalx == 'if':
                                    print(estControl)
                                    try: 
                                        if estControl[6] != '(':
                                            errorSintax(getframeinfo(currentframe()))
                                        if estControl[7] == 'isfacing':
                                            print('evalcond') ##NECESITA VERIFICAR LA CONDICION.
                                            if estControl[11] != ')':
                                                errorSintax(getframeinfo(currentframe()))
                                            if estControl[12] != '{':
                                                errorSintax(getframeinfo(currentframe()))
                                            if estControl[13] in instrucciones:
                                                print("Necesita evalins") ##NECESITA VERIFICAR LA INSTRUCCION.
                                            
                                        
                                        if estControl[7] == 'not':
                                            if estControl[11] != ')':
                                                errorSintax(getframeinfo(currentframe()))
                                            if estControl[12] != '{':
                                                errorSintax(getframeinfo(currentframe()))
                                            
                                        if estControl[7] in condicions2param:
                                            if estControl[12] != ')':
                                                errorSintax(getframeinfo(currentframe()))
                                            if estControl[13] != '{': 
                                                errorSintax(getframeinfo(currentframe()))

                                            if estControl[22] == 'else':
                                                print(1)
                                                if estControl[11] == '{': ##BLOCK2
                                                    errorSintax(getframeinfo(currentframe()))
                                                if estControl[12] != 'fi':
                                                    errorSintax(getframeinfo(currentframe()))

                                    except:
                                        errorSintax(getframeinfo(currentframe()))
                                
                            

                        elif tokens[i] == 'PROC' and tokens[i+3] != ')':
                            i+=1
                            while tokens[i] != '}' and not(error):
                                procedimientos.append(tokens[i])
                                i+=1
                            if procedimientos[1] != '(':
                                errorSintax(getframeinfo(currentframe()))
                                error = True

                            #Chequea bracket al inicio del bloque#
                            sintaxBrackets = sintaxChecker('{', procedimientos)
                            if sintaxBrackets != True:
                                errorSintax(getframeinfo(currentframe()))

                            for each in procedimientos:
                                if each in instrucciones:
                                    ins.append(each)
                                
                                
                            #Chequea si las instrucciones tienen variable dentro y ambos parentesis#
                            while count < len(ins):
                                pos = procedimientos.index(ins[count])
                                if procedimientos[pos+1] != '(':
                                    errorSintax(getframeinfo(currentframe()))
                                if procedimientos[pos+3] != ')':
                                    errorSintax(getframeinfo(currentframe()))
                                else:
                                    count+=1
                        
                        else:
                            error = True
            elif tokens[i] in instrucciones:
                i+=1
                print(tokens)
                i,error=evalins(tokens,i,error,True)
            elif tokens[i] in variables :
                i+=1
                if tokens[i]=="=" or (tokens[i][0]=="=" and (tokens[i][1:].isdigit())):
                    i+=1
                    if (("." or "-") not in tokens[i]) and (tokens[i].isdigit()):
                        i+=1
                        if tokens[i]==";":
                            variables[tokens[i-3]]=int(tokens[i-1])
                            print(variables)
                            i+=1
                        else:
                            errorSintax(getframeinfo(currentframe()))
                            error=True
                    elif (("." or "-") not in tokens[i-1]):
                        if tokens[i]==";":
                            variables[tokens[i-2]]=int(tokens[i-1][1])
                            print(variables)
                            i+=1
                        else:
                            errorSintax(getframeinfo(currentframe()))
                            error=True


                    else:
                        errorSintax(getframeinfo(currentframe()))
                        error=True
                else:
                    errorSintax(getframeinfo(currentframe()))
                    error=True

            elif "=" in tokens[i]:
                p=""
                param=[]
                for k in tokens[i]:
                    if k!="=":
                        p+=k  
                    else:
                        if not(p in variables):
                            errorSintax(getframeinfo(currentframe()))
                            error=True
                        else:
                            param.append(p)
                            p="" 
                param.append(p)               
                if not(p.isdigit()) or (("." or "-") in p):
                    if tokens[i+1].isdigit() and (("."or"-" not in tokens[i+1])):
                        i+=2
                        if tokens[i]==";":
                            variables[param[0]]=int(tokens[i-1])
                            print(variables)
                            i+=1
                        else:
                            errorSintax(getframeinfo(currentframe()))
                            error=True    
                    else:    
                        errorSintax(getframeinfo(currentframe()))
                        error=True
                else:
                    i+=1
                    if tokens[i]==";":
                        variables[param[0]]=int(param[1])
                        print(variables)
                        i+=1 
                    else:
                        errorSintax(getframeinfo(currentframe()))
                        error=True       

            else:
                errorSintax(getframeinfo(currentframe()))
                error=True



        #print(tokens)

    ##Si no empieza por PROG y termina en GORP       
    else:
        errorSintax(getframeinfo(currentframe())) 





if __name__ == "__main__":
    main()
