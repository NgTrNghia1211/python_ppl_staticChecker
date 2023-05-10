import unittest
from TestUtils import TestChecker
from AST import *
from StaticError import *

"""
    TODO: check again + implement:
    * Undeclared (Identifier(), ...) - checked
    * Don't have Undeclared(Function(), ...) - checked
    * No Infer in VarDecl - checked
    * Assign Int to Float can be: in VarDecl, in PassParam, in assign
    > in params, only when call, the infer 
    * No array cell
    * No param auto
    * if function declared after use
    * No inherit
    * forum _ funcall can be return auto???
"""

"""
    TODO: test assign to array cell, inherit ..
"""


class CheckerSuite(unittest.TestCase):
    def test_undeclared_1(self):
        input = """
                    a: integer = 5;
		b: function integer (x: integer) {
			x = a;
			return c;
		}
				main: function void () {}
                """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_undeclared_2(self):
        input = """
                    a1: integer = 5;
		b: function integer (x: integer) {
			c: integer;
			x = 1;
			return a;
		}
				main: function void () {}
                """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_undeclared_3(self):
        input = """
                    a1: integer = 5;
		b: function integer (x: integer) {
			x = 1;
			{
				c: integer = 5;
				{
					return a;
				}
			}
		}
				main: function void () {}
                """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_undeclared_4(self):
        input = """
                    c: function integer (d: boolean) {
			return 9;
		}
		a: integer = 5;
		b: function integer (x: integer) {
			return c(d);
		}
				main: function void () {}
                """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_undeclared_5(self):
        input = """
                    a: integer = 5;
		b: function integer (x: integer) {
			return c(x);
		}
				main: function void () {}
                """
        expect = "Undeclared Function: c"
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_undeclared_6(self):
        input = """
                    c: function integer (d: boolean, e: integer) {
			return 3;
		}
		a: integer = 5;
		b: function integer (x: integer) {
			return c(true, e);
		}
				main: function void () {}
                """
        expect = "Undeclared Identifier: e"
        self.assertTrue(TestChecker.test(input, expect, 405))

    # ? check return raise error
    def test_return_1(self):
        input = """
                    d: boolean = true;
		c: function boolean (d: boolean) {
			return d;
		}
		a: integer = 5;
		b: function integer (x: integer) {
			return c(d);
		}
				main: function void () {}
                """
        expect = "Type mismatch in statement: ReturnStmt(FuncCall(c, [Id(d)]))"
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_return_2(self):
        input = """
                    d: boolean = true;
		c: function auto (d: boolean) {
			return d;
		}
		a: boolean = true;
		b: function boolean (x: integer) {
			return c(a);
		}
		//		main: function void () {}
                """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_flex_1(self):
        input = """
                    a: integer = 1;
		c: function auto (d: float) {
			return d;
		}
	
		main: function void () {
			a = 1 + c(1.0);

		}
		//		main: function void () {}
                """
        expect = "Type mismatch in statement: AssignStmt(Id(a), BinExpr(+, IntegerLit(1), FuncCall(c, [FloatLit(1.0)])))"
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_flex_2(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {}
		a : float;

		main: function void () {
            a = foo(1,2);
		    b : integer = foo (1 , 2) + 1;
		}
		//		main: function void () {}
                """
        expect = "Type mismatch in Variable Declaration: VarDecl(b, IntegerType, BinExpr(+, FuncCall(foo, [IntegerLit(1), IntegerLit(2)]), IntegerLit(1)))"
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_redeclared_1(self):
        input = """
        a: integer = 5;
		b: integer = 6;
		a: integer = 6;
				main: function void () {}
                """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_redeclared_2(self):
        input = """
        fn: function integer (x: integer) {
			return x;
			}
			fn: function integer (x: integer) {
				return x;
				}
		main: function void () {}
                """
        expect = "Redeclared Function: fn"
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_redeclared_3(self):
        input = """
        fn: function void (x: integer) {
			x: integer = 5;
			return;
		}
				main: function void () {}
                """
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_redeclared_4(self):
        input = """
        a: integer = 5;
	 fn: function integer (a: integer) {
		return a;
	 }
                """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_redeclared_5(self):
        input = """
        fn: function void (x: integer, x: boolean) {
			return;
		}
				main: function void () {}
                """
        expect = "Redeclared Parameter: x"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_vardecl_auto_1(self):
        input = """
        a: integer = 5;
		c: array[2] of integer;
		b: auto;
		main: function void () {}
                """
        expect = "Invalid Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_flex_3(self):
        input = """
        a: integer = 5;
		b: function void (i : float) {
			return;
		}
		main: function void () {
			b(7.0);
			b(1.0);
			a(1);
		}
                """
        expect = "Undeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_flex_4(self):
        input = """
        a: float = foo(1, 2) + 1.5;
		foo: function auto(a: integer, b: integer) {
			return a + b;
		}
		b: float = foo(1, 2);
                """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_flex_5(self):
        # print("test 19")
        input = """
        a: float = 5.0;
		b: function auto (i : float) {
			return i;
		}
        main: function void () {
			b(a);
			a(1);
		}
                """
        expect = "Undeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_array_1(self):
        input = """
        main: function void () {
			arr: array[2] of integer;
			arr["0"] = 5;
		}
                """
        expect = "Type mismatch in expression: ArrayCell(arr, [StringLit(0)])"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_array_2(self):
        input = """
        main: function void () {
			arr: array[2,2] of integer;
			arr["0",1] = 5;
		}
                """
        expect = "Type mismatch in expression: ArrayCell(arr, [StringLit(0), IntegerLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_simple_recursion_1(self):
        input = """
        fn: function integer (x: integer) {
			return fn(x);
		}
        main: function void () {
			a(1);
		}
                """
        expect = "Undeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_simple_recursion_2(self):
        input = """
        fn: function integer (x: string) {
			return fn("avc");
		}
        main: function void () {
			a(1);
		}
                """
        expect = "Undeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_flex_6(self):
        input = """
        goo: function boolean(a: boolean) {
            return;
        }
        fn: function integer (x: string) {
            goo(false);
			return fn("avc");
		}
        main: function void () {
			a(1);
		}
                """
        expect = "Undeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_int_float_1(self):
        input = """
        fun: function void () {
            a: float = 1;
        }
        main: function void () {
			a(1);
		}
                """
        expect = "Undeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_int_float_2(self):
        input = """
        t: integer = 1;
        b: float = 2;
        too: function void () {
            a: float = t + b;
            c: float = 3 - 7;
            //d: integer = 1.0;
        }
        main: function void () {
			a(1);
		}
                """
        expect = "Undeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_vardecl_infer_1(self):
        input = """
        foo : function auto ( a : integer , b : integer ) {
            return a + b;
        }
		a : auto = foo(1 , 2);
		//b : integer = foo (1 , 2) + 1;

		man: function void () { foo(1, 2); }
                """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_auto_params(self):
        input = """
        foo: function float (a: auto, b: auto) {
            return;
        }
        mai: function void() {
            c: float = foo("ss", true);
        }
                """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 427))
    def test_para_1(self):
        input = """
        a: integer = 5;
		b: function float (i : float) {
			return 1.0;
		}
		main: function void () {
			b(a);
			b(1);
			a(1);
            }
                """
        expect = "Undeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_para_2(self):
        input = """
        a: integer = 5;
		b: function float (i : auto) {
			return 1.0;
		}
		main: function void () {
			b(1.0);
			b(a);
			a(1);
            }
                """
        expect = "Undeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_para_3(self):
        input = """
        a: integer = 5;
		b: function float (i : auto) {
			return 1.0;
		}
        c: function auto () {
        
        }
		main: function void () {
			b(c());
            }
                """
        expect = "Type mismatch in statement: CallStmt(b, FuncCall(c, []))"
        self.assertTrue(TestChecker.test(input, expect, 430))
    
    def test_int_out_3(self):
        input = """
        a: float = 5;
		mai: function void () {
			a = 7;
            }
                """
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_vardecl_infer_2(self):
        input = """
        boo: function auto () {}
        a: float = boo();
        main: function void () {
			a(1);
		}
                """
        expect = "Undeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 432))

    def test_vardecl_infer_3(self):
        input = """
        boo: function auto () {}
        a: float = boo();
        b: auto = 1 + boo();
        goo: function void() {
            a = b;
            }
        main: function void () {
			a(1);
		}
                """
        expect = "Undeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_int_out_4(self):
        input = """
        a: float = 5;
        goo: function auto () {}
		main: function void () {
			a = goo();
            b: auto = goo();  
            a(1);  
        }
                """
        expect = "Undeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_flex_7(self):
        input = """
        a: integer = 5;
		i: float = 5;
		b: function integer (i : auto) {
			return 12 % (i + 1) + d(5);
		}
		main: function void () {
			b(a);
			b(1);
			a(1);
		}
		d: function integer (i : integer) {
			return i;
		}   
                """
        expect = "Undeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_flex_8(self):
        input = """
        a: integer = 5;
		b: function auto (i : auto) {
			return i;
		}
		main: function void () {
			b(a);
			b(1);
			a(1);
		}
                """
        expect = "Undeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_flex_9(self):
        input = """
        a: integer = 5;
		b: function auto (i : auto) {
			return i;
		}
		main: function void () {
			b(a);
			b(1.0);
		}
                """
        expect = "Type mismatch in statement: CallStmt(b, FloatLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_flex_10(self):
        input = """
        a: integer = 5;
		b: function auto (i : auto) {
			return i;
		}
		main: function void () {
			a = b(a) + 1.5;
		}
                """
        expect = "Type mismatch in statement: AssignStmt(Id(a), BinExpr(+, FuncCall(b, [Id(a)]), FloatLit(1.5)))"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_flex_11(self):
        input = """
        a: integer = 5;
        d: float;
		b: function auto (i : auto) {
			return i;
		}
		main: function void () {
			c: float = b(a) + 1.5;
            d = b(a);
            a(1);
		}
                """
        expect = "Undeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_flex_12(self):
        input = """
            a: float = foo(1, 2) + 1.5;
			foo: function auto(a: integer, b: integer) {
				return a + b;
			}
			b: float = foo(1, 2);
            main: function void() {
                a(1);
            }
                """
        expect = "Undeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_flex_13(self):
        input = """
            a: integer = 5;
		b: function auto (i : float) {
			return i;
		}
		main: function void () {
			//b(a);
			a(1);
		}
                """
        expect = "Undeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_flex_14(self):
        input = """
            main: function void () {
			arr: array[2] of integer;
			arr["0"] = 5;
		}
                """
        expect = "Type mismatch in expression: ArrayCell(arr, [StringLit(0)])"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_flex_15(self):
        input = """
            a: function integer (x: integer, y: integer) {
			return x;
		}
		main: function void () {
			a(4, 2.0);
		}
                """
        expect = "Type mismatch in statement: CallStmt(a, IntegerLit(4), FloatLit(2.0))"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_flex_16(self):
        input = """
            a: integer = 5;
		b: float = 5.0;
		foo: function float (x: float) {
			return x;
		}
		main: function void () {
			b = foo(a);
			a = foo(b);
		}
                """
        expect = "Type mismatch in statement: AssignStmt(Id(a), FuncCall(foo, [Id(b)]))"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_flex_17(self):
        input = """
            a: integer = 5;
		b: float = 5.0;
		foo: function float (x: float) {
			return x;
		}
		main: function void () {
			b = foo(a);
			c = foo(b);
		}
                """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_flex_18(self):
        input = """
            foo: function integer (x: integer) {
			return x;
		}

		bar: function integer (x: boolean) {
			return 1;
		}

		zar: function integer (x: float) {
			return 1;
		}

		a: integer = 5;
		e: integer = 7;
		b: auto = 5;
		d: auto = (a + 16) < (17 + e);
		f: auto = 5 + 1.1 + a;
		main: function void () {
			a = foo(b);

			a = b;

			b = bar(d);

			b = zar(f);

			c = foo(b);
		}
                """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_scope_1(self): 
        input = """
		a: integer = 5;
		foo: function integer (x: integer) {
			b: auto = 5;
			x = 5;
			{
				c: integer = 5;
			}
			{
				c: float = a + 1.1;
			}

			return c;
		}
			main: function void () {}
                """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_scope_2(self):
        input = """
		a: integer = 5;
		foo: function integer (x: integer) {
			b: auto = 5;
			{
				c: integer = 5;
				{
					d: integer = 5;
				}
				c = 6;
				{
					e: integer = 9;
				}
				e  = 10;
			}
			
			return 1;
		}
			main: function void () {}
                """
        expect = "Undeclared Identifier: e"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_scope_3(self):
        input = """
		a: integer = 5;
		foo: function integer (x: integer) {
			b: auto = 5;
			{
				c: integer = 5;
				{
					d: integer = 5;
				}
				c = 6;
				{
					e: integer = 9;
                    // break;
				}
			}
			
			return 1;
		}
		bar : function integer () {
			a = 5;
			
				return a;
			
		}
        main: function void () {
			a(1);
		}
                """
        expect = "Undeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 449))

    # ? next 50 testcases

    def test_stmt_1(self):
        input = """
		a : integer = 5;
		foo: function integer (x: integer) {
			i: integer = 1;
			for (i = 0, (i+11) < (10+11) , i + 1) {
				i = 5;
			}

			return a;
		}
        main: function void () {
			a(1);
		}
                """
        expect = "Undeclared Function: a"
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_stmt_2(self):
        input = """
		a : integer = 5;
		foo: function integer (x: integer) {
			for (i = 0, (i+11) < (10+11) , i + 1) {
				i = 5;
			}

			return a;
		}
        main: function void () {}
                """
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_stmt_3(self):
        input = """
		a : integer = 5;
		foo: function integer (x: integer) {
            i: integer;
			for (i = 0, i + 10, i + 1) {
				a = a + i;
			}

			return a;
		}
		main: function void () {}
                """
        expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(0)), BinExpr(+, Id(i), IntegerLit(10)), BinExpr(+, Id(i), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), Id(i)))]))"
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_stmt_4(self):
        input = """
		a : integer = 5;
		foo: function integer (x: integer) {
            i: integer;
			for (i = 1.0, i < 10, i + 1) {
				a = a + i;
			}

			return a;
		}
		main: function void () {}
                """
        expect = "Type mismatch in statement: AssignStmt(Id(i), FloatLit(1.0))"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_stmt_5(self):
        input = """
		a : integer = 5;
		foo: function integer (x: integer) {
            i: integer;
			for (i = 1, i < 10, i + 1.0) {
				a = a + i;
			}

			return a;
		}
		main: function void () {}
                """
        expect = "Type mismatch in statement: ForStmt(AssignStmt(Id(i), IntegerLit(1)), BinExpr(<, Id(i), IntegerLit(10)), BinExpr(+, Id(i), FloatLit(1.0)), BlockStmt([AssignStmt(Id(a), BinExpr(+, Id(a), Id(i)))]))"
        self.assertTrue(TestChecker.test(input, expect, 454))
    
    def test_stmt_6(self):
        input = """
		a : integer = 5;
		foo: function integer (x: integer) {
			if (a- 10 + 1) {
				a = 10;
			} else {
				a = 5;
			}

			return a;
		}
		main: function void () {}
                """
        expect = "Type mismatch in statement: IfStmt(BinExpr(+, BinExpr(-, Id(a), IntegerLit(10)), IntegerLit(1)), BlockStmt([AssignStmt(Id(a), IntegerLit(10))]), BlockStmt([AssignStmt(Id(a), IntegerLit(5))]))"
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_stmt_7(self):
        input = """
		a : integer = 5;
		foo: function integer (x: integer) {
			if (a < 10) {
				a = 10;
				b : float = 5.5;
			} else {
				a = 5;
				b = 5.5;
			}
			return a;
		}
		main: function void () {}
                """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_stmt_8(self):
        input = """
		a : integer = 5;
		foo: function integer (x: integer) {
			if (a < 10) {
				a = 10;
				c : float = 5.5;
				c = 5.5;
			} else {
				a = 5;
				b : float = 5.5;
			}
			b = 5.5;
			return a;
		}
		main: function void () {}
                """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_stmt_9(self):
        input = """
		a : integer = 5;
		foo: function integer (x: integer) {
			if (a < 10) {
				a = 10;
				c : float = 5.5;
				c = 5.5;
			} else {
				a = 5;
				b : float = 5.5;
			}
			c = 5.5;
			return a;
		}
		main: function void () {}
                """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_stmt_10(self):
        input = """
		a : integer = 5;
		foo: function integer (x: integer) {
			if (a < 10) {
				a = 10;
				c : float = 5.5;
				c = 5.5;
			} else {
				a = 5;
				b : float = 5.5;
			}
			c = 5.5;
			return a;
		}
		main: function void () {}
                """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_stmt_11(self):
        input = """
		a : integer = 5;
		foo: function integer (x: integer) {
			while (a + 10) {
				a = 10;
			}
			return a;
		}
		main: function void () {}
                """
        expect = "Type mismatch in statement: WhileStmt(BinExpr(+, Id(a), IntegerLit(10)), BlockStmt([AssignStmt(Id(a), IntegerLit(10))]))"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_stmt_12(self):
        input = """
		a : integer = 5;
		foo: function integer (x: integer) {
		
			while ((11 > a) && (10 - 1 < 1)) 
				a = 10;
            
			b : float = 5.5;
		    b = 1.1e1;
            c = 3;
			return a;
		}
		main: function void () {}
                """
        expect = "Undeclared Identifier: c"
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_stmt_13(self):
        input = """
		a : integer = 5;
		foo: function integer (x: integer) {
			do {
				a = 10;
			} while (a < 10);

			return a;
		}
		main: function void () {
            d(1);
        }
                """
        expect = "Undeclared Function: d"
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_stmt_14(self):
        input = """
		a : integer = 5;
		foo: function integer (x: integer) {
			do {
				a = 10;
			} while (a < 10);

			return a;
		}
		main: function void () {
            d(1);
        }
                """
        expect = "Undeclared Function: d"
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_stmt_15(self):
        input = """
		a : integer = 5;
		foo: function integer (x: integer) {
		
			do {
				a = 10;
				b : float = 5.5;
			} while (a - 10);

			return a;
		}
		main: function void () {}
                """
        expect = "Type mismatch in statement: DoWhileStmt(BinExpr(-, Id(a), IntegerLit(10)), BlockStmt([AssignStmt(Id(a), IntegerLit(10)), VarDecl(b, FloatType, FloatLit(5.5))]))"
        self.assertTrue(TestChecker.test(input, expect, 464))
    
    def test_stmt_16(self):
        input = """
		a : integer = 5;
		foo: function integer (x: integer) {
			while (a < 10) {
				a = 10;
				break;
			}
            d(1);
			return a;
		}
		main: function void () {}
                """
        expect = "Undeclared Function: d"
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_stmt_17(self):
        input = """
		a : integer = 5;
		foo: function integer (x: integer) {
			while (a < 10) {
				a = 10;
				break;
			}
            d(1);
			return a;
		}
		main: function void () {}
                """
        expect = "Undeclared Function: d"
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_stmt_18(self):
        input = """
		a : integer = 5;
		foo: function integer (x: integer) {
			while (a < 10) {
				a = 10;
			}
			break;
			return a;
		}
		main: function void () {}
                """
        expect = "Must in loop: BreakStmt()"
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_stmt_19(self):
        input = """
		a : integer = 5;
		foo: function integer (x: integer) {
			do  {
				a = 10;
			} while (a < 10);
			continue;
			return a;
		}
		main: function void () {}
                """
        expect = "Must in loop: ContinueStmt()"
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_stmt_20(self):
        input = """
		a : integer = 5;
		foo: function integer (x: integer) {
			do  {
				a = 10;
			    continue;
			} while (a < 10);
			return d;
		}
		main: function void () {}
                """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_stmt_21(self):
        input = """
		a : boolean = false;
		foo: function integer (x: integer) {
			do  {
				a = true;
			    continue;
			} while (!a);
			return d;
		}
		main: function void () {}
                """
        expect = "Undeclared Identifier: d"
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_arraylit_1(self):
        input = """
		b: auto = {1, 2, 3, 4, 5};
		a : array[5] of integer = {1, 2, 3, 4, 5.5};
		
		foo: function integer (x: integer) {
            
			return 1;
		}
		main: function void () {}
                """
        expect = "Illegal array literal: ArrayLit([IntegerLit(1), IntegerLit(2), IntegerLit(3), IntegerLit(4), FloatLit(5.5)])"
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_arraylit_2(self):
        input = """
		b: auto = {1, 2, 3, 4, 5};
		a : array[5] of integer = {1, 2, 3, 4, 5};
		
		foo: function integer (x: integer) {
            a[1] = 2;
            e(1);
		}
		main: function void () {}
                """
        expect = "Undeclared Function: e"
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_arraylit_3(self):
        input = """
		b: auto = {1, 2, 3, 4, 5};
		a : array[5] of integer = {1, 2, 3, 4, 5};
		
		foo: function integer (x: integer) {
            a[1] = "a";
		}
		main: function void () {}
                """
        expect = "Type mismatch in statement: AssignStmt(ArrayCell(a, [IntegerLit(1)]), StringLit(a))"
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_basicUndeclared_Identifier(self):
        input = Program([
	FuncDecl("main", VoidType(), [], None, BlockStmt([VarDecl("a", IntegerType(), IntegerLit(65)), AssignStmt(Id("a"), BinExpr("+", Id("a"), Id("b")))]))
])    
        # expect = """main: function void () {
        #     a: integer = 65; 
        #     a = a + b;
        # }"""
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_arraylit_4(self):
        input = Program([
	VarDecl("a", ArrayType([2, 2], IntegerType()), ArrayLit([ArrayLit([IntegerLit(2), IntegerLit(2)]), ArrayLit([IntegerLit(2), IntegerLit(2)])])),
    FuncDecl("main", VoidType(), [], None, BlockStmt([AssignStmt(Id("a"), BinExpr("+", Id("a"), Id("b")))]))
])    
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_arraylit_5(self):
        input = Program([
	VarDecl("a", ArrayType([2, 3], IntegerType())),
    FuncDecl("main", VoidType(), [], None, BlockStmt([AssignStmt(Id("a"), ArrayLit([ArrayLit([IntegerLit(2), IntegerLit(2)]), ArrayLit([IntegerLit(2), IntegerLit(2)])]))]))
])    
        expect = "Type mismatch in statement: AssignStmt(Id(a), ArrayLit([ArrayLit([IntegerLit(2), IntegerLit(2)]), ArrayLit([IntegerLit(2), IntegerLit(2)])]))"
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_arraylit_6(self):
        input = """
        a: array [2] of integer;
        main: function void () {
            a = {1,2};
            e(1);
        }
                """  
        expect = "Undeclared Function: e" 
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_arraylit_7(self):
        input = Program([
	VarDecl("a", ArrayType([2, 2], IntegerType()), ArrayLit([ArrayLit([IntegerLit(2), IntegerLit(2), IntegerLit(2)]), ArrayLit([IntegerLit(2), IntegerLit(2)])])),
    FuncDecl("main", VoidType(), [], None, BlockStmt([AssignStmt(Id("a"), BinExpr("+", Id("a"), Id("b")))]))
])    
        expect = "Illegal array literal: ArrayLit([ArrayLit([IntegerLit(2), IntegerLit(2), IntegerLit(2)]), ArrayLit([IntegerLit(2), IntegerLit(2)])])"
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_arraylit_8(self):
        input = Program([
	VarDecl("a", ArrayType([2, 2], IntegerType()), ArrayLit([ArrayLit([IntegerLit(2), IntegerLit(2), IntegerLit(2)]), ArrayLit([IntegerLit(2), IntegerLit(2), IntegerLit(2)])])),
    FuncDecl("main", VoidType(), [], None, BlockStmt([AssignStmt(Id("a"), BinExpr("+", Id("a"), Id("b")))]))
])    
        expect = "Type mismatch in Variable Declaration: VarDecl(a, ArrayType([2, 2], IntegerType), ArrayLit([ArrayLit([IntegerLit(2), IntegerLit(2), IntegerLit(2)]), ArrayLit([IntegerLit(2), IntegerLit(2), IntegerLit(2)])]))"
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_all_bin_1(self):
        input = """
                a : integer = 5;
		b : integer = 10;
		c : integer = a + b;
		d : integer = a - b;
		e : integer = a * b;
		f : integer = a / b;
		g : integer = a % b;
		h : boolean = a && b;

		main : function void () {}
                """
        expect = "Type mismatch in expression: BinExpr(&&, Id(a), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_all_bin_2(self):
        input = """
        a : integer = 5;
		b : float = 10.5;
		c : float = a + b;
		d : float = a - b;
		e : float = a * b;
		f : float = a / b;
		g : float = a % b;
		h : boolean = a <= b;

		main : function void () {}
                """
        expect = "Type mismatch in expression: BinExpr(%, Id(a), Id(b))"
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_all_bin_3(self):
        input = """
        b: integer = 5;
        a: integer = 1;
        c: auto = 1 % a;
        e: float = 1;
		main : function void () {
            a = c;
		    h: boolean = a <= e;
            d: boolean = "a" > "b";
        }
                """
        expect = "Type mismatch in expression: BinExpr(>, StringLit(a), StringLit(b))"
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_flex_20(self):
        input = """
        a : array[5] of integer = {1, 2, 3, 4, 5};
		b : integer = a[5];
		c : integer = a[6];
		d : integer = a[0];
		e : integer = a[-1];
		f : integer = a[1.5];
        main : function void () {}
                """
        expect = "Type mismatch in expression: ArrayCell(a, [FloatLit(1.5)])"
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_spec_func_1(self):
        input = """
        foo: function auto () {
	
		}
		bar: function integer () {
			return 1;
		}
		a: boolean = foo() == bar();

		main : function void () {
			readInteger();
			printInteger(1);
			readFloat();
			writeFloat(1.1);
			readBoolean();
			printBoolean(true);
			readString();
			printString("abc");
            printString(b);

		}
                 """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_spec_func_2(self):
        input = """
        x: integer = 65;
		fact : function integer (n : integer) {
			if (n == 0) return 1;
			else return n * fact(n - 1);
		}

		// main : function void () {}
		inc : function void (out n : integer, delta : integer ) {
			n = n + delta ;
		}
		main : function void () {
			delta : integer = fact (3) ;
			inc (x , delta) ;
			printInteger(x) ;
			inc(y, delta) ;
		}
                 """
        expect = "Undeclared Identifier: y"
        self.assertTrue(TestChecker.test(input, expect, 485))
    def test_inherit_1(self):
        input = """
        foo: function auto (a: float, b: string) {
	
		}
		gig: function void () inherit foo{
			super(1, "b");
			d(1);
		}
		main: function void () {
			
		}
                 """
        expect = "Undeclared Function: d"
        self.assertTrue(TestChecker.test(input, expect, 486))
    def test_inherit_2(self):
        input = """
		foo: function auto (a: string, b: string) {
	
		}
		gig: function void () inherit foo{
			a = 1;
			super("a", "b");
			d(1);
		}
		main: function void () {
			
		}
                """
        expect = "Invalid statement in function: gig"
        self.assertTrue(TestChecker.test(input, expect, 487))
    def test_inherit_3(self):
        input = """
        		a: integer = 1;
        foo: function auto (x: integer, f: float) {
	
		}
		gig: function void () inherit foo {
			super(1.0, 2);
			
		}
		main: function void () {
			
		}
                """
        expect = "Type mismatch in statement: CallStmt(super, FloatLit(1.0), IntegerLit(2))"
        self.assertTrue(TestChecker.test(input, expect, 488))
    def test_inherit_4(self):
        input = """
        		a: integer = 1;
        foo: function auto () {
	
		}
		gig: function void () inherit foo {
			a = 1;
			d(1);
		}
		main: function void () {
			
		}
                """
        expect = "Undeclared Function: d"
        self.assertTrue(TestChecker.test(input, expect, 489))
    def test_flex_21(self):
        input = """
				foo: function void () {}
                too: function void () {}
                foo: function integer () {}
                main: function void () {}
        		"""
        expect = "Redeclared Function: foo"
        self.assertTrue(TestChecker.test(input, expect, 490))
    def test_flex_22(self):
        input = """
				a: integer = 123;
                main: function void () {
					a: string = a;
				}
        		"""
        expect = "Type mismatch in Variable Declaration: VarDecl(a, StringType, Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 491))
    def test_flex_23(self):
        input = """
				a: integer = 123;
                b: integer = a;
                a: boolean;
                main: function void () {
					a: string = a;
				}
        		"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 492))
    def test_flex_25(self):
        input = """
				a: integer = 123;
                b: integer = a;
                a: boolean;
                main: function void () {
					a: string = a;
				}
        		"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 493))
    def test_flex_24(self):
        input = """
				a: integer = 123;
                b: integer = a;
                a: boolean;
                main: function void () {
					a: string = a;
				}
        		"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 494))
    def test_flex_26(self):
        input = """
				a: integer = 123;
                b: integer = a;
                a: boolean;
                main: function void () {
					a: string = a;
				}
        		"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 495))
    def test_flex_27(self):
        input = """
				a: integer = 123;
                b: integer = a;
                a: boolean;
                main: function void () {
					a: string = a;
				}
        		"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 496))    
    def test_flex_29(self):
        input = """
				a: integer = 123;
                b: integer = a;
                a: boolean;
                main: function void () {
					a: string = a;
				}
        		"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 497))
    def test_flex_28(self):
        input = """
				a: integer = 123;
                b: integer = a;
                a: boolean;
                main: function void () {
					a: string = a;
				}
        		"""
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 498)) 
    def test_flex_30(self):
        input = """
				a: integer = 123;
                b: integer = a;
                mai: function void () {
					
				}
        		"""
        expect = "No entry point"
        self.assertTrue(TestChecker.test(input, expect, 499))           
	
	
