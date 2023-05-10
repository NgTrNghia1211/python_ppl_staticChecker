# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decllist.
    def visitDecllist(self, ctx:MT22Parser.DecllistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decl.
    def visitDecl(self, ctx:MT22Parser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#vardecl.
    def visitVardecl(self, ctx:MT22Parser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#shortform_vardecl.
    def visitShortform_vardecl(self, ctx:MT22Parser.Shortform_vardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#fullform_vardecl.
    def visitFullform_vardecl(self, ctx:MT22Parser.Fullform_vardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#prefullform_vardecl.
    def visitPrefullform_vardecl(self, ctx:MT22Parser.Prefullform_vardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#base_fullform.
    def visitBase_fullform(self, ctx:MT22Parser.Base_fullformContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#idlist.
    def visitIdlist(self, ctx:MT22Parser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#explist.
    def visitExplist(self, ctx:MT22Parser.ExplistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#param.
    def visitParam(self, ctx:MT22Parser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paramsdecl.
    def visitParamsdecl(self, ctx:MT22Parser.ParamsdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcdecl.
    def visitFuncdecl(self, ctx:MT22Parser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paramslist.
    def visitParamslist(self, ctx:MT22Parser.ParamslistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#paramsprime.
    def visitParamsprime(self, ctx:MT22Parser.ParamsprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_type.
    def visitReturn_type(self, ctx:MT22Parser.Return_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expr.
    def visitExpr(self, ctx:MT22Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#relational_expr.
    def visitRelational_expr(self, ctx:MT22Parser.Relational_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#logical_expr.
    def visitLogical_expr(self, ctx:MT22Parser.Logical_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#adding_expr.
    def visitAdding_expr(self, ctx:MT22Parser.Adding_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#multiply_expr.
    def visitMultiply_expr(self, ctx:MT22Parser.Multiply_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#ulogical_expr.
    def visitUlogical_expr(self, ctx:MT22Parser.Ulogical_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#sign_expr.
    def visitSign_expr(self, ctx:MT22Parser.Sign_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#index_expr.
    def visitIndex_expr(self, ctx:MT22Parser.Index_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcall.
    def visitFuncall(self, ctx:MT22Parser.FuncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#funcall_list.
    def visitFuncall_list(self, ctx:MT22Parser.Funcall_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#operands.
    def visitOperands(self, ctx:MT22Parser.OperandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#stmt.
    def visitStmt(self, ctx:MT22Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assg_stmt.
    def visitAssg_stmt(self, ctx:MT22Parser.Assg_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#lhs.
    def visitLhs(self, ctx:MT22Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#scalar_var.
    def visitScalar_var(self, ctx:MT22Parser.Scalar_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#if_stmt.
    def visitIf_stmt(self, ctx:MT22Parser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#for_stmt.
    def visitFor_stmt(self, ctx:MT22Parser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#conditional_expr.
    def visitConditional_expr(self, ctx:MT22Parser.Conditional_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#update_expr.
    def visitUpdate_expr(self, ctx:MT22Parser.Update_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#init_expr.
    def visitInit_expr(self, ctx:MT22Parser.Init_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#while_stmt.
    def visitWhile_stmt(self, ctx:MT22Parser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#do_while_stmt.
    def visitDo_while_stmt(self, ctx:MT22Parser.Do_while_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#break_stmt.
    def visitBreak_stmt(self, ctx:MT22Parser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continue_stmt.
    def visitContinue_stmt(self, ctx:MT22Parser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_stmt.
    def visitReturn_stmt(self, ctx:MT22Parser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#call_stmt.
    def visitCall_stmt(self, ctx:MT22Parser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_stmt.
    def visitBlock_stmt(self, ctx:MT22Parser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_stmt_prime_2.
    def visitBlock_stmt_prime_2(self, ctx:MT22Parser.Block_stmt_prime_2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_stmt_prime.
    def visitBlock_stmt_prime(self, ctx:MT22Parser.Block_stmt_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#boollit.
    def visitBoollit(self, ctx:MT22Parser.BoollitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arraylit.
    def visitArraylit(self, ctx:MT22Parser.ArraylitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrayprime_2.
    def visitArrayprime_2(self, ctx:MT22Parser.Arrayprime_2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#arrayprime.
    def visitArrayprime(self, ctx:MT22Parser.ArrayprimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#bool_typ.
    def visitBool_typ(self, ctx:MT22Parser.Bool_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#int_typ.
    def visitInt_typ(self, ctx:MT22Parser.Int_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#float_typ.
    def visitFloat_typ(self, ctx:MT22Parser.Float_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#string_typ.
    def visitString_typ(self, ctx:MT22Parser.String_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#element_typ.
    def visitElement_typ(self, ctx:MT22Parser.Element_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_typ.
    def visitArray_typ(self, ctx:MT22Parser.Array_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#type_in_array.
    def visitType_in_array(self, ctx:MT22Parser.Type_in_arrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimension_list.
    def visitDimension_list(self, ctx:MT22Parser.Dimension_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimension_prime.
    def visitDimension_prime(self, ctx:MT22Parser.Dimension_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#void_typ.
    def visitVoid_typ(self, ctx:MT22Parser.Void_typContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#auto_typ.
    def visitAuto_typ(self, ctx:MT22Parser.Auto_typContext):
        return self.visitChildren(ctx)



del MT22Parser