cmake_minimum_required(VERSION 3.12.0)
project(netlist-paths-tests)
include(ExternalProject)
find_package(Python REQUIRED COMPONENTS
             Interpreter)
ExternalProject_Add(netlist-paths
  SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/netlist-paths
  PREFIX netlist-paths
  CMAKE_CACHE_ARGS
    -DCMAKE_INSTALL_PREFIX:PATH=${CMAKE_CURRENT_BINARY_DIR}/netlist-paths
  )
