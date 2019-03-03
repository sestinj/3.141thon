class Token:
    def __init__(self,value,typ:str):
        #number,symbol(var,operator),instructions(func,loop)
        self.value=value
        self.typ=typ
class Function:
    def __init__(self,variables:list,chars:str):
        self.variables=variables
        self.chars=chars
TOKENS="+= -= *= /= == != <= >= && || + - / * % ^ = < > ( ) { } [ ] . , \" -> ;".split(" ") #must be in order of largest to smallest
OPERATORS=[[' . '], [' ^ '],[' * ',' / ',' % '], [' + ',' - '], [' == ',' != ',' < ',' > ',' <= ',' >= '], [' && ',' || '], [' = '],[' -> ']] #The spaces show where values to be evaluated should be #Order of operations: first in array are evaluated first
OPERATORS_NOSPACE=[['.'], ['^'], ['*','/','%'],['+','-'], ['==','!=','<','>','<=','>='], ['&&','||'], ['='],['->']]
KEYWORDS=["if", "rtn"]
SCOPE=[{'len':Function(['array'],"")}]#An array of dictionaries - most specific scope is last - THIS IS WHERE ALL BUILT IN FUNCTIONS GO
def saveToScope(var:str,val):
    #Look for the variable already existing, starting in the most local scope. If it doesn't exist anywhere, add it to the most local scope.
    for i in range(len(SCOPE)):
        idx=len(SCOPE)-i-1
        scope=SCOPE[idx]
        if var in scope:
            scope[var]=val
            return
    SCOPE[len(SCOPE)-1][var]=val
def expandArray(array):
    temp=array.copy()
    #In: array
    #Out: array, but all inner arrays are disbanded to become one long array (not necessarily in order)
    containsArray=True
    while containsArray:
        containsArray = False
        for i in range(len(temp)):
            if type(temp[i])==list:
                containsArray=True
        for i in range(len(temp)):
            if type(temp[i])==list:
                if len(temp[i])>0:
                    for j in range(len(temp[i])):
                        temp.append(temp[i][j])
                temp.pop(i)              
    return temp
def isWhiteSpace(string:str)->bool:
    rtn=True
    for char in string:
        if char != " ":
            rtn=False
    return rtn
def listToString(lst:list)->str:
    string=''
    for sub in lst:
        if type(sub)==type(Token("","")): #Because quotes are put together before stuff inside curly braces, they have to be switched back to string form
            sub=sub.string
        string+=sub
    return string
def tokenize(chars:str) -> list:
    #raw input -> tokens
    chars=chars.replace('\n',' ') #new lines become spaces - ALL LINES MUST END IN SEMICOLON
    chars=chars.replace('\t',' ')
    if type(chars)==str:chars=chars.split(" ")
    for token in TOKENS:
        #Remove extra white space
        dl=0
        for i in range(len(chars)):
            if isWhiteSpace(chars[i-dl]):
                chars.pop(i-dl)
                dl+=1
        #Split up each string further if it isn't already a token and add the parts back to the main list       
        i=0
        while i < len(chars):
            #What's with the while loop?: When chars are split and inserted into the list, they extend the length, so a for loop won't make it to the end
            char=chars[i] #each string
            if char in TOKENS:
                i+=1
                continue #if it isn't already a token
            char=char.replace(token,' '+token+' ') #split up
            char=char.split(" ") #the parts
            chars.pop(i)
            for j in range(len(char)):
                chars.insert(i+j,char[j]) #add the parts back to the main list
            i+=1
    #Remove extra white space
        dl=0
        for i in range(len(chars)):
            if isWhiteSpace(chars[i-dl]):
                chars.pop(i-dl)
                dl+=1
    return chars
def getValue(token):
    #What about for functions?
    if not type(token)==type(Token("","")):return token
    if token.typ=="variable":
        for i in range(len(SCOPE)):
            scope=SCOPE[len(SCOPE)-i-1]
            if token.value in scope:
                return scope[token.value]
    return token.value
