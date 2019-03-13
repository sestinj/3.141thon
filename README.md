# 3.141thon
is a powerful, flexible, and concise scripting language similar to Python (after all, that's what it is built on). Currently, 3.141thon supports the following features (but it is still progressing):

- Expressions
- Variables
- Functions
- Nested scopes
- Arrays
- For loops
- Dictionaries
- Subscripting
- While loops
- If/Else statements
- Most common operators supported
- Built in functions


## Usage:
To run 3.141thon code, open and run the file NL.py. Any 3.141thon code typed into the file NLCode.text will be run at the start, after which a command line will appear where line by line instructions can be specified.

### Setting Variables: 
```varName=2; varName="string"; varName=[1,2,3]```
### Defining functions:
```nameOfFunction(param1,param2)={varName=param1+param2;return(varName);}```
### Calling functions:
`nameOfFunction(4,6)`
### Arrays: 
`array=[1,2,[3,4]]; print(array[2][0]);array[0]=[0,1];`
### For loop:
`for(i,1,11)={j=i*2;print(j);}`
### Dictionaries:
`d=["one":1, "two":2];d["three"]=3;`
### While loop:
`a=1;b=10;while("a<b",{a+=1;print(a);})`
### If/Else statements:
`a=4;b=5;if(a<b,{print(b-a)}, {print(a-b)})`

Got any feedback? Please email me at sestinj@gmail.com
