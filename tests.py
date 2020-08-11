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

    def test_nvdla(self):
        output_file = os.path.join(defs.WORKING_DIR, 'nvdla.xml')
        test_directory = os.path.join(defs.SOURCE_DIR, 'thirdparty', 'nvdla', 'verif', 'verilator')
        subprocess.check_call([defs.VERILATOR_EXE,
                               '--xml-only', '--flatten',
                               '--error-limit', '10000',
                               '--xml-output', output_file,
                               '-f', 'verilator.f',
                               '--timescale-override', '1ns'],
                              cwd=test_directory)
        np.NetlistPaths('nvdla.xml')

if __name__ == '__main__':
    unittest.main()