digits="1234567890"
def typify(tokens:list)->list:
    #token strings -> token objects (list of lists, seperated by lines (;))
    #First, search for string literals
    inQuote=False
    start=0
    for i in range(len(tokens)):
        token=tokens[i]
        if not type(token)==str:continue #Because it is already typified
        if token=="\"":
            if not inQuote:
                start=i
                inQuote=True
            else:
                inQuote=False
                stringWQuotes=listToString(tokens[start:i]) #Get rid of quotes with the slice ([1:len(strWQuotes)]) below
                newString=Token(stringWQuotes[1:len(stringWQuotes)],"string")
                for k in range(start,i):
                    tokens.pop(start)
                tokens[start]=newString
                return typify(tokens)
    #Second, search for instructions
    braceCount=0
    start=0
    for i in range(len(tokens)):
        token=tokens[i]
        if not type(token)==str:continue #Because it is already typified
        if token=='{':
            if braceCount==0:
                start=i
            braceCount+=1
        elif token=='}':
            braceCount-=1
            if braceCount==0:
                newInstruction=Token(listToString(tokens[start+1:i]),"instruction")
                for k in range(start,i):
                    tokens.pop(start)
                tokens[start]=newInstruction
                return typify(tokens)
    #Then look for numbers, variables, operators (numbers have to start with a digit, strings have to start with a quotation, variables have to start with a letter, operators have to start with a non-digit-non-letter-non-quotation-non-parenthese character)
    for i in range(len(tokens)):
        token=tokens[i]
        if not type(token)==str:continue #Because it is already typified
        if token[0] in digits:
            #Number
            newNum=int(token)
            if i+2<len(tokens) and tokens[i+1]=="." and tokens[i+2]:
                #Float
                newNum=float(newNum)+float(tokens[i+2])/(10**len(tokens[i+2]))
                tokens.pop(i);tokens.pop(i);tokens[i]=Token(newNum,"float") #replace strings with new float
                return typify(tokens)
            else:
                #Int
                tokens[i]=Token(newNum,"int")
                return typify(tokens)
        elif token in expandArray(OPERATORS_NOSPACE):
            tokens[i]=Token(token, "operator")
            return typify(tokens)
        elif token in TOKENS:
            tokens[i]=Token(token, "token")
            return typify(tokens)
        elif token=="true":
            tokens[i]=True
            return typify(tokens)
        elif token=="false":
            tokens[i]=False
            return typify(tokens)
        else:
            tokens[i]=Token(token, "variable")
            return typify(tokens)
    #Seperate the lines
    finalLines=[]
    current=[]
    for i in range(len(tokens)):
        if equal(tokens[i],';'):
            finalLines.append(current)
            current=[]
        else:
            current.append(tokens[i])
    if len(current)>0:finalLines.append(current)
    return finalLines
#Order of evaluation: do stuff in () and [],.operator,[subscript]operator,operators
def operate(tokens:list,opIdx:int):
    #In: token list, index of the operator (in the case of non-unary operators, the index of the first part is given)
    op=tokens[opIdx].value
    
    #BINARY:
    lhs=getValue(tokens[opIdx-1])
    rhs=getValue(tokens[opIdx+1])
    ans=1
    if op==".":
        print(". not yet operable")
    elif op=="^":
        ans=lhs**rhs
    elif op=="*":
        ans=lhs*rhs
    elif op=="/":
        ans=lhs/rhs
    elif op=="%":
        ans=lhs%rhs
    elif op=="+":
        ans=lhs+rhs
    elif op=="-":
        ans=lhs-rhs
    elif op=="==":
        ans=lhs==rhs
    elif op=="!=":
        ans=lhs!=rhs
    elif op=="<":
        ans=lhs<rhs
    elif op==">":
        ans=lhs>rhs
    elif op=="<=":
        ans=lhs<=rhs
    elif op==">=":
        ans=lhs>=rhs
    elif op=="&&":
        ans=lhs and rhs
    elif op=="||":
        ans=lhs or rhs
    elif op=="=":
        ans=rhs
        saveToScope(tokens[opIdx-1].value,rhs)
    else:
        print("Unknown operator: " + op)
    tokens.pop(opIdx-1)
    tokens.pop(opIdx-1)
    tokens[opIdx-1]=ans
    return tokens
def equal(token:Token,value)->bool:
    if not type(token)==type(Token("","")):return
    if token.value==value:
        return True
    return False
