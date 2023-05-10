"""
* Student ID: 2013873
"""  
from AST import *
from StaticError import *
from Utils import *
from Visitor import Visitor


# ? Error messages
# NoEntryPoint
# TypeMisMatchInExpression
# TypeMisMatchInVarDecl
# TypeMisMatchInStatement
# Redeclared
# Undeclared
# Invalid

# ? Plan
# a first [] contains prototype "only" functions
# a second [] contains global declarations: functions and decl

# ? Utility class
class Symbol:
    def __init__(self, name, type, kind, parent = None, value = None, local = None, params = None):
        self.name = name # ID
        self.type = type # Type, Return type
        self.kind = kind # Kind: Function, Variable, Params
        self.parent = parent # ID
        self.value = value
        self.local = local # Env of a function
        self.params = params

    def __str__(self) -> str:
        # print("Params({})".format(", ".join([str(expr) for expr in self.params])))
        return f"Name: {self.name}, Type: {self.type}, Kind: {self.kind}, Parent: {self.parent}"

class GetEnv(Visitor):
    """after visit a function: [Symbol(ast.name, ast.return_type, Function, ast.inherit, None, local[0], ast.params)]"""
    def __init__(self, ast):
        self.nothing = ast

    """
        Symbol("readInteger", IntegerType(), Function, None, None, [], []),
             Symbol("printInteger", VoidType(), Function, None, None, [], [ParamDecl('anArg', IntegerType())]),
             Symbol("readFloat", FloatType(), Function, None, None, [], []),
             Symbol("writeFloat", VoidType(), Function, None, None, [], [ParamDecl('anArg', FloatType())]),
             Symbol("readBoolean", BooleanType(), Function, None, None, [], []),
             Symbol("printBoolean", VoidType(), Function, None, None, [], [ParamDecl('anArg', BooleanType())]),
             Symbol("readString", StringType(), Function, None, None, [], []),
             Symbol("printString", BooleanType(), Function, None, None, [], [ParamDecl('anArg', StringType())]),
    """
    def visitProgram(self, ast: Program, o):
        o = [Symbol("readInteger", IntegerType(), Function, None, None, [], []),
             Symbol("printInteger", VoidType(), Function, None, None, [], [ParamDecl('anArg', IntegerType())]),
             Symbol("readFloat", FloatType(), Function, None, None, [], []),
             Symbol("writeFloat", VoidType(), Function, None, None, [], [ParamDecl('anArg', FloatType())]),
             Symbol("readBoolean", BooleanType(), Function, None, None, [], []),
             Symbol("printBoolean", VoidType(), Function, None, None, [], [ParamDecl('anArg', BooleanType())]),
             Symbol("readString", StringType(), Function, None, None, [], []),
             Symbol("printString", BooleanType(), Function, None, None, [], [ParamDecl('anArg', StringType())]),
             Symbol("preventDefault", VoidType(), Function, None, None, [], []),
             Symbol("super", VoidType(), Function, None, None, [], [])]
        # o = []
        for decl in ast.decls:
            self.visit(decl, o)
        return o

    def visitFuncDecl(self, ast: FuncDecl, o): 
        # print(ast.params)
        o += [Symbol(ast.name, ast.return_type, Function, ast.inherit, None, None, ast.params)]
        return o

    def visitVarDecl(self, ast: VarDecl, o): 
        pass

class Loop:
    pass
class Scope:
    pass

