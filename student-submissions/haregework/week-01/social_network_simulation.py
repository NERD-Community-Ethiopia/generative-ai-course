#!/usr/bin/env python3
"""
Social Network Simulation using NetworkX
Week 1 Assignment - Generative AI & Automation Course

This script creates a simulated social network, analyzes its properties,
and generates visualizations to demonstrate network analysis concepts.
"""

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
from typing import Dict, List, Tuple
import json
from datetime import datetime


class SocialNetworkSimulation:
    """
    A class to simulate and analyze social networks using NetworkX.
    """
    
    def __init__(self, num_users: int = 20, connection_probability: float = 0.3):
        """
        Initialize the social network simulation.
        
        Args:
            num_users: Number of users in the network
            connection_probability: Probability of connection between users
        """
        self.num_users = num_users
        self.connection_probability = connection_probability
        self.network = nx.Graph()
        self.users = []
        self.analysis_results = {}
        
    def create_users(self) -> None:
        """Create users with random names and attributes."""
        first_names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", 
                      "Henry", "Ivy", "Jack", "Kate", "Liam", "Mia", "Noah", "Olivia",
                      "Paul", "Quinn", "Ruby", "Sam", "Tina"]
        
        last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia",
                     "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez",
                     "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore",
                     "Jackson", "Martin"]
        
        for i in range(self.num_users):
            user = {
                'id': i,
                'name': f"{random.choice(first_names)} {random.choice(last_names)}",
                'age': random.randint(18, 65),
                'interests': random.sample(['AI', 'Music', 'Sports', 'Cooking', 'Travel', 
                                          'Technology', 'Art', 'Science', 'Reading', 'Gaming'], 
                                         random.randint(2, 5)),
                'activity_level': random.uniform(0.1, 1.0)
            }
            self.users.append(user)
            self.network.add_node(i, **user)
    
    def create_connections(self) -> None:
        """Create connections between users based on similarity and randomness."""
        for i in range(self.num_users):
            for j in range(i + 1, self.num_users):
                # Calculate similarity based on interests and age
                user_i = self.users[i]
                user_j = self.users[j]
                
                # Interest similarity
                common_interests = len(set(user_i['interests']) & set(user_j['interests']))
                interest_similarity = common_interests / max(len(user_i['interests']), 
                                                          len(user_j['interests']))
                
                # Age similarity (closer ages = higher similarity)
                age_diff = abs(user_i['age'] - user_j['age'])
                age_similarity = max(0, 1 - (age_diff / 50))
                
                # Combined similarity
                similarity = (interest_similarity * 0.7) + (age_similarity * 0.3)
                
                # Connection probability based on similarity and random factor
                connection_prob = similarity * self.connection_probability
                
                if random.random() < connection_prob:
                    weight = similarity * user_i['activity_level'] * user_j['activity_level']
                    self.network.add_edge(i, j, weight=weight, 
                                        common_interests=common_interests)
    
    def analyze_network(self) -> Dict:
        """Analyze the network and return comprehensive statistics."""
        analysis = {}
        
        # Basic network properties
        analysis['total_users'] = self.network.number_of_nodes()
        analysis['total_connections'] = self.network.number_of_edges()
        analysis['average_degree'] = sum(dict(self.network.degree()).values()) / self.num_users
        analysis['network_density'] = nx.density(self.network)
        analysis['connected_components'] = nx.number_connected_components(self.network)
        
        # Path analysis
        if nx.is_connected(self.network):
            analysis['average_path_length'] = nx.average_shortest_path_length(self.network)
            analysis['diameter'] = nx.diameter(self.network)
        else:
            analysis['average_path_length'] = float('inf')
            analysis['diameter'] = float('inf')
        
        # Centrality measures
        degree_centrality = nx.degree_centrality(self.network)
        betweenness_centrality = nx.betweenness_centrality(self.network)
        closeness_centrality = nx.closeness_centrality(self.network)
        
        analysis['most_connected_user'] = max(degree_centrality.items(), key=lambda x: x[1])
        analysis['most_central_user'] = max(betweenness_centrality.items(), key=lambda x: x[1])
        analysis['most_closeness_user'] = max(closeness_centrality.items(), key=lambda x: x[1])
        
        # Community detection
        communities = list(nx.community.greedy_modularity_communities(self.network))
        analysis['number_of_communities'] = len(communities)
        analysis['largest_community_size'] = max(len(community) for community in communities)
        
        # Network type analysis
        analysis['is_scale_free'] = self._check_scale_free_property()
        
        self.analysis_results = analysis
        return analysis
    
    def _check_scale_free_property(self) -> bool:
        """Check if the network follows scale-free properties."""
        degrees = [d for n, d in self.network.degree()]
        if len(degrees) < 3:
            return False
        
        # Simple check: if there are high-degree nodes (hubs)
        max_degree = max(degrees)
        avg_degree = sum(degrees) / len(degrees)
        
        # Network is scale-free if max degree is significantly higher than average
        return max_degree > avg_degree * 2
    
    def visualize_network(self, filename: str = "network_visualization.png") -> None:
        """Create and save a network visualization."""
        plt.figure(figsize=(12, 10))
        
        # Position nodes using spring layout
        pos = nx.spring_layout(self.network, k=1, iterations=50)
        
        # Draw nodes with size based on degree
        node_sizes = [self.network.degree(node) * 100 for node in self.network.nodes()]
        nx.draw_networkx_nodes(self.network, pos, node_size=node_sizes, 
                             node_color='lightblue', alpha=0.7)
        
        # Draw edges with width based on weight
        edge_weights = [self.network[u][v]['weight'] * 3 for u, v in self.network.edges()]
        nx.draw_networkx_edges(self.network, pos, width=edge_weights, 
                             alpha=0.5, edge_color='gray')
        
        # Add labels for some nodes (to avoid clutter)
        labels = {node: self.users[node]['name'].split()[0] 
                 for node in self.network.nodes() 
                 if self.network.degree(node) > 2}
        nx.draw_networkx_labels(self.network, pos, labels, font_size=8)
        
        plt.title("Social Network Simulation", fontsize=16, fontweight='bold')
        plt.axis('off')
        plt.tight_layout()
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        plt.close()
        
        print(f"Network visualization saved as: {filename}")
    
    def save_analysis_report(self, filename: str = "network_analysis.txt") -> None:
        """Save detailed analysis report to a text file."""
        with open(filename, 'w') as f:
            f.write("SOCIAL NETWORK ANALYSIS REPORT\n")
            f.write("=" * 40 + "\n\n")
            f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            f.write("NETWORK STATISTICS\n")
            f.write("-" * 20 + "\n")
            f.write(f"Total Users: {self.analysis_results['total_users']}\n")
            f.write(f"Total Connections: {self.analysis_results['total_connections']}\n")
            f.write(f"Average Degree: {self.analysis_results['average_degree']:.2f}\n")
            f.write(f"Network Density: {self.analysis_results['network_density']:.3f}\n")
            f.write(f"Connected Components: {self.analysis_results['connected_components']}\n")
            
            if self.analysis_results['average_path_length'] != float('inf'):
                f.write(f"Average Path Length: {self.analysis_results['average_path_length']:.2f}\n")
                f.write(f"Network Diameter: {self.analysis_results['diameter']}\n")
            
            f.write(f"Number of Communities: {self.analysis_results['number_of_communities']}\n")
            f.write(f"Largest Community Size: {self.analysis_results['largest_community_size']}\n")
            f.write(f"Scale-Free Network: {'Yes' if self.analysis_results['is_scale_free'] else 'No'}\n\n")
            
            f.write("CENTRALITY ANALYSIS\n")
            f.write("-" * 20 + "\n")
            most_connected = self.analysis_results['most_connected_user']
            most_central = self.analysis_results['most_central_user']
            most_closeness = self.analysis_results['most_closeness_user']
            
            f.write(f"Most Connected User: {self.users[most_connected[0]]['name']} "
                   f"(Degree Centrality: {most_connected[1]:.3f})\n")
            f.write(f"Most Central User: {self.users[most_central[0]]['name']} "
                   f"(Betweenness Centrality: {most_central[1]:.3f})\n")
            f.write(f"Most Closeness User: {self.users[most_closeness[0]]['name']} "
                   f"(Closeness Centrality: {most_closeness[1]:.3f})\n\n")
            
            f.write("USER DETAILS\n")
            f.write("-" * 20 + "\n")
            for user in self.users:
                degree = self.network.degree(user['id'])
                f.write(f"{user['name']} (Age: {user['age']}, Degree: {degree}, "
                       f"Interests: {', '.join(user['interests'])})\n")
        
        print(f"Analysis report saved as: {filename}")
    
    def run_simulation(self) -> Dict:
        """Run the complete social network simulation."""
        print("Starting Social Network Simulation...")
        print("=" * 40)
        
        # Create users
        print("Creating users...")
        self.create_users()
        
        # Create connections
        print("Creating connections...")
        self.create_connections()
        
        # Analyze network
        print("Analyzing network...")
        analysis = self.analyze_network()
        
        # Visualize network
        print("Creating visualization...")
        self.visualize_network()
        
        # Save analysis report
        print("Saving analysis report...")
        self.save_analysis_report()
        
        # Print summary
        print("\nSimulation Results:")
        print("=" * 40)
        print(f"Total Users: {analysis['total_users']}")
        print(f"Total Connections: {analysis['total_connections']}")
        print(f"Average Degree: {analysis['average_degree']:.2f}")
        print(f"Network Density: {analysis['network_density']:.3f}")
        print(f"Connected Components: {analysis['connected_components']}")
        
        if analysis['average_path_length'] != float('inf'):
            print(f"Average Path Length: {analysis['average_path_length']:.2f}")
        
        print(f"Number of Communities: {analysis['number_of_communities']}")
        print(f"Scale-Free Network: {'Yes' if analysis['is_scale_free'] else 'No'}")
        
        return analysis


def main():
    """Main function to run the social network simulation."""
    print("Social Network Simulation - Week 1 Assignment")
    print("Generative AI & Automation Course")
    print("=" * 50)
    
    # Create and run simulation
    simulation = SocialNetworkSimulation(num_users=20, connection_probability=0.3)
    results = simulation.run_simulation()
    
    print("\nSimulation completed successfully!")
    print("Check the generated files:")
    print("- network_visualization.png (Network graph)")
    print("- network_analysis.txt (Detailed analysis)")


if __name__ == "__main__":
    main() 