# coding: utf-8
"""Script pour tester la classe linkedList.

@author: Ghassan Dabane
"""
from __future__ import absolute_import
import unittest
from linkedList import Node, LinkedList

class LinkedListTest(unittest.TestCase):
    """Test class to try out the 'linked list' module."""

    def setUp(self):
        """Initialize before every test"""
        self.liste = LinkedList()

    def test_one(self):
        """First test: Creating an empty list and verifying if it's really
        empty.
        """
        self.assertTrue(self.liste.is_empty())

    def test_two(self):
        """Second test: Adding an element to an empty list and verifying that
        it's not empty.
        """
        new_node = Node(5)
        self.liste.add_first(new_node)
        self.assertTrue(not self.liste.is_empty())

    def test_three(self):
        """Third test: Adding a node to the list and then deleting it, to
        verify that the list remains unchanged.
        """
        node_1, node_2, node_3 = 5, 6, 99
        self.liste.add_first(Node(node_1))
        self.liste.add_after(node_1, Node(node_2))

        copie = self.liste # créer une copie avant l'insertion

        self.liste.add_after(node_2, Node(node_3)) #ajout
        self.liste.remove_node(node_3) #effacement

        self.assertEqual(self.liste, copie) # fait appel à __eq__

    def test_four(self):
        """Forth test: adding a root node to a list and verifying that it's
        well placed.
        """
        node_data = 3
        new_node = Node(node_data)
        self.liste.add_first(new_node)
        self.assertEqual(self.liste.get(0), node_data)

    def tearDown(self):
        """Call after every test."""
        self.liste = None
