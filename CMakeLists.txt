cmake_minimum_required(VERSION 3.12.0)
project(netlist-paths-tests)
include(ExternalProject)
find_package(Python3 REQUIRED COMPONENTS
             Interpreter)
enable_testing()

ExternalProject_Add(netlist-paths
  SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/netlist-paths
  PREFIX netlist-paths
  CMAKE_CACHE_ARGS
    -DCMAKE_INSTALL_PREFIX:PATH=${CMAKE_CURRENT_BINARY_DIR}/netlist-paths
    #-DCMAKE_INSTALL_RPATH_USE_LINK_PATH:BOOL=ON
    -DCMAKE_INSTALL_RPATH:PATH=${CMAKE_CURRENT_BINARY_DIR}/netlist-paths/lib
  BUILD_ALWAYS 1)

# Setup tests

configure_file(definitions.py.in
               definitions.py)

configure_file(tests.py
               ${CMAKE_CURRENT_BINARY_DIR}
               COPYONLY)

add_test(NAME tests.py
         COMMAND ${Python3_EXECUTABLE} tests.py -v
         WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR})
