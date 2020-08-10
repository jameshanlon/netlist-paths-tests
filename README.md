# Netlist paths tests

This repository contains additional tests for the netlist paths tool, using
third-party Verilog designs.

## Dependencies

- C/C++ compiler
- Python3
- Boost (minimum 1.68.0)
- CMake (minimum 3.12.0)

## Building

```
git submodule update --init --recursive
mkdir Release
cd Release
cmake .. -DCMAKE_BUILD_TYPE=Release
cmake -j8
```

# Run the tests

```
cd Release
ctest .
```
