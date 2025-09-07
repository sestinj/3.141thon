# 3.141thon

A powerful, flexible, and concise scripting language built on Python. 3.141thon combines familiar Python-like syntax with unique mathematical notation inspired by π.

## Features

3.141thon currently supports:

- ✅ **Variables and expressions** - Dynamic variable assignment and evaluation
- ✅ **Functions** - First-class function definitions with parameters
- ✅ **Control flow** - If/else statements, for loops, and while loops
- ✅ **Data structures** - Arrays and dictionaries with subscripting support
- ✅ **Nested scopes** - Proper variable scoping within functions and blocks
- ✅ **Operators** - Full range of arithmetic, comparison, and logical operators
- ✅ **Built-in functions** - Essential functions like print, len, str, and more

## Quick Start

1. **Run the interpreter:**
   ```bash
   python NL.py
   ```

2. **Initial code execution:**
   - Any code in `NLCode.txt` runs automatically on startup
   - Interactive REPL appears for line-by-line execution

3. **Interactive mode:**
   - Enter commands at the `>>>` prompt
   - Each statement should end with a semicolon `;`

## Language Syntax

### Variables
```python
# Assign different data types
varName = 2;
varName = "string";
varName = [1, 2, 3];
```

### Functions
```python
# Function definition
nameOfFunction(param1, param2) = {
    varName = param1 + param2;
    return(varName);
};

# Function call
nameOfFunction(4, 6);
```

### Arrays and Subscripting
```python
# Create and manipulate arrays
array = [1, 2, [3, 4]];
print(array[2][0]);  # Prints 3
array[0] = [0, 1];   # Modify elements
```

### Dictionaries
```python
# Dictionary creation and access
d = ["one":1, "two":2];
d["three"] = 3;
print(d["one"]);
```

### Control Flow

#### For Loops
```python
# Loop from 1 to 10
for(i, 1, 11) = {
    j = i * 2;
    print(j);
};
```

#### While Loops
```python
# While loop with condition
a = 1;
b = 10;
while("a<b", {
    a += 1;
    print(a);
});
```

#### If/Else Statements
```python
# Conditional execution
a = 4;
b = 5;
if(a < b, {
    print(b - a);
}, {
    print(a - b);
});
```

## Built-in Functions

- `print(value)` - Output values to console
- `len(array)` - Get length of array or dictionary
- `str(value)` - Convert value to string
- `return(value)` - Return from function
- `scope()` - View current variable scope
- `run(code)` - Execute code from string

## Example Program

```python
# Function to calculate absolute difference
diff(a, b) = {
    if (a > b, {
        return(a - b);
    }, {
        return(b - a);
    });
};

# Test the function
result = diff(10, 7);
print("Difference: " + str(result));
```

## Project Status

This is an experimental scripting language project. While functional, it's primarily for educational and experimental purposes.

## Contributing

Feedback and contributions are welcome! Feel free to:
- Report issues or bugs
- Suggest new features
- Submit pull requests
- Share interesting 3.141thon programs

## Contact

For questions or feedback, email: sestinj@gmail.com