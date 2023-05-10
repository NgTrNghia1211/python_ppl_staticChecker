from MT22Visitor import MT22Visitor
from MT22Parser import MT22Parser
from AST import *

# @Student Id: 2013873

class ASTGeneration(MT22Visitor):
    def visitProgram(self, ctx: MT22Parser.ProgramContext):
        return Program([x for x  in self.visit(ctx.decllist())])
    # ? decl - full form vardecl must reverse the expression value
    def visitDecllist(self, ctx: MT22Parser.DecllistContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.decl())
        else: return self.visit(ctx.decl()) + self.visit(ctx.decllist())

    def visitDecl(self, ctx: MT22Parser.DeclContext):
        return self.visit(ctx.vardecl()) if ctx.vardecl() else self.visit(ctx.funcdecl())

    def visitFuncdecl(self, ctx: MT22Parser.FuncdeclContext):
        ide = ctx.IDENTIFIER(0).getText()
        inherit = ctx.IDENTIFIER(1).getText() if ctx.INHERIT() else None
        return_type = self.visit(ctx.return_type())
        params = self.visit(ctx.paramsdecl())
        block_stmt = self.visit(ctx.block_stmt())
        return [FuncDecl(ide, return_type, params, inherit, block_stmt)]

    def visitReturn_type(self, ctx: MT22Parser.Return_typeContext):
        if ctx.AUTO():
            return AutoType()
        elif ctx.VOID():
            return VoidType()
        else: return self.visit(ctx.element_typ())

    def visitParamsdecl(self, ctx: MT22Parser.ParamsdeclContext):
        return self.visit(ctx.paramslist())

    def visitParamslist(self, ctx: MT22Parser.ParamslistContext):
        if ctx.getChildCount() == 0:
            return []
        else: return self.visit(ctx.paramsprime())

    def visitParamsprime(self, ctx: MT22Parser.ParamsprimeContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.param())]
        else: return [self.visit(ctx.param())] + self.visit(ctx.paramsprime())

    def visitParam(self, ctx: MT22Parser.ParamContext):
        inherit = False
        if (ctx.INHERIT()):
            inherit = True
        out = False
        if (ctx.OUT()):
            out = True
        ide = ctx.IDENTIFIER().getText()
        if ctx.AUTO():
            type = AutoType()
            return ParamDecl(ide, type, out, inherit)
        else:
            type = self.visit(ctx.element_typ())
            return ParamDecl(ide, type, out, inherit)


    def visitVardecl(self, ctx: MT22Parser.VardeclContext):
        return self.visit(ctx.shortform_vardecl()) if ctx.shortform_vardecl() else self.visit(ctx.fullform_vardecl())

    def visitShortform_vardecl(self, ctx: MT22Parser.Shortform_vardeclContext):
        if ctx.element_typ():
            ids = self.visit(ctx.idlist())
            x = self.visit(ctx.element_typ())
            return [VarDecl(id, x) for id in ids]
        else:    
            ids = self.visit(ctx.idlist())
            x = AutoType()
            return [VarDecl(id, x) for id in ids]    
        
    def visitIdlist(self, ctx: MT22Parser.IdlistContext):
        if ctx.getChildCount() == 1:
            return [ctx.IDENTIFIER().getText()]
        else: return [ctx.IDENTIFIER().getText()] + self.visit(ctx.idlist())

    def visitFullform_vardecl(self, ctx: MT22Parser.Fullform_vardeclContext):
        listVardecl = self.visit(ctx.prefullform_vardecl())
        for i in range(int(len(listVardecl)/2)):
            temp = listVardecl[i].init
            listVardecl[i].init = listVardecl[len(listVardecl)-1-i].init
            listVardecl[len(listVardecl)-1-i].init = temp
        return listVardecl


    def visitPrefullform_vardecl(self, ctx: MT22Parser.Prefullform_vardeclContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.base_fullform())
        else: 
            t1 = self.visit(ctx.prefullform_vardecl())
            type = t1[0].typ
            return [VarDecl(ctx.IDENTIFIER().getText(), type, self.visit(ctx.expr()))] + self.visit(ctx.prefullform_vardecl())

    def visitBase_fullform(self, ctx: MT22Parser.Base_fullformContext):
        if (ctx.AUTO()):
            id = ctx.IDENTIFIER().getText()
            type = AutoType()
            value = self.visit(ctx.expr())
            return [VarDecl(id, type, value)]
        else:
            id = ctx.IDENTIFIER().getText()
            value = self.visit(ctx.expr())
            type = self.visit(ctx.element_typ())
            return [VarDecl(id, type, value)]
    # ! stmt - only block stmt
    def visitStmt(self, ctx: MT22Parser.StmtContext):
        return self.visit(ctx.getChild(0))
    
    def visitAssg_stmt(self, ctx: MT22Parser.Assg_stmtContext):
        return [AssignStmt(self.visit(ctx.lhs()), self.visit(ctx.expr()))]
    
    def visitLhs(self, ctx: MT22Parser.LhsContext):
        return self.visit(ctx.getChild(0))
    
    def visitScalar_var(self, ctx: MT22Parser.Scalar_varContext):
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        else: return self.visit(ctx.index_expr())
    
    def visitIf_stmt(self, ctx: MT22Parser.If_stmtContext):
        if ctx.ELSE():
            exp = self.visit(ctx.expr())
            tstmt = self.visit(ctx.stmt(0))
            fstmt = self.visit(ctx.stmt(1))
            if (isinstance(tstmt, BlockStmt) == False):
                tstmt = tstmt[0]
            if (isinstance(fstmt, BlockStmt) == False):
                fstmt = fstmt[0]
            return [IfStmt(exp, tstmt, fstmt)]
        exp = self.visit(ctx.expr())
        tstmt = self.visit(ctx.stmt(0))
        if (isinstance(tstmt, BlockStmt)):
            return [IfStmt(exp, tstmt)]
        return [IfStmt(exp, tstmt[0])]
        
    # ! not yet 'for' stmt

    def visitFor_stmt(self, ctx: MT22Parser.For_stmtContext):
        sca_var = self.visit(ctx.scalar_var())
        init = self.visit(ctx.init_expr())
        update = self.visit(ctx.update_expr())
        cond = self.visit(ctx.conditional_expr())
        ass = AssignStmt(sca_var, init)
        stmt = self.visit(ctx.stmt())
        if (isinstance(stmt, BlockStmt) == False):
            stmt = stmt[0]
        return [ForStmt(ass, cond, update, stmt)]
    
    def visitConditional_expr(self, ctx: MT22Parser.Conditional_exprContext):
        return self.visit(ctx.expr())

    def visitUpdate_expr(self, ctx: MT22Parser.Update_exprContext):
        return self.visit(ctx.expr())

    def visitInit_expr(self, ctx: MT22Parser.Init_exprContext):
        return self.visit(ctx.expr())
    
    def visitWhile_stmt(self, ctx: MT22Parser.While_stmtContext):
        exp = self.visit(ctx.expr())
        stmt = self.visit(ctx.stmt())
        if (isinstance(stmt, BlockStmt) == False):
            stmt = stmt[0]
        return [WhileStmt(exp, stmt)]
    
    def visitDo_while_stmt(self, ctx: MT22Parser.Do_while_stmtContext):
        exp = self.visit(ctx.expr())
        return [DoWhileStmt(exp, self.visit(ctx.block_stmt()))]
    
    def visitBreak_stmt(self, ctx: MT22Parser.Break_stmtContext):
        return [BreakStmt()]
    
    def visitContinue_stmt(self, ctx: MT22Parser.Continue_stmtContext):
        return [ContinueStmt()]
    
    def visitReturn_stmt(self, ctx: MT22Parser.Return_stmtContext):
        if (ctx.expr()):
            return [ReturnStmt(self.visit(ctx.expr()))]
        return [ReturnStmt()]
    
    def visitCall_stmt(self, ctx: MT22Parser.Call_stmtContext):
        ide = ctx.IDENTIFIER().getText()
        if (ctx.explist()):
            return [CallStmt(ide, self.visit(ctx.explist()))]
        return [CallStmt(ide, [])]

    def visitBlock_stmt(self, ctx: MT22Parser.Block_stmtContext):
        param = self.visit(ctx.block_stmt_prime_2())
        if type(param) is BlockStmt:
            param = [param]
            return BlockStmt(param)
        return BlockStmt(param)
        
    def visitBlock_stmt_prime_2(self, ctx: MT22Parser.Block_stmt_prime_2Context):
        if ctx.getChildCount() == 0:
            return []
        else: return self.visit(ctx.block_stmt_prime())

    def visitBlock_stmt_prime(self, ctx: MT22Parser.Block_stmt_primeContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.vardecl()) if ctx.vardecl() else self.visit(ctx.stmt())
        else:
            if ctx.vardecl():
                p1 = self.visit(ctx.block_stmt_prime())
                if type(p1) is BlockStmt:
                    p1 = [p1]
                    return self.visit(ctx.vardecl()) + p1
                return self.visit(ctx.vardecl()) + p1
            else:
                p1 = self.visit(ctx.block_stmt_prime())
                p2 = self.visit(ctx.stmt())
                if type(p1) is BlockStmt and type(p2) is BlockStmt:
                    p1 = [p1]
                    p2 = [p2]
                    return p2 + p1
                if type(p2) is BlockStmt:
                    p2 = [p2]
                    return p2 + p1
                if type(p1) is BlockStmt:
                    p1 = [p1]
                    return p2 + p1
                return p2 + p1
                


            # p1 = self.visit(ctx.block_stmt_prime())
            # p2 = self.visit(ctx.stmt())


            # return self.visit(ctx.vardecl()) + self.visit(ctx.block_stmt_prime()) if ctx.vardecl() else self.visit(ctx.stmt()) + self.visit(ctx.block_stmt_prime())


    # ! expr - not func call
    def visitExplist(self, ctx: MT22Parser.ExplistContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        else: return [self.visit(ctx.expr())] + self.visit(ctx.explist())

    def visitExpr(self, ctx: MT22Parser.ExprContext):
        if (ctx.getChildCount() == 3):
            return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        else: return self.visit(ctx.getChild(0))

    def visitRelational_expr(self, ctx: MT22Parser.Relational_exprContext):
        if (ctx.getChildCount() == 3):
            return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        else: return self.visit(ctx.getChild(0))

    def visitLogical_expr(self, ctx: MT22Parser.Logical_exprContext):
        if (ctx.getChildCount() == 3):
            return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        else: return self.visit(ctx.getChild(0))
    
    def visitAdding_expr(self, ctx: MT22Parser.Adding_exprContext):
        if (ctx.getChildCount() == 3):
            return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        else: return self.visit(ctx.getChild(0))

    def visitMultiply_expr(self, ctx: MT22Parser.Multiply_exprContext):
        if (ctx.getChildCount() == 3):
            return BinExpr(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
        else: return self.visit(ctx.getChild(0))

    def visitUlogical_expr(self, ctx: MT22Parser.Ulogical_exprContext):
        if (ctx.getChildCount() == 2):
            return UnExpr(ctx.getChild(0).getText(), self.visit(ctx.getChild(1)))
        else: return self.visit(ctx.getChild(0))

    def visitSign_expr(self, ctx: MT22Parser.Sign_exprContext):
        if (ctx.getChildCount() == 2):
            return UnExpr(ctx.getChild(0).getText(), self.visit(ctx.getChild(1)))
        else: return self.visit(ctx.getChild(0))

    def visitIndex_expr(self, ctx: MT22Parser.Index_exprContext):
        if (ctx.getChildCount() == 1):
            return self.visit(ctx.operands())
        else: return ArrayCell(self.visit(ctx.index_expr()).name, self.visit(ctx.explist()))

    # ! still not enough in operands and func call
    def visitFuncall(self, ctx: MT22Parser.FuncallContext):
        id = ctx.IDENTIFIER().getText()
        li = self.visit(ctx.funcall_list())
        return FuncCall(id, li)

    def visitFuncall_list(self, ctx: MT22Parser.Funcall_listContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.explist())
    
    def visitOperands(self, ctx: MT22Parser.OperandsContext):
        if (ctx.getChildCount() == 3):
            return self.visit(ctx.expr()) # need definition for visitExpr
        else:
            if (ctx.INTLIT()):
                return IntegerLit(int(ctx.INTLIT().getText()))
            elif (ctx.FLOATLIT()):
                return FloatLit(float('0'+ctx.FLOATLIT().getText()))
            elif (ctx.STRINGLIT()):
                return StringLit(ctx.STRINGLIT().getText())
            elif (ctx.boollit()):
                return self.visit(ctx.boollit())
            elif (ctx.IDENTIFIER()):
                return Id(ctx.IDENTIFIER().getText())
            elif (ctx.arraylit()):
                return self.visit(ctx.arraylit())
            else: return self.visit(ctx.funcall())
    # ? type
    # ! array lit not yet
    def visitArraylit(self, ctx: MT22Parser.ArraylitContext):
        if ctx.getChildCount() == 1:
            return ArrayLit(self.visit(ctx.arrayprime()))
        else: return ArrayLit(self.visit(ctx.arrayprime_2()))

    def visitArrayprime_2(self, ctx: MT22Parser.Arrayprime_2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.arrayprime())
        else: return self.visit(ctx.arrayprime()) + self.visit(ctx.arrayprime_2())
    def visitArrayprime(self, ctx: MT22Parser.ArrayprimeContext):
        return self.visit(ctx.explist())

    def visitBoollit(self, ctx: MT22Parser.BoollitContext):
        return BooleanLit(True) if ctx.TRUE() else BooleanLit(False)
    # ? mono type
    def visitElement_typ(self, ctx: MT22Parser.Element_typContext):
        if (ctx.bool_typ()):
            return self.visit(ctx.bool_typ())
        elif (ctx.int_typ()):
            return self.visit(ctx.int_typ())
        elif (ctx.float_typ()):
            return self.visit(ctx.float_typ())
        elif (ctx.string_typ()):
            return self.visit(ctx.string_typ())
        else: return self.visit(ctx.array_typ())

    def visitString_typ(self, ctx: MT22Parser.String_typContext):
        return StringType()
    
    def visitFloat_typ(self, ctx: MT22Parser.Float_typContext):
        return FloatType()
    
    def visitBool_typ(self, ctx: MT22Parser.Bool_typContext):
        return BooleanType() 
    
    def visitInt_typ(self, ctx: MT22Parser.Int_typContext):
        return IntegerType()
    
    def visitVoid_typ(self, ctx: MT22Parser.Void_typContext):
        return VoidType()
    
    def visitAuto_typ(self, ctx: MT22Parser.Auto_typContext):
        return AutoType()
    # ? Array Type
    def visitArray_typ(self, ctx: MT22Parser.Array_typContext):
        return ArrayType(self.visit(ctx.dimension_list()), self.visit(ctx.type_in_array()))
    
    def visitType_in_array(self, ctx: MT22Parser.Type_in_arrayContext):
        if (ctx.bool_typ()):
            return self.visit(ctx.bool_typ())
        elif (ctx.int_typ()):
            return self.visit(ctx.int_typ())
        elif (ctx.float_typ()):
            return self.visit(ctx.float_typ())
        else:
            return self.visit(ctx.string_typ())
        
    def visitDimension_list(self, ctx: MT22Parser.Dimension_listContext):
        return self.visit(ctx.dimension_prime())
    
    def visitDimension_prime(self, ctx: MT22Parser.Dimension_primeContext):
        if ctx.getChildCount() == 1:
            # print([IntegerLit(int(ctx.INTLIT().getText()))])
            return [int(ctx.INTLIT().getText())]
        return [int(ctx.INTLIT().getText())] + self.visit(ctx.dimension_prime())