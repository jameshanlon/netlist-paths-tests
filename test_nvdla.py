import os
import sys
import unittest
import shutil
import subprocess
import definitions as defs
sys.path.insert(0, os.path.join(defs.BINARY_DIR_PREFIX, 'lib'))
import py_netlist_paths as np

class NetlistPathsTests(unittest.TestCase):

    def test_nvdla(self):
        xml_file = os.path.join(defs.WORKING_DIR, 'nvdla.xml')
        log_file = os.path.join(defs.WORKING_DIR, 'nvdla.log')
        test_directory = os.path.join(defs.SOURCE_DIR, 'thirdparty', 'nvdla', 'verif', 'verilator')
        with open(log_file, 'wb') as fp:
            proc = subprocess.Popen([defs.VERILATOR_EXE,
                                     '--xml-only', '--flatten',
                                     '--xml-output', xml_file,
                                     '-f', 'verilator.f',
                                     '--timescale-override', '1ns'],
                                    stdout=fp, stderr=subprocess.STDOUT,
                                    cwd=test_directory)
            proc.wait()
        np.Netlist(xml_file)


if __name__ == '__main__':
    unittest.main()
