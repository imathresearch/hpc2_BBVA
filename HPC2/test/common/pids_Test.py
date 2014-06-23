import unittest
from HPC2.common import pids

class pids_Test(unittest.TestCase):
    
    def setUp(self):
        pass
        
    def tearDown(self):
        pass
    
    # We check that init() works properly
    def test_init(self):
        pids.init()
        pids.addEntry("123","hola")
        self.assertEqual(pids.getProcess("123"), "hola");
        pids.init()
        self.assertEqual(pids.getProcess("123"), None);
        
    def test_addModifyDeleteValues(self):
        pids.init()
        
        # Add two elements
        pids.addEntry("123","hola")
        pids.addEntry("124","adeu")
        
        # Check both are in
        self.assertEqual(pids.getProcess("123"), "hola");
        self.assertEqual(pids.getProcess("124"), "adeu");
        
        # Check element 125 is not there
        self.assertEqual(pids.getProcess("125"), None);
        
        dictMine = pids.getDict()
        del dictMine["123"]
        del dictMine["124"]
        pids.saveDict(dictMine)
        self.assertEqual(pids.getProcess("124"), None);
        self.assertEqual(pids.getProcess("123"), None);

if __name__ == '__main__':
    unittest.main()