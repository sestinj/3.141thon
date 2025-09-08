# 🥧 3.141thon

**A custom, Python-inspired programming language interpreter**

3.141thon (pronounced "pi-thon") is a powerful, flexible, and concise scripting language that brings together the simplicity of Python with its own unique syntax and features. Built as an educational interpreter project, it demonstrates how programming languages work under the hood while providing a functional scripting environment.

## ✨ Features

3.141thon supports a comprehensive set of programming language features:

### Core Language Features
- **Variables & Data Types**: Integers, floats, strings, booleans
- **Expressions & Operators**: Arithmetic, comparison, logical, and assignment operators
- **Control Flow**: If/else statements, while loops, for loops
- **Functions**: User-defined functions with parameters and return values
- **Data Structures**: Arrays (lists) and dictionaries with full subscripting support
- **Scoping**: Nested scopes with proper variable resolution

### Advanced Features
- **Built-in Functions**: `print()`, `len()`, `str()`, `var()`, `scope()`, `run()`, and more
- **Interactive REPL**: Command-line interface for live code execution
- **File Execution**: Run 3.141thon scripts from files
- **Dynamic Programming**: Programmatic variable creation and code execution

## 🚀 Quick Start

### Prerequisites
- Python 3.x installed on your system

### Running 3.141thon

1. **Clone or download** this repository
2. **Run the interpreter**:
   ```bash
   python NL.py
   ```
3. **Write code** in `NLCode.txt` (executed automatically on startup)
4. **Use the interactive REPL** that appears after file execution

### Your First Program

Create or edit `NLCode.txt`:
```python
# Define a function to calculate the difference between two numbers
d(a, b) = {
    if (a > b, {
        print(a - b);
    }, {
        if (a < b, {
            print(b - a);
        }, {
            print("zero");
        })
    })
};

# Call the function
d(10, 7);
```

## 📖 Language Syntax

### Variables
```python
x = 42;
name = "Alice";
numbers = [1, 2, 3, 4, 5];
scores = ["math": 95, "science": 87];
```

### Functions
```python
# Define a function
add(a, b) = {
    result = a + b;
    return(result);
};

# Call the function
sum = add(10, 5);
print(sum);
```

### Control Flow

#### If/Else Statements
```python
age = 18;
if (age >= 18, {
    print("You can vote!");
}, {
    print("Too young to vote.");
});
```

#### For Loops
```python
# Loop from 1 to 10
for(i, 1, 11) = {
    square = i * i;
    print(square);
};
```

#### While Loops
```python
count = 1;
while("count <= 5", {
    print(count);
    count += 1;
});
```

### Data Structures

#### Arrays
```python
fruits = ["apple", "banana", "orange"];
print(fruits[0]);  # Prints "apple"
fruits[1] = "grape";  # Modify element
nested = [1, [2, 3], 4];
print(nested[1][0]);  # Prints 2
```

#### Dictionaries
```python
person = ["name": "Bob", "age": 25];
print(person["name"]);  # Prints "Bob"
person["city"] = "New York";  # Add new key-value pair
```

### Operators

#### Arithmetic
`+`, `-`, `*`, `/`, `%`, `^` (exponentiation)

#### Comparison
`==`, `!=`, `<`, `>`, `<=`, `>=`

#### Logical
`&&` (and), `||` (or)

#### Assignment
`=`, `+=`, `-=`, `*=`, `/=`

### Built-in Functions

```python
# Output and debugging
print("Hello World");

# Data manipulation
length = len([1, 2, 3, 4]);  # Returns 4
text = str(123);  # Convert to string

# Dynamic programming
var("dynamicVar", "Hello");  # Create variable programmatically
currentScope = scope();  # Get current scope variables
result = run("2 + 2");  # Execute code from string
```

## 🏗️ Project Structure

- **`NL.py`**: Main interpreter with tokenizer, parser, and evaluator
- **`NLCode.txt`**: Script file containing 3.141thon code to execute on startup
- **`README.md`**: This documentation file

## 🤝 Contributing

This is an educational project showcasing interpreter design and implementation. While not actively maintained, it demonstrates:

- **Tokenization**: Breaking source code into meaningful tokens
- **Parsing**: Converting tokens into executable structures
- **Evaluation**: Executing parsed code with proper scoping
- **REPL Implementation**: Interactive programming environment

## 📧 Contact

Got feedback, questions, or suggestions? Reach out at: **sestinj@gmail.com**

---

*3.141thon - Because every programmer needs their own slice of π*
