## Python execution flow: source → AST → bytecode → interpreter (machine-level execution)

This note explains how Python (specifically CPython, the reference implementation) processes your code:

### 1) Source code → Tokens → AST
- **Lexing (tokenization)**: The source `.py` text is turned into a stream of tokens (names, numbers, strings, operators, etc.).
- **Parsing → AST**: Tokens are parsed into an **Abstract Syntax Tree (AST)** that structurally represents your program. The AST captures the semantics of statements and expressions independent of concrete syntax.

Why AST matters:
- **Validation and errors**: Syntax errors are detected here.
- **Optimizations and analysis**: The compiler can perform simple optimizations and constant folding; tools can analyze/transform code using the `ast` module.

### 2) AST → Bytecode (code objects)
- **Compilation**: CPython compiles the AST into **bytecode**, packaged in immutable **code objects**.
- **Caching**: Compiled bytecode may be cached in `__pycache__/module.<magic>.pyc` to skip recompilation on subsequent runs (if timestamps and the CPython “magic number” match).

Key points about bytecode:
- Bytecode is a compact, VM-level instruction set (e.g., `LOAD_CONST`, `CALL`, `RETURN_VALUE`).
- It is portable across platforms for the same CPython version, but not across different major CPython versions.

### 3) Bytecode → Interpreter execution (to the machine level)
- **Evaluation loop**: CPython’s virtual machine runs a tight C loop (often called the "ceval loop"). It repeatedly fetches a bytecode instruction, decodes it, and executes the corresponding C code.
- **Objects and C implementations**: Python objects (ints, lists, functions, etc.) are C structs. Most operations (like addition, attribute access, calls) ultimately invoke C functions operating on these structs.
- **Machine-level execution**: The interpreter itself is compiled native code. When it executes bytecode, control flows through compiled C functions and eventually to CPU instructions. In CPython there is generally no JIT to native machine code for your Python functions (contrast: PyPy has a JIT).

Frames, stack, and scope:
- Each executing function has a **frame** (locals, globals, instruction pointer, and a data stack for operands/intermediates).
- Bytecode is **stack-based**: instructions push/pop values on an evaluation stack.

### 4) Where AST is exposed to you
- The `ast` standard library lets you parse, inspect, and transform Python code programmatically.
- Example uses: linters, code formatters, static analyzers, macro-like transformations (via source-to-source rewriting), and security scanners.

### 5) Minimal example
```python
# save as demo.py
import ast, dis

source = "x = 2 + 3\nprint(x)\n"

# Parse to AST
tree = ast.parse(source)
print(ast.dump(tree, indent=2))

# Compile to bytecode (code object)
code_obj = compile(source, filename="<memory>", mode="exec")

# Disassemble bytecode
dis.dis(code_obj)
```

What you’ll see:
- A structured AST with `Assign`, `BinOp`, `Call`, etc.
- A disassembly showing bytecode like `LOAD_CONST 2`, `LOAD_CONST 3`, `BINARY_ADD`, `STORE_NAME x`, `LOAD_NAME print`, `CALL`, `RETURN_VALUE`.

### 6) Quick FAQ
- **Does Python compile to native machine code?** Not in CPython by default. It compiles to bytecode that a C-based interpreter executes. Native code may appear via C extensions, `ctypes`, `cffi`, NumPy internals, or alternative runtimes (e.g., PyPy JIT).
- **Why .pyc files?** To avoid recompiling unchanged modules; they store bytecode plus a header (timestamp/hash + magic number).
- **Is AST the same as bytecode?** No. AST is a high-level syntactic/semantic tree; bytecode is a low-level VM instruction stream derived from the AST.

### 7) One-sentence summary
Python (CPython) turns source → tokens → AST → bytecode, then a C interpreter executes that bytecode, which drives actual CPU instructions; the AST is the structured, high-level representation used during compilation and available to you via the `ast` module.