def evaluate(tokenss:list): #Input is a list of lists (each representing one line)
    for l in range(len(tokenss)): #Evaluate each line
        tokens=tokenss[l]
        #Condenses list of tokens into a single value, running instructions in the list
        #Whenever something is evaluated, this function is recursively called so it can start fresh
        for i in range(len(tokens)):
            token=tokens[i]
            if not type(token)==type(Token("","")):continue#This is to avoid trying to evaluate an already simplified value (non token object, for example a python int)
            if not type(token.value)==str:continue#This is because a parthese or bracket will always be a string
            token=token.value
            if token==')' or token==']':
                if token==')':lookingFor='('
                else:lookingFor='['
                count=0
                while True:
                    count+=1
                    if equal(tokens[i-count],lookingFor):
                        if type(tokens[i-count-1])==type(Token('','')):
                            if tokens[i-count-1].typ=="variable":
                                #These parentheses are for functions() or arrrays[]
                                if lookingFor=='(':
                                    #Function
                                    if tokens[min(i+1,len(tokens)-1)].value=='=':
                                        funcName=tokens[i-count-1].value
                                        if funcName=='for':
                                            #For loop
                                            array=[] #[i,startIdx,endIdx]
                                            current=[]
                                            for j in range(i-count+1,i):
                                                if type(tokens[j])==type(Token("","")):
                                                    if type(tokens[j].value)==str:
                                                        if tokens[j].value==",":
                                                            array.append(evaluate([current])[0])
                                                            current=[]
                                                        else:
                                                            current.append(tokens[j])
                                                    else:
                                                        current.append(tokens[j])
                                                else:
                                                    current.append(tokens[j])
                                            if len(current)>0:array.append(evaluate([current])[0])
                                            chars=tokens[i+2].value
                                            function=Function([array[0]],chars)
                                            SCOPE[len(SCOPE)-1]['for']=function #Always save to the most specific scope, so there can be nested for loops
                                            for j in range(i-count-1,i+2):
                                                tokens.pop(i-count-1)
                                            #Store each result of the loop in the results list, so they can be evaluated seperately
                                            results=[]
                                            for j in range(array[1],array[2]):
                                                print(j)
                                                results.append(evaluate(typify(tokenize("for("+str(j)+");")))[0])
                                            tokens[i-count-1]=results
                                            return evaluate(tokenss)
                                            break
                                        else:
                                            #Function Definition
                                            variables=[]
                                            for j in range(i-count+1,i):
                                                if not tokens[j].value==",":
                                                    variables.append(tokens[j].value)
                                            chars=tokens[i+2].value
                                            function=Function(variables,chars)
                                            saveToScope(funcName,function)
                                            for j in range(i-count-1,i+2):
                                                tokens.pop(i-count-1)
                                            tokens[i-count-1]=Token(chars,'instruction')
                                            return evaluate(tokenss)
                                            break
                                    else:
                                        #Function Call
                                        function=getValue(tokens[i-count-1])
                                        newScope={}
                                        array=[]
                                        current=[]
                                        for j in range(i-count+1,i):
                                            if type(tokens[j])==type(Token("","")):
                                                if type(tokens[j].value)==str:
                                                    if tokens[j].value==",":
                                                        array.append(evaluate([current])[0])
                                                        current=[]
                                                    else:
                                                        current.append(tokens[j])
                                                else:
                                                    current.append(tokens[j])
                                            else:
                                                current.append(tokens[j])
                                        if len(current)>0:array.append(evaluate([current])[0])
                                        for j in range(len(function.variables)):
                                            newScope[function.variables[j]]=array[j]
                                        SCOPE.append(newScope)
                                        for j in range(i-count-1,i):
                                            tokens.pop(i-count-1)
                                        tok=tokenize(function.chars)
                                        typi=typify(tok)
                                        evalu=evaluate(typi)
                                        tokens[i-count-1]=evalu[0]
                                        return evaluate(tokenss)
                                        break
                                else:
                                    #Subscripting
                                    #Evaluate the stuff in the braces
                                    tokensToEval=tokens[i-count+1:i]
                                    array=getValue(tokens[i-count-1])
                                    subscript=evaluate([tokensToEval])[0]
                                    #Replace everything in braces, including braces and array before, with new simplified expression
                                    for j in range(i-count-1,i):
                                        tokens.pop(i-count-1)
                                    tokens[i-count-1]=array[subscript]
                                    return evaluate(tokenss)
                                    break
                            else:
                                if lookingFor=='(':
                                    #Order of operations
                                    tokensToEval=tokens[i-count+1:i]
                                    new=evaluate([tokensToEval])[0]
                                    #Replace everything in parentheses, including parentheses, with new simplified expression
                                    for j in range(i-count,i):
                                        tokens.pop(i-count)
                                    tokens[i-count]=new
                                    return evaluate(tokenss)
                                    break
                                else:
                                    #Array literal
                                    array=[]
                                    current=[]
                                    for j in range(i-count+1,i):
                                        if type(tokens[j].value)==str:
                                            if tokens[j].value==",":
                                                array.append(evaluate([current])[0])
                                                current=[]
                                            else:
                                                current.append(tokens[j])
                                        else:
                                            current.append(tokens[j])
                                    if len(current)>0:array.append(evaluate([current])[0])
                                    for j in range(i-count,i):
                                        tokens.pop(i-count)
                                    tokens[i-count]=array
                                    return evaluate(tokenss)
                                    break
                        elif type(tokens[i-count-1])==list:
                            #Subscripting an array literal
                            tokensToEval=tokens[i-count+1:i]
                            subscript=evaluate([tokensToEval])[0]
                            array=tokens.pop(i-count-1)
                            for j in range(i-count,i):
                                tokens.pop(i-count-1)
                            tokens[i-count-1]=array[subscript]
                            return evaluate(tokenss)
                            break
        #Then evaluate operators
        for ops in OPERATORS_NOSPACE:
            for i in range(len(tokens)):
                token=tokens[i]
                if not type(token)==type(Token("","")):continue
                if token.value in ops:
                    tokens=operate(tokens,i)
                    return evaluate(tokenss)
        #Remove semi-colons and spaces from the array of final expressions
        dl=0
        for i in range(len(tokens)):
            token=tokens[i-dl]
            if not type(token)==type(Token("","")):
                if token==[]:
                    tokens.pop(i-dl)
                    dl+=1
                continue
            if type(token.value)==str:
                if token.value==';':
                    tokens.pop(i-dl)
                    dl+=1
        tokenss[l]=tokens
    #Change list of lists of values to a list of values - and if it is a leftover variable, change it to a value
    for i in range(len(tokenss)):
        tokenss[i]=getValue(tokenss[i][0])
    return tokenss
