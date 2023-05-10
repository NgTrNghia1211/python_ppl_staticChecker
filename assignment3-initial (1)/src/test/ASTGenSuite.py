import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
#     def test_mixed_decl_variable5(self):
#         inp = """a: float = - a;"""
#         expect = """Program([
# 	VarDecl(a, FloatType, BinExpr(+, BinExpr(+, UnExpr(-, Id(a)), Id(b)), FloatLit(10.0)))
# ])"""
#         self.assertTrue(TestAST.test(inp, expect, 315))

#         # ? with parameters
    def test_full_program(self):
        """Test full program"""
        input = """
                    b: auto = {1, 2, 3, 4, 5};
		a : array[3,2] of integer = {{1, 2}, {3, 4}, {5.5, 6}};
                 """
        expect = "successful"
        self.assertTrue(TestAST.test(input, expect, 500))