#     def test_inherit_2(self):
# 		input = """
        
# """
# 	# 	expect = "Invalid statement in function: gig"
# 	# 	self.assertTrue(TestChecker.test(input, expect, 487))


    # # flex: next = 20
	# def test_inherit_1(self):
	# 	input = """
    #     foo: function auto (a: float, b: string) {
	
	# 	}
	# 	gig: function void () inherit foo{
	# 		super(1, "b");
	# 		d(1);
	# 	}
	# 	main: function void () {
			
	# 	}
    #              """
	# 	expect = "Undeclared Function: d"
	# 	self.assertTrue(TestChecker.test(input, expect, 486))

	

	# def test_inherit_3(self):
	# 	input = """
		
    #              """
	# 	expect = "Undeclared Function: d"
	# 	self.assertTrue(TestChecker.test(input, expect, 488))


	# def test_inherit_4(self):
	# 	input = """
	# 	a: integer = 1;
    #     foo: function auto (x: integer, f: float) {
	
	# 	}
	# 	gig: function void () inherit foo {
	# 		super(1.0, 2);
			
	# 	}
	# 	main: function void () {
			
	# 	}
    #              """
	# 	expect = "Type mismatch in statement: CallStmt(super, FloatLit(1.0), IntegerLit(2))"
		# self.assertTrue(TestChecker.test(input, expect, 489))
	
	# def test_full_program(self):
	# 	input = """
    #     foo: function auto (a: string, b: string) {
	
	# 	}
	# 	bar: function integer () {
	# 		return 1;
	# 	}

    #     too: function integer (a: string, b: float) {
        
	# 	}
	# 	main : function void () inherit bar {
	# 		//super("true", 1.0);
    #         preventDefault();
    #         foo("ab", "nc");
	# 	}
    #              """
	# 	expect = "successful"
	# 	self.assertTrue(TestChecker.test(input, expect, 500))
        
