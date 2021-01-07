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
make -j8 install
```

# Run the tests

```
cd Release
make
python3 tests.py --verbose # or 'ctest .'
```

# Included designs

- NVDLA, the Nvidia Deep Learning accelerator core (https://github.com/nvdla/hw).
- Picorv32, a 32-bit RISC-V processor core (https://github.com/cliffordwolf/picorv32).
- RSD, a 32-bit out-of-order RISC-V processor core (https://github.com/rsd-devel/rsd).
