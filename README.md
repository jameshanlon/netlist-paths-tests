# Netlist paths tests

This repository contains additional tests for the netlist paths tool, using
third-party Verilog designs.

## Compile and run

```
git submodule update --init --recursive
mkdir Release
cd Release
cmake .. -DCMAKE_BUILD_TYPE=Release
cmake -j8 install
```