# ? Static Checker
class StaticChecker(Visitor):
    def __init__(self, ast):
        self.ast = ast
        # self.ob = []

    def check(self):
        return self.visit(self.ast, [])
    
    def visitIntegerType(self, ctx: IntegerType, o): return IntegerType()
    def visitFloatType(self, ctx: FloatType, o): return FloatType()
    def visitBooleanType(self, ctx: BooleanType, o): return BooleanType()
    def visitStringType(self, ctx: StringType, o): return StringType()
    def visitAutoType(self, ctx, o): return AutoType()
    def visitVoidType(self, ctx, o): return VoidType()
    def visitArrayType(self, ctx, o): pass

    # * op: str, left: Expr, right: Expr
    # * case:
    def visitBinExpr(self, ast: BinExpr, o): 
        left = self.visit(ast.left, o)
        right = self.visit(ast.right, o)
        op = ast.op
        # print(left)
        # print(right)
        if op in ['+', '-', '*', '/']:
            if type(left) in [AutoType, VoidType] and type(right) in [AutoType, VoidType]:
                raise TypeMismatchInExpression(ast)
            
            if type(left) in [AutoType, VoidType]:
                if type(right) not in [IntegerType, FloatType]:
                    raise TypeMismatchInExpression(ast)
                for symbol_list in o:
                    for symbol in symbol_list:
                        if symbol.name == ast.left.name:
                            symbol.type = right
                            # print(symbol)
                            if type(right) is IntegerType:
                                return IntegerType()
                            return FloatType()
            

            if type(right) in [AutoType, VoidType]:
                if type(left) not in [IntegerType, FloatType]:
                    raise TypeMismatchInExpression(ast)
                for symbol_list in o:
                    for symbol in symbol_list:
                        if symbol.name == ast.right.name:
                            symbol.type = left
                            if type(left) is IntegerType:
                                return IntegerType()
                            return FloatType()
            

            if type(left) not in [FloatType, IntegerType] or type(right) not in [FloatType, IntegerType]:
                raise TypeMismatchInExpression(ast)
            if type(left) is IntegerType and type(right) is IntegerType:
                return IntegerType()
            if type(left) is FloatType or type(right) is FloatType:
                return FloatType()

        if op in ['%']:
            if type(left) in [AutoType, VoidType] and type(right) in [AutoType, VoidType]:
                raise TypeMismatchInExpression(ast)
            
            if type(left) in [AutoType, VoidType]:
                if type(right) not in [IntegerType]:
                    raise TypeMismatchInExpression(ast)
                for symbol_list in o:
                    for symbol in symbol_list:
                        if symbol.name == ast.left.name:
                            symbol.type = right
                            # print(symbol)
                            return IntegerType()
            if type(right) in [AutoType, VoidType]:
                if type(left) not in [IntegerType]:
                    raise TypeMismatchInExpression(ast)
                for symbol_list in o:
                    for symbol in symbol_list:
                        if symbol.name == ast.right.name:
                            symbol.type = left
                            return IntegerType()
            if type(left) not in [IntegerType] or type(right) not in [IntegerType]:
                raise TypeMismatchInExpression(ast)
            return IntegerType()                

        if op in ['||', '&&']:
            if type(left) in [AutoType, VoidType] and type(right) in [AutoType, VoidType]:
                raise TypeMismatchInExpression(ast)
            
            if type(left) in [AutoType, VoidType]:
                if type(right) not in [BooleanType]:
                    raise TypeMismatchInExpression(ast)
                for symbol_list in o:
                    for symbol in symbol_list:
                        if symbol.name == ast.left.name:
                            symbol.type = right
                            return BooleanType()
            
            if type(right) in [AutoType, VoidType]:
                if type(left) not in [BooleanType]:
                    raise TypeMismatchInExpression(ast)
                for symbol_list in o:
                    for symbol in symbol_list:
                        if symbol.name == ast.right.name:
                            symbol.type = left
                            return BooleanType()


            if type(left) is BooleanType and type(right) is BooleanType:
                return BooleanType()
            else :
                raise TypeMismatchInExpression(ast)
        
        if op in ['::']:
            if type(left) in [AutoType, VoidType] and type(right) in [AutoType, VoidType]:
                raise TypeMismatchInExpression(ast)
            
            if type(left) in [AutoType, VoidType]:
                if type(right) not in [StringType]:
                    raise TypeMismatchInExpression(ast)
                for symbol_list in o:
                    for symbol in symbol_list:
                        if symbol.name == ast.left.name:
                            symbol.type = right
                            return StringType()
            
            if type(right) in [AutoType, VoidType]:
                if type(left) not in [StringType]:
                    raise TypeMismatchInExpression(ast)
                for symbol_list in o:
                    for symbol in symbol_list:
                        if symbol.name == ast.right.name:
                            symbol.type = left
                            return StringType()

            if type(left) is StringType and type(right) is StringType:
                return StringType()
            else: 
                raise TypeMismatchInExpression(ast)
            
        if op in ['==', '!=', '>=', '<=', '>', '<']:
            if type(left) in [AutoType, VoidType] and type(right) in [AutoType, VoidType]:
                raise TypeMismatchInExpression(ast)

            if type(left) in [AutoType, VoidType]:
                if type(right) not in [FloatType, IntegerType]:
                    raise TypeMismatchInExpression(ast)
                for symbol_list in o:
                    for symbol in symbol_list:
                        if symbol.name == ast.left.name:
                            symbol.type = right
                            return BooleanType()
            
            if type(right) in [AutoType, VoidType]:
                if type(left) not in [FloatType, IntegerType]:
                    raise TypeMismatchInExpression(ast)
                for symbol_list in o:
                    for symbol in symbol_list:
                        if symbol.name == ast.right.name:
                            symbol.type = left
                            return BooleanType()


            if type(left) in [IntegerType, FloatType] and type(right) in [IntegerType, FloatType]:
                return BooleanType()
            else:
                raise TypeMismatchInExpression(ast)

    # * op: str, val: Expr
    def visitUnExpr(self, ast: UnExpr, o): 
        e = self.visit(ast.val, o)
        op = ast.op

        if op in ['-']:
            if type(e) in [VoidType, AutoType]:
                for symbol_list in o:
                    for symbol in symbol_list:
                        if symbol.name == ast.val.name:
                            symbol.type = FloatType()
                            return FloatType()

            if type(e) is IntegerType or type(e) is FloatType:
                return e
            else: 
                raise TypeMismatchInExpression(ast)
            
        if op in ['!']:
            if type(e) in [VoidType, AutoType]:
                for symbol_list in o:
                    for symbol in symbol_list:
                        if symbol.name == ast.val.name:
                            symbol.type = BooleanType()
                            return BooleanType()

            if type(e) is BooleanType:
                return BooleanType()
            else: 
                raise TypeMismatchInExpression(ast)
            
    # * name: str
    def visitId(self, ast:Id, o): 
        for list_symbol in o:
            for symbol in list_symbol:
                # print(symbol.name)
                if ast.name == symbol.name and symbol.kind != Function:
                    return symbol.type
        raise Undeclared(Identifier(), ast.name)
    
    # * name: str, cell: List[Expr]
    # * check [name] type is array
    # * check visit expr -> type, if not integer -> raise
    # * ArrayType(List[Int], typ)
    def visitArrayCell(self, ast: ArrayCell, o): 
        for exp in ast.cell:
            typ =  self.visit(exp, o)
            if type(typ) is not IntegerType:
                raise TypeMismatchInExpression(ast)
        for symbol_list in o:
            for symbol in symbol_list:
                if symbol.name == ast.name:
                    # print(symbol.type.typ)
                    return symbol.type.typ

        return AutoType()

    def visitIntegerLit(self, ast, o): return IntegerType()
    def visitFloatLit(self, ast, o): return FloatType()
    def visitStringLit(self, ast, o): return StringType()
    def visitBooleanLit(self, ast, o): return BooleanType()

    # * explist: List[Expr]
    def visitArrayLit(self, ast: ArrayLit, o): 
        pre_typ = AutoType()
        temp = 1
        pre_temp = 1
        first_check = False
        for exp in ast.explist:
            typ =  self.visit(exp, o)
            # print(typ)
            # print(pre_typ)
            if type(typ) is not AutoType and type(typ) is not VoidType:
                if type(pre_typ) is not AutoType and type(pre_typ) is not type(typ):
                    raise IllegalArrayLiteral(ast)
                if type(typ) is ArrayType:
                    temp = self.visit(exp, o)
                    if first_check == True:
                        if (temp != pre_temp):
                            raise IllegalArrayLiteral(ast)
                    if first_check == False:
                        pre_temp = temp
                        first_check = True
                pre_typ = typ
            else:
                if type(pre_typ) is not None:
                    for symbol_list in o:
                        for symbol in symbol_list:
                            if symbol.name == exp.name:
                                symbol.type = pre_typ
                # print(1)
        if type(pre_typ) is not AutoType:
            # example: ArrayType([2], IntegerType)
            if type(temp) is ArrayType:
                # print(temp)
                return ArrayType([len(ast.explist),temp.dimensions[0]], pre_typ.typ)
            return ArrayType([len(ast.explist)], pre_typ)
        return AutoType()

        # return ArrayType()
    # * name: str, args: List[Expr]
    def visitFuncCall(self, ast: FuncCall, o):
        for symbol_list in o:
            for symbol in symbol_list:
                if ast.name == symbol.name and symbol.kind == Function and type(symbol.type) is not VoidType:
                    # ? Must Implement - check params
                    # print(ast.args)
                    # print(symbol)
                    if len(ast.args) != len(symbol.params):
                        raise TypeMismatchInStatement(ast)
                    idx = 0
                    for arg in ast.args:
                        typ = self.visit(arg, o)
                        if type(symbol.params[idx].typ) is FloatType and type(typ) is IntegerType:
                            typ = symbol.params[idx].typ
                        if type(symbol.params[idx].typ) is AutoType and type(typ) is AutoType:
                            raise TypeMismatchInStatement(ast)
                        if type(symbol.params[idx].typ) is AutoType:
                            symbol.params[idx].typ = typ
                        if type(typ) is not type(symbol.params[idx].typ):
                            raise TypeMismatchInStatement(ast)
                        idx += 1
                        # print(type(symbol.params[0].typ))
                        # print(type(typ) is type(symbol.params[0].typ))
                    return symbol.type
        raise Undeclared(Function(), ast.name)

    # * lhs: LHS, rhs: Expr
    # * infer only when the rhs is a void function
    def visitAssignStmt(self, ast:AssignStmt, o):
        lhs = self.visit(ast.lhs, o)
        rhs = self.visit(ast.rhs, o)
        # print(lhs)
        # print(rhs)
        if type(rhs) is AutoType:
            for symbol_list in o:
                for symbol in symbol_list:
                    if symbol.name == ast.rhs.name:
                        symbol.type = lhs
                        return lhs
        if type(rhs) is ArrayType and type(lhs) is ArrayType:
            if lhs != rhs:
                raise TypeMismatchInStatement(ast)
            return lhs
        if type(lhs) is FloatType and type(rhs) is IntegerType:
            return lhs
        if type(lhs) is type(rhs):
            return lhs# must be return type
        raise TypeMismatchInStatement(ast)
    
    # * body: List[Stmt or VarDecl]
    def visitBlockStmt(self, ast: BlockStmt, o): 
        typ = None
        first_stmt = False
        spec = False
        # for symbol_list in o:
        #     for symbol in symbol_list:
        #         print(symbol)
        #     print("end a scope")
        # print("end large scope")
        for decl in ast.body:
            if first_stmt == False:
                if o[0][0].parent != None:
                    for sy in o[len(o)-1]:
                        if sy.name == o[0][0].parent:
                            if len(sy.params) <= 0:
                                spec = True

                    if spec == False:
                        if type(decl) is not CallStmt:
                            raise InvalidStatementInFunction(o[0][0].name)
                        if decl.name != "super" and decl.name != "preventDefault":
                            raise InvalidStatementInFunction(o[0][0].name)
                    self.visit(decl, o)
                else:
                    if type(decl) is VarDecl:
                        o = self.visit(decl, o)
                    elif type(decl) is ReturnStmt:
                        typ = self.visit(decl, o)
                    elif type(decl) is BlockStmt:
                        new_ev =[[Symbol(None, None, Stmt)]]
                        new_ev = new_ev + o
                        self.visit(decl, new_ev)
                    else:
                        self.visit(decl, o)
                first_stmt = True
            else:
                if type(decl) is VarDecl:
                    o = self.visit(decl, o)
                elif type(decl) is ReturnStmt:
                    typ = self.visit(decl, o)
                elif type(decl) is BlockStmt:
                    new_ev =[[Symbol(None, None, Stmt)]]
                    new_ev = new_ev + o
                    self.visit(decl, new_ev)
                else:
                    self.visit(decl, o)
        return typ


    # * cond: Expr, tstmt: Stmt, fstmt: Stmt or None = None
    def visitIfStmt(self, ast: IfStmt, o): 
        typ = self.visit(ast.cond, o)
        if type(typ) is not BooleanType:
            # raise TypeMismatchInExpression(ast.cond)
            raise TypeMismatchInStatement(ast)
        if type(ast.tstmt) is BlockStmt:
            new_ev = [[Symbol(None, None, Stmt)]]
            new_ev = new_ev + o
            self.visit(ast.tstmt, new_ev)
        else:
            self.visit(ast.tstmt, o)

        if ast.fstmt:
            if type(ast.fstmt) is BlockStmt:
                new_ev = [[Symbol(None, None, Stmt)]]
                new_ev = new_ev + o
                self.visit(ast.fstmt, new_ev)
            else:
                self.visit(ast.fstmt, o)

    # * init: AssignStmt, cond: Expr, upd: Expr, stmt: Stmt
    def visitForStmt(self, ast: ForStmt, o): 
        typ_init = self.visit(ast.init, o)
        if type(typ_init) is not IntegerType:
            # print("go here")
            raise TypeMismatchInStatement(ast)
        
        typ_upd = self.visit(ast.upd, o)
        if type(typ_upd) is not IntegerType:
            # print("go here 1")
            raise TypeMismatchInStatement(ast)
        
        typ_cond = self.visit(ast.cond, o)
        if type(typ_cond) is not BooleanType:
            # print("go here 2")
            raise TypeMismatchInStatement(ast)
        
        if type(ast.stmt) is BlockStmt:
            new_ev = [[Symbol(None, None, Loop)]] + o
            self.visit(ast.stmt, new_ev)
        else:
            self.visit(ast.stmt, o)


    # * cond: Expr, stmt: Stmt
    def visitWhileStmt(self, ast: WhileStmt, o): 
        typ = self.visit(ast.cond, o)
        if type(typ) is not BooleanType:
            raise TypeMismatchInStatement(ast)
        if type(ast.stmt) is BlockStmt:
            new_ev = [[Symbol(None, None, Loop)]] + o
            self.visit(ast.stmt, new_ev)
        else:
            self.visit(ast.stmt, o)
        
    # * cond: Expr, stmt: BlockStmt
    def visitDoWhileStmt(self, ast: DoWhileStmt, o): 
        typ =  self.visit(ast.cond, o)
        if type(typ) is not BooleanType:
            raise TypeMismatchInStatement(ast)

        new_ev = [[Symbol(None, None, Loop)]] + o
        self.visit(ast.stmt, new_ev)
        

    def visitBreakStmt(self, ast: BreakStmt, o): 
        flag = False
        for i in range(0, len(o)):
            if (o[i][0].kind == Loop):
                flag = True
        # print(flag)
        if flag == False:
            raise MustInLoop(ast)
        
    def visitContinueStmt(self, ast, o): 
        flag = False
        for i in range(0, len(o)):
            if (o[i][0].kind == Loop):
                flag = True
        # print(flag)
        if flag == False:
            raise MustInLoop(ast)

    # * expr: Expr or None = None
    def visitReturnStmt(self, ast: ReturnStmt, o): 
        if ast.expr:
            typ = self.visit(ast.expr, o)
            # print(type(typ))
            # print(type(o[0][0].type))
            if type(typ) is IntegerType and type(o[0][0].type) is FloatType:
                return FloatType()
            if type(typ) is not type(o[0][0].type) and type(o[0][0].type) is not AutoType:
                raise TypeMismatchInStatement(ast)
            return typ
        return None
    
    # * name: str, args: List[Expr] # must be VoidType
    def visitCallStmt(self, ast: CallStmt, o): 
        flag = False
        for symbol_list in o:
            for symbol in symbol_list:
                if ast.name == symbol.name and symbol.kind == Function:
                    # ? Implement check if super()
                    # print(ast.args)
                    if ast.name  == "super":
                        # print(o[0][0].parent)
                        idx = 0
                        for sym in symbol_list:
                            if sym.name == o[0][0].parent:
                            # print(symbol.params)
                                for arg in ast.args:
                                    typ = self.visit(arg, o)
                                    if type(sym.params[idx].typ) is FloatType and type(typ) is IntegerType:
                                        typ = sym.params[idx].typ
                                    if type(sym.params[idx].typ) is AutoType and type(typ) is AutoType:
                                        raise TypeMismatchInStatement(ast)
                                    if type(sym.params[idx].typ) is AutoType:
                                        sym.params[idx].typ = typ
                                    if type(typ) is not type(sym.params[idx].typ):
                                        raise TypeMismatchInStatement(ast)
                                    idx += 1
                        return
                    else:
                    # ? Must Implement - check params
                        if len(ast.args) != len(symbol.params):
                            raise TypeMismatchInStatement(ast)
                        idx = 0
                        for arg in ast.args:
                            typ = self.visit(arg, o)
                            if type(symbol.params[idx].typ) is FloatType and type(typ) is IntegerType:
                                typ = symbol.params[idx].typ
                            if type(symbol.params[idx].typ) is AutoType and type(typ) is AutoType:
                                raise TypeMismatchInStatement(ast)
                            if type(symbol.params[idx].typ) is AutoType:
                                symbol.params[idx].typ = typ
                            if type(typ) is not type(symbol.params[idx].typ):
                                raise TypeMismatchInStatement(ast)
                            idx += 1
                            # print(type(symbol.params[0].typ))
                            # print(type(typ) is type(symbol.params[0].typ))
                        return
        raise Undeclared(Function(), ast.name)        

    # * name: string, typ: Type, init: Expr/None
    def visitVarDecl(self, ast: VarDecl, o): 
        if type(ast.typ) is AutoType:
            if not ast.init:
                raise Invalid(Variable(), ast.name)
            

        typ = None
        if ast.init:
            typ = self.visit(ast.init, o)
            # print(type(typ))
            # print(type(ast.typ))
            if type(typ) is IntegerType and type(ast.typ) is FloatType:
                typ = ast.typ
            if type(typ) is AutoType and type(ast.typ) is AutoType:
                raise TypeMismatchInVarDecl(ast)
            if type(ast.typ) is AutoType:
                ast.typ = typ
            if type(typ) is AutoType:
                for symbol_list in o:
                    for symbol in symbol_list:
                        if symbol.name == ast.init.name:
                            # print("here")
                            symbol.type = ast.typ
                            typ = ast.typ
            if type(typ) is ArrayType:
                if typ != ast.typ:
                    raise TypeMismatchInVarDecl(ast)
                
            # print(typ)
            # print(ast.typ)
            if type(typ) is not type(ast.typ):
                
                raise TypeMismatchInVarDecl(ast)
            
        for symbol in o[0]:
            if ast.name == symbol.name:
                raise Redeclared(Variable(), ast.name)
        
        o[0] += [Symbol(ast.name, ast.typ, Variable)]
        return o
    
    # * name: string, typ: Type, out: bool, inherit: bool
    def visitParamDecl(self, ast, o):
        for symbol in o:
            if ast.name == symbol.name:
                raise Redeclared(Parameter(), ast.name)
        
        o += [Symbol(ast.name, ast.typ, Parameter)]    
        return o
    
    # * name: string, return_type: Type, params: List[ParamDecl], inherit: string/None, 
    # * body: BlockStmt
    def visitFuncDecl(self, ast: FuncDecl, o): 
        # ? checking Redeclare Function
        for symbol in o[0]:
            if ast.name == symbol.name:
                raise Redeclared(Function(), ast.name)
        for symbol in o[1]:
            if ast.name == symbol.name:
                # print("access here")
                ast.return_type = symbol.type

        # ? get params
        local = [Symbol(ast.name, ast.return_type, Function, ast.inherit, None, None, ast.params)]
        for param in ast.params:
            local = self.visit(param, local) # ? list of params
        local = [local] + o

        if ast.inherit:
            isParent = False
            for symbol_list in o:
                for symbol in symbol_list:
                    if ast.inherit == symbol.name and symbol.kind == Function:
                        isParent = True
                        break
            if isParent == False:
                # print("here is not")
                raise Undeclared(Function(), ast.inherit)

        typ = self.visit(ast.body, local)
        if type(ast.return_type) is AutoType:
            if type(typ) is not type(None):
                ast.return_type = typ
        elif (type(typ) is not type(None) and type(typ) is not type(ast.return_type)):
            raise TypeMismatchInVarDecl(ast)
        
        # for symbol in local[0]:
        #     print(symbol)
        # print("end of function")
        # ? Maybe need a steps to change local in global scope
        o[0] += [Symbol(ast.name, ast.return_type, Function, ast.inherit, None, local[0], ast.params)]
        

    # * decls: List[Decl] (VarDecl, FuncDecl)
    def visitProgram(self, ast: Program, o): # o = [[Symbol Global]]
        # env = GetEnv(ast).visit(ast, o) # ? return list of FuncDecl in global
        env = GetEnv(ast).visit(ast, o) # ? return list of FuncDecl in global
        entry_flag = False
        # for symbol in env:
        #     # print(symbol)
        #     if symbol.name == "main" and type(symbol.type) is VoidType:
        #         entry_flag = True
        # if entry_flag == False:
        #     raise NoEntryPoint()

        ev = [[]] + [env]
        for decl in ast.decls:
            self.visit(decl, ev)

        for symbol in env:
            if symbol.name == "main" and type(symbol.type) is VoidType:
                entry_flag = True
        if entry_flag == False:
            raise NoEntryPoint()

        # print('Defined Function:')    
        # for symbol in ev[1]:
        #     print(symbol)
        # for symbol in ev[0]:
        #     print(symbol)   
        #     if symbol.name == 'main':
        #         entry_flag = True
        # if entry_flag == False:
        #     raise NoEntryPoint()
        
