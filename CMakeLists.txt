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

function(add_py_test test_name test_source_file)
  configure_file(${test_source_file}
                 ${CMAKE_CURRENT_BINARY_DIR}
                 COPYONLY)
  add_test(NAME ${test_name}
           COMMAND ${Python3_EXECUTABLE} ${test_source_file} -v
           WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR})
endfunction()

add_py_test(test_picorv32 test_picorv32.py)
add_py_test(test_rsd      test_rsd.py)
add_py_test(test_nvdla    test_nvdla.py)
