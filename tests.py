import os
import sys
import unittest
import subprocess
import definitions as defs
sys.path.insert(0, os.path.join(defs.BINARY_DIR_PREFIX, 'lib'))
import py_netlist_paths as np

class NetlistPathsTests(unittest.TestCase):

    def test_verilator_exe(self):
        self.assertTrue(os.path.exists(defs.VERILATOR_EXE))

    def test_picorv32(self):
        xml_file = os.path.join(defs.WORKING_DIR, 'picorv32.xml')
        log_file = os.path.join(defs.WORKING_DIR, 'picorv32.log')
        test_directory = os.path.join(defs.SOURCE_DIR, 'thirdparty', 'picorv32')
        with open(log_file, 'wb') as fp:
            proc = subprocess.Popen([defs.VERILATOR_EXE,
                                     '--xml-only', '--flatten',
                                     '--error-limit', '10000',
                                     '--xml-output', xml_file,
                                     '--top-module', 'picorv32_axi', 'picorv32.v'],
                                    stdout=fp, stderr=subprocess.STDOUT,
                                    cwd=test_directory)
            proc.wait()
        np.Netlist(xml_file)

    def test_nvdla(self):
        xml_file = os.path.join(defs.WORKING_DIR, 'nvdla.xml')
        log_file = os.path.join(defs.WORKING_DIR, 'nvdla.log')
        test_directory = os.path.join(defs.SOURCE_DIR, 'thirdparty', 'nvdla', 'verif', 'verilator')
        with open(log_file, 'wb') as fp:
            proc = subprocess.Popen([defs.VERILATOR_EXE,
                                     '--xml-only', '--flatten',
                                     '--error-limit', '10000',
                                     '--xml-output', xml_file,
                                     '-f', 'verilator.f',
                                     '--timescale-override', '1ns'],
                                    stdout=fp, stderr=subprocess.STDOUT,
                                    cwd=test_directory)
            proc.wait()
        np.Netlist('nvdla.xml')

    def test_rsd(self):
        xml_file = os.path.join(defs.WORKING_DIR, 'rsd.xml')
        log_file = os.path.join(defs.WORKING_DIR, 'rsd.log')
        test_directory = os.path.join(defs.SOURCE_DIR, 'thirdparty', 'rsd', 'Processor', 'Src')
        with open(log_file, 'wb') as fp:
            proc = subprocess.Popen(['make', '-B', '-f', 'Makefile.verilator.mk',
                                     'XML_OUTPUT='+xml_file,
                                     'VERILATOR_BIN='+defs.VERILATOR_EXE],
                                    stdout=fp, stderr=subprocess.STDOUT,
                                    cwd=test_directory)
            proc.wait()
        np.Netlist(xml_file)


if __name__ == '__main__':
    unittest.main()
