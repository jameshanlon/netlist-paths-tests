import os
import sys
import unittest
import shutil
import subprocess
import definitions as defs
sys.path.insert(0, os.path.join(defs.BINARY_DIR_PREFIX, 'lib'))
import py_netlist_paths as np

class TestPicorv32(unittest.TestCase):

    def setUp(self):
        xml_file = os.path.join(defs.WORKING_DIR, 'picorv32.xml')
        log_file = os.path.join(defs.WORKING_DIR, 'picorv32.log')
        test_directory = os.path.join(defs.SOURCE_DIR, 'thirdparty', 'picorv32')
        with open(log_file, 'wb') as fp:
            proc = subprocess.Popen([defs.VERILATOR_EXE,
                                     '--xml-only', '--flatten',
                                     '--xml-output', xml_file,
                                     '--top-module', 'picorv32_axi', 'picorv32.v'],
                                    stdout=fp, stderr=subprocess.STDOUT,
                                    cwd=test_directory)
            proc.wait()
        self.netlist = np.Netlist(xml_file)


if __name__ == '__main__':
    unittest.main()

