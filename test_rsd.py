import os
import sys
import unittest
import shutil
import subprocess
import definitions as defs
sys.path.insert(0, os.path.join(defs.BINARY_DIR_PREFIX, 'lib'))
import py_netlist_paths as np

class TestRSD(unittest.TestCase):

    def setUp(self):
        xml_file = os.path.join(defs.WORKING_DIR, 'rsd.xml')
        log_file = os.path.join(defs.WORKING_DIR, 'rsd.log')
        test_directory = os.path.join(defs.SOURCE_DIR, 'thirdparty', 'rsd', 'Processor', 'Src')
        # Remove the XML file in tree.
        if os.path.exists(os.path.join(test_directory, 'rsd.xml')):
            os.remove(os.path.join(test_directory, 'rsd.xml'))
        with open(log_file, 'wb') as fp:
            proc = subprocess.Popen(['make', '-f', os.path.join(defs.SOURCE_DIR, 'rsd.Makefile.netlist-paths.mk'),
                                          'VERILATOR_BIN='+defs.VERILATOR_EXE],
                                    stdout=fp, stderr=subprocess.STDOUT,
                                    cwd=test_directory)
            proc.wait()
        # Copy the XML file back out.
        shutil.copyfile(os.path.join(test_directory, 'rsd.xml'),
                        os.path.join(defs.WORKING_DIR, 'rsd.xml'))
        np.Options.get_instance().set_error_on_unmatched_node(True)
        self.netlist = np.Netlist(xml_file)

  def test_rsd(self):
      pass

if __name__ == '__main__':
    unittest.main()
