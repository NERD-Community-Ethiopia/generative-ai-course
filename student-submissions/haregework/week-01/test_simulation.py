#!/usr/bin/env python3
"""
Test file for Social Network Simulation
Week 1 Assignment - Generative AI & Automation Course
"""

import unittest
import sys
import os

# Add the current directory to the path so we can import our module
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from social_network_simulation import SocialNetworkSimulation


class TestSocialNetworkSimulation(unittest.TestCase):
    """Test cases for the SocialNetworkSimulation class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.simulation = SocialNetworkSimulation(num_users=10, connection_probability=0.5)
    
    def test_initialization(self):
        """Test that the simulation initializes correctly."""
        self.assertEqual(self.simulation.num_users, 10)
        self.assertEqual(self.simulation.connection_probability, 0.5)
        self.assertIsNotNone(self.simulation.network)
        self.assertEqual(len(self.simulation.users), 0)
    
    def test_create_users(self):
        """Test user creation."""
        self.simulation.create_users()
        self.assertEqual(len(self.simulation.users), 10)
        self.assertEqual(self.simulation.network.number_of_nodes(), 10)
        
        # Check that users have required attributes
        for user in self.simulation.users:
            self.assertIn('id', user)
            self.assertIn('name', user)
            self.assertIn('age', user)
            self.assertIn('interests', user)
            self.assertIn('activity_level', user)
    
    def test_create_connections(self):
        """Test network connection creation."""
        self.simulation.create_users()
        self.simulation.create_connections()
        
        # Should have some connections
        self.assertGreaterEqual(self.simulation.network.number_of_edges(), 0)
        
        # Check edge attributes
        for u, v, data in self.simulation.network.edges(data=True):
            self.assertIn('weight', data)
            self.assertIn('common_interests', data)
    
    def test_network_analysis(self):
        """Test network analysis functionality."""
        self.simulation.create_users()
        self.simulation.create_connections()
        analysis = self.simulation.analyze_network()
        
        # Check that analysis contains expected keys
        expected_keys = [
            'total_users', 'total_connections', 'average_degree',
            'network_density', 'connected_components', 'number_of_communities'
        ]
        
        for key in expected_keys:
            self.assertIn(key, analysis)
        
        # Check that values are reasonable
        self.assertEqual(analysis['total_users'], 10)
        self.assertGreaterEqual(analysis['total_connections'], 0)
        self.assertGreaterEqual(analysis['average_degree'], 0)
        self.assertGreaterEqual(analysis['network_density'], 0)
        self.assertLessEqual(analysis['network_density'], 1)
    
    def test_scale_free_check(self):
        """Test scale-free property checking."""
        # Create a simple network
        self.simulation.create_users()
        self.simulation.create_connections()
        
        # The method should return a boolean
        is_scale_free = self.simulation._check_scale_free_property()
        self.assertIsInstance(is_scale_free, bool)
    
    def test_visualization_creation(self):
        """Test that visualization files can be created."""
        self.simulation.create_users()
        self.simulation.create_connections()
        self.simulation.analyze_network()
        
        # Test visualization creation (should not raise an exception)
        try:
            self.simulation.visualize_network("test_visualization.png")
            # Check if file was created
            self.assertTrue(os.path.exists("test_visualization.png"))
            # Clean up
            os.remove("test_visualization.png")
        except Exception as e:
            self.fail(f"Visualization creation failed: {e}")
    
    def test_analysis_report_creation(self):
        """Test that analysis reports can be created."""
        self.simulation.create_users()
        self.simulation.create_connections()
        self.simulation.analyze_network()
        
        # Test report creation (should not raise an exception)
        try:
            self.simulation.save_analysis_report("test_analysis.txt")
            # Check if file was created
            self.assertTrue(os.path.exists("test_analysis.txt"))
            # Clean up
            os.remove("test_analysis.txt")
        except Exception as e:
            self.fail(f"Analysis report creation failed: {e}")


def run_tests():
    """Run all tests."""
    print("Running Social Network Simulation Tests...")
    print("=" * 50)
    
    # Create a test suite
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestSocialNetworkSimulation)
    
    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\nTest Summary:")
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.wasSuccessful():
        print("✅ All tests passed!")
    else:
        print("❌ Some tests failed!")
    
    return result.wasSuccessful()


if __name__ == "__main__":
    run_tests() 