#while True:
    #i=input(">>> ")
file=open('NLCode.txt')
i=file.read()
nonType=tokenize(i)
    #print("nonType: "+str(nonType))
withType=typify(nonType)
    #print(withType)
    #for l in withType:
        #for t in l:
            #print(t.typ + " -> " + str(t.value))
withEval=evaluate(withType)
for e in withEval:
    print(e)
    
#/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/                        
# /\  /\  /\  /\  /\  /\  /\  /\  /\  /\  /\           
#//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\//\\
#/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \/  \
#  /\    /\    /\    /\    /\    /\
# /  \  /  \  /  \  /  \  /  \  /  \
#/ /\ \/ /\ \/ /\ \/ /\ \/ /\ \/ /\ \
# /  \  /  \  /  \  /  \  /  \  /  \ \
#/    \/    \/    \/    \/    \/    \/
#   /\      /\      /\      /\      /\      /
#  /  \    /  \    /  \    /  \    /  \    /
# /    \  /    \  /    \  /    \  /    \  /  /
#/  /\  \/  /\  \/  /\  \/  /\  \/  /\  \/  /
#  /  \    /  \    /  \    /  \    /  \    /
# /    \  /    \  /    \  /    \  /    \  /
#/      \/      \/      \/      \/      \/

#loops should print results on new lines
#should be able to programmatically create and run code using strings
#interpreter should be flexible with adding new keywords/operators/syntaxes

#loops should be treated as functions
#functions with no func keyword
#scope should be represented as a list of lists of variables, in order from largest to smallest scope. When entering a scope, simply append that new array. When exiting, simply pop it off. Always search the last(most specific)scope list, then move towards the start if the variable isn't found
#scopes are entered when there is an opening curly brace
#subscripting and arrays
#you need to make numbers into tokens,too, so checking a value is always the same. and Token.string should be Token.value
