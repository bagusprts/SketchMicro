# test_sketchmicro.py
"""
Tests for SketchMicro module.
"""

import unittest
from sketchmicro import SketchMicro

class TestSketchMicro(unittest.TestCase):
    """Test cases for SketchMicro class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SketchMicro()
        self.assertIsInstance(instance, SketchMicro)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SketchMicro()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
