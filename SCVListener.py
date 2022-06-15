# Generated from SCV.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SCVParser import SCVParser
else:
    from SCVParser import SCVParser

# This class defines a complete listener for a parse tree produced by SCVParser.
class SCVListener(ParseTreeListener):

    # Enter a parse tree produced by SCVParser#program.
    def enterProgram(self, ctx:SCVParser.ProgramContext):
        pass

    # Exit a parse tree produced by SCVParser#program.
    def exitProgram(self, ctx:SCVParser.ProgramContext):
        pass


    # Enter a parse tree produced by SCVParser#vars_decl.
    def enterVars_decl(self, ctx:SCVParser.Vars_declContext):
        pass

    # Exit a parse tree produced by SCVParser#vars_decl.
    def exitVars_decl(self, ctx:SCVParser.Vars_declContext):
        pass


    # Enter a parse tree produced by SCVParser#var_decl.
    def enterVar_decl(self, ctx:SCVParser.Var_declContext):
        pass

    # Exit a parse tree produced by SCVParser#var_decl.
    def exitVar_decl(self, ctx:SCVParser.Var_declContext):
        pass


    # Enter a parse tree produced by SCVParser#var_spc.
    def enterVar_spc(self, ctx:SCVParser.Var_spcContext):
        pass

    # Exit a parse tree produced by SCVParser#var_spc.
    def exitVar_spc(self, ctx:SCVParser.Var_spcContext):
        pass


    # Enter a parse tree produced by SCVParser#value_init.
    def enterValue_init(self, ctx:SCVParser.Value_initContext):
        pass

    # Exit a parse tree produced by SCVParser#value_init.
    def exitValue_init(self, ctx:SCVParser.Value_initContext):
        pass


    # Enter a parse tree produced by SCVParser#funcs_decl.
    def enterFuncs_decl(self, ctx:SCVParser.Funcs_declContext):
        pass

    # Exit a parse tree produced by SCVParser#funcs_decl.
    def exitFuncs_decl(self, ctx:SCVParser.Funcs_declContext):
        pass


    # Enter a parse tree produced by SCVParser#func_decl.
    def enterFunc_decl(self, ctx:SCVParser.Func_declContext):
        pass

    # Exit a parse tree produced by SCVParser#func_decl.
    def exitFunc_decl(self, ctx:SCVParser.Func_declContext):
        pass


    # Enter a parse tree produced by SCVParser#arguments.
    def enterArguments(self, ctx:SCVParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by SCVParser#arguments.
    def exitArguments(self, ctx:SCVParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by SCVParser#args_list.
    def enterArgs_list(self, ctx:SCVParser.Args_listContext):
        pass

    # Exit a parse tree produced by SCVParser#args_list.
    def exitArgs_list(self, ctx:SCVParser.Args_listContext):
        pass


    # Enter a parse tree produced by SCVParser#arg_list_continuation.
    def enterArg_list_continuation(self, ctx:SCVParser.Arg_list_continuationContext):
        pass

    # Exit a parse tree produced by SCVParser#arg_list_continuation.
    def exitArg_list_continuation(self, ctx:SCVParser.Arg_list_continuationContext):
        pass


    # Enter a parse tree produced by SCVParser#arg_list.
    def enterArg_list(self, ctx:SCVParser.Arg_listContext):
        pass

    # Exit a parse tree produced by SCVParser#arg_list.
    def exitArg_list(self, ctx:SCVParser.Arg_listContext):
        pass


    # Enter a parse tree produced by SCVParser#id_list.
    def enterId_list(self, ctx:SCVParser.Id_listContext):
        pass

    # Exit a parse tree produced by SCVParser#id_list.
    def exitId_list(self, ctx:SCVParser.Id_listContext):
        pass


    # Enter a parse tree produced by SCVParser#id_list_continuation.
    def enterId_list_continuation(self, ctx:SCVParser.Id_list_continuationContext):
        pass

    # Exit a parse tree produced by SCVParser#id_list_continuation.
    def exitId_list_continuation(self, ctx:SCVParser.Id_list_continuationContext):
        pass


    # Enter a parse tree produced by SCVParser#return_type.
    def enterReturn_type(self, ctx:SCVParser.Return_typeContext):
        pass

    # Exit a parse tree produced by SCVParser#return_type.
    def exitReturn_type(self, ctx:SCVParser.Return_typeContext):
        pass


    # Enter a parse tree produced by SCVParser#block.
    def enterBlock(self, ctx:SCVParser.BlockContext):
        pass

    # Exit a parse tree produced by SCVParser#block.
    def exitBlock(self, ctx:SCVParser.BlockContext):
        pass


    # Enter a parse tree produced by SCVParser#stmts.
    def enterStmts(self, ctx:SCVParser.StmtsContext):
        pass

    # Exit a parse tree produced by SCVParser#stmts.
    def exitStmts(self, ctx:SCVParser.StmtsContext):
        pass


    # Enter a parse tree produced by SCVParser#stmt.
    def enterStmt(self, ctx:SCVParser.StmtContext):
        pass

    # Exit a parse tree produced by SCVParser#stmt.
    def exitStmt(self, ctx:SCVParser.StmtContext):
        pass


    # Enter a parse tree produced by SCVParser#assignation.
    def enterAssignation(self, ctx:SCVParser.AssignationContext):
        pass

    # Exit a parse tree produced by SCVParser#assignation.
    def exitAssignation(self, ctx:SCVParser.AssignationContext):
        pass


    # Enter a parse tree produced by SCVParser#if_block.
    def enterIf_block(self, ctx:SCVParser.If_blockContext):
        pass

    # Exit a parse tree produced by SCVParser#if_block.
    def exitIf_block(self, ctx:SCVParser.If_blockContext):
        pass


    # Enter a parse tree produced by SCVParser#if_trigger.
    def enterIf_trigger(self, ctx:SCVParser.If_triggerContext):
        pass

    # Exit a parse tree produced by SCVParser#if_trigger.
    def exitIf_trigger(self, ctx:SCVParser.If_triggerContext):
        pass


    # Enter a parse tree produced by SCVParser#alter.
    def enterAlter(self, ctx:SCVParser.AlterContext):
        pass

    # Exit a parse tree produced by SCVParser#alter.
    def exitAlter(self, ctx:SCVParser.AlterContext):
        pass


    # Enter a parse tree produced by SCVParser#else_block.
    def enterElse_block(self, ctx:SCVParser.Else_blockContext):
        pass

    # Exit a parse tree produced by SCVParser#else_block.
    def exitElse_block(self, ctx:SCVParser.Else_blockContext):
        pass


    # Enter a parse tree produced by SCVParser#loop_block.
    def enterLoop_block(self, ctx:SCVParser.Loop_blockContext):
        pass

    # Exit a parse tree produced by SCVParser#loop_block.
    def exitLoop_block(self, ctx:SCVParser.Loop_blockContext):
        pass


    # Enter a parse tree produced by SCVParser#while_block.
    def enterWhile_block(self, ctx:SCVParser.While_blockContext):
        pass

    # Exit a parse tree produced by SCVParser#while_block.
    def exitWhile_block(self, ctx:SCVParser.While_blockContext):
        pass


    # Enter a parse tree produced by SCVParser#while_trigger.
    def enterWhile_trigger(self, ctx:SCVParser.While_triggerContext):
        pass

    # Exit a parse tree produced by SCVParser#while_trigger.
    def exitWhile_trigger(self, ctx:SCVParser.While_triggerContext):
        pass


    # Enter a parse tree produced by SCVParser#for_loop.
    def enterFor_loop(self, ctx:SCVParser.For_loopContext):
        pass

    # Exit a parse tree produced by SCVParser#for_loop.
    def exitFor_loop(self, ctx:SCVParser.For_loopContext):
        pass


    # Enter a parse tree produced by SCVParser#built_in_func.
    def enterBuilt_in_func(self, ctx:SCVParser.Built_in_funcContext):
        pass

    # Exit a parse tree produced by SCVParser#built_in_func.
    def exitBuilt_in_func(self, ctx:SCVParser.Built_in_funcContext):
        pass


    # Enter a parse tree produced by SCVParser#func_call.
    def enterFunc_call(self, ctx:SCVParser.Func_callContext):
        pass

    # Exit a parse tree produced by SCVParser#func_call.
    def exitFunc_call(self, ctx:SCVParser.Func_callContext):
        pass


    # Enter a parse tree produced by SCVParser#params.
    def enterParams(self, ctx:SCVParser.ParamsContext):
        pass

    # Exit a parse tree produced by SCVParser#params.
    def exitParams(self, ctx:SCVParser.ParamsContext):
        pass


    # Enter a parse tree produced by SCVParser#params_continuation.
    def enterParams_continuation(self, ctx:SCVParser.Params_continuationContext):
        pass

    # Exit a parse tree produced by SCVParser#params_continuation.
    def exitParams_continuation(self, ctx:SCVParser.Params_continuationContext):
        pass


    # Enter a parse tree produced by SCVParser#variable.
    def enterVariable(self, ctx:SCVParser.VariableContext):
        pass

    # Exit a parse tree produced by SCVParser#variable.
    def exitVariable(self, ctx:SCVParser.VariableContext):
        pass


    # Enter a parse tree produced by SCVParser#indexation.
    def enterIndexation(self, ctx:SCVParser.IndexationContext):
        pass

    # Exit a parse tree produced by SCVParser#indexation.
    def exitIndexation(self, ctx:SCVParser.IndexationContext):
        pass


    # Enter a parse tree produced by SCVParser#dimensions.
    def enterDimensions(self, ctx:SCVParser.DimensionsContext):
        pass

    # Exit a parse tree produced by SCVParser#dimensions.
    def exitDimensions(self, ctx:SCVParser.DimensionsContext):
        pass


    # Enter a parse tree produced by SCVParser#dimensions_continuation.
    def enterDimensions_continuation(self, ctx:SCVParser.Dimensions_continuationContext):
        pass

    # Exit a parse tree produced by SCVParser#dimensions_continuation.
    def exitDimensions_continuation(self, ctx:SCVParser.Dimensions_continuationContext):
        pass


    # Enter a parse tree produced by SCVParser#data_type.
    def enterData_type(self, ctx:SCVParser.Data_typeContext):
        pass

    # Exit a parse tree produced by SCVParser#data_type.
    def exitData_type(self, ctx:SCVParser.Data_typeContext):
        pass


    # Enter a parse tree produced by SCVParser#value_literal.
    def enterValue_literal(self, ctx:SCVParser.Value_literalContext):
        pass

    # Exit a parse tree produced by SCVParser#value_literal.
    def exitValue_literal(self, ctx:SCVParser.Value_literalContext):
        pass


    # Enter a parse tree produced by SCVParser#expression.
    def enterExpression(self, ctx:SCVParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SCVParser#expression.
    def exitExpression(self, ctx:SCVParser.ExpressionContext):
        pass


    # Enter a parse tree produced by SCVParser#bool_exp.
    def enterBool_exp(self, ctx:SCVParser.Bool_expContext):
        pass

    # Exit a parse tree produced by SCVParser#bool_exp.
    def exitBool_exp(self, ctx:SCVParser.Bool_expContext):
        pass


    # Enter a parse tree produced by SCVParser#next_bool.
    def enterNext_bool(self, ctx:SCVParser.Next_boolContext):
        pass

    # Exit a parse tree produced by SCVParser#next_bool.
    def exitNext_bool(self, ctx:SCVParser.Next_boolContext):
        pass


    # Enter a parse tree produced by SCVParser#and_exp.
    def enterAnd_exp(self, ctx:SCVParser.And_expContext):
        pass

    # Exit a parse tree produced by SCVParser#and_exp.
    def exitAnd_exp(self, ctx:SCVParser.And_expContext):
        pass


    # Enter a parse tree produced by SCVParser#next_and.
    def enterNext_and(self, ctx:SCVParser.Next_andContext):
        pass

    # Exit a parse tree produced by SCVParser#next_and.
    def exitNext_and(self, ctx:SCVParser.Next_andContext):
        pass


    # Enter a parse tree produced by SCVParser#not_exp.
    def enterNot_exp(self, ctx:SCVParser.Not_expContext):
        pass

    # Exit a parse tree produced by SCVParser#not_exp.
    def exitNot_exp(self, ctx:SCVParser.Not_expContext):
        pass


    # Enter a parse tree produced by SCVParser#bool_term.
    def enterBool_term(self, ctx:SCVParser.Bool_termContext):
        pass

    # Exit a parse tree produced by SCVParser#bool_term.
    def exitBool_term(self, ctx:SCVParser.Bool_termContext):
        pass


    # Enter a parse tree produced by SCVParser#rel_exp.
    def enterRel_exp(self, ctx:SCVParser.Rel_expContext):
        pass

    # Exit a parse tree produced by SCVParser#rel_exp.
    def exitRel_exp(self, ctx:SCVParser.Rel_expContext):
        pass


    # Enter a parse tree produced by SCVParser#num_exp.
    def enterNum_exp(self, ctx:SCVParser.Num_expContext):
        pass

    # Exit a parse tree produced by SCVParser#num_exp.
    def exitNum_exp(self, ctx:SCVParser.Num_expContext):
        pass


    # Enter a parse tree produced by SCVParser#prod_exp.
    def enterProd_exp(self, ctx:SCVParser.Prod_expContext):
        pass

    # Exit a parse tree produced by SCVParser#prod_exp.
    def exitProd_exp(self, ctx:SCVParser.Prod_expContext):
        pass


    # Enter a parse tree produced by SCVParser#prod_div.
    def enterProd_div(self, ctx:SCVParser.Prod_divContext):
        pass

    # Exit a parse tree produced by SCVParser#prod_div.
    def exitProd_div(self, ctx:SCVParser.Prod_divContext):
        pass


    # Enter a parse tree produced by SCVParser#sum_res.
    def enterSum_res(self, ctx:SCVParser.Sum_resContext):
        pass

    # Exit a parse tree produced by SCVParser#sum_res.
    def exitSum_res(self, ctx:SCVParser.Sum_resContext):
        pass


    # Enter a parse tree produced by SCVParser#factor.
    def enterFactor(self, ctx:SCVParser.FactorContext):
        pass

    # Exit a parse tree produced by SCVParser#factor.
    def exitFactor(self, ctx:SCVParser.FactorContext):
        pass


    # Enter a parse tree produced by SCVParser#prod_op.
    def enterProd_op(self, ctx:SCVParser.Prod_opContext):
        pass

    # Exit a parse tree produced by SCVParser#prod_op.
    def exitProd_op(self, ctx:SCVParser.Prod_opContext):
        pass


    # Enter a parse tree produced by SCVParser#sum_op.
    def enterSum_op(self, ctx:SCVParser.Sum_opContext):
        pass

    # Exit a parse tree produced by SCVParser#sum_op.
    def exitSum_op(self, ctx:SCVParser.Sum_opContext):
        pass


    # Enter a parse tree produced by SCVParser#rel_operator.
    def enterRel_operator(self, ctx:SCVParser.Rel_operatorContext):
        pass

    # Exit a parse tree produced by SCVParser#rel_operator.
    def exitRel_operator(self, ctx:SCVParser.Rel_operatorContext):
        pass



del SCVParser