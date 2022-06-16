from select import select
from antlr4 import *                #
from SCVLexer import SCVLexer       #
from SCVParser import SCVParser     #
from SCVListener import *           #
from stack import *                 #
from pprint import pprint           #

def report_error(ctx, msg):
    line = ctx.start.line
    column = ctx.start.column
    print(f'error {line}:{column} {msg}')

t_count = 0     # Contador para generar cuadrúplos

line_return = 0 # Registrar linea a regresar en saltos



# cuadruplo = []  # Elementos de cuadrúplo

#############################################################################################
#                                 DICCIONARIO DE OPERACIONES
#############################################################################################
BIN = "bin"
UNI = "uni"

op_nary = {
    "+"     : BIN,
    "-"     : BIN,
    "*"     : BIN,
    "/"     : BIN,
    "<"     : BIN,
    ">"     : BIN,
    "<="    : BIN,
    ">="    : BIN,
    "="     : BIN,
    "and"   : BIN,
    "or"    : BIN,
    "not"   : UNI,
    ":="    : BIN,
    "print" : UNI
}

#############################################################################################
#                                      OPERACIONES
#############################################################################################

def gen_quad(self):
    op = self.opstack.pop()
    p = []
    c = []

    c.append(op)

    # Evaluar número de parametros necesarios para operación
    if op_nary[op] == BIN:
        val0 = self.valstack.pop()
        val1 = self.valstack.pop()

        if op == ':=':
            c.append(val0)
            c.append(' ')
            c.append(val1)
        else:
            c.append(val0)
            c.append(val1)


        p.append(val0)
        p.append(val1)

    elif op_nary[op] == UNI:
        val0 = self.valstack.pop()
        c.append(' ')
        c.append(val0)
        p.append(val0)

    else :
        pass
    
    #print('====>', op, p)

    if op != ':=' :
        for i, _ in enumerate(p):
            if isinstance(p[i], int):
                continue
            elif isinstance(p[i], float):
                continue
            elif p[i].isidentifier():
                if p[i] in self.symtable:
                    continue
                elif p[i][0] == '_':
                    continue
                else:
                    raise Exception(f'variable {p[i]} not declared')
            else:
                raise Exception('unidentified', p[i])

    
    # Realizar operaciones aritméticas
    global t_count
    temp = '_t' + str(t_count)

    if op != ':=':
        t_count += 1 
        self.valstack.append(temp)
        self.symtable[temp] = dict()

        c.append(temp)

    self.ir_code.append(c)
    print(c)

    # Realizar operaciones Built_In
    #elif op == 'print':
        #self.valstack.append(0)


#############################################################################################
#                                     CLASE INTERPRETADOR
#############################################################################################

# This class defines a complete listener for a parse tree produced by SCVParser.
class Interpreter(SCVListener):
    symtable = dict()
    symlocal = set()
    ctrl_var = set()

    in_function = False

    opstack = Stack()   # Stack para operadores
    valstack = Stack()  # Stack para valores

    ir_code = []        # Lista de cuadrúplos

    jumps = Stack()     # Stack para saltos

    reading_ctrl_var = False

    for_direction = 1

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
        sym = ctx.ID().getText()

        if sym in self.symtable:
            report_error(ctx, f'duplicated variable "{sym}"')
            exit()

        symtype = ctx.data_type().getText()

        self.symtable[sym] = dict()
        self.symtable[sym]['type'] = symtype

        if symtype == 'mat':
            pass
        else:
            symvalue = ctx.var_spc().value_init().value_literal().getText()
            
            if symtype == 'int':
                symvalue = int(symvalue)
            else:
                symvalue = float(symvalue)

            self.opstack.append(':=')
            self.valstack.append(sym)
            self.valstack.append(symvalue)
            gen_quad(self)

            if self.in_function:
                self.symlocal.add(sym)

            print(self.symtable)

    # Exit a parse tree produced by SCVParser#var_decl.
    def exitVar_decl(self, ctx:SCVParser.Var_declContext):
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
        self.in_function = True

    # Exit a parse tree produced by SCVParser#func_decl.
    def exitFunc_decl(self, ctx:SCVParser.Func_declContext):
        for sym in self.symlocal:
            del self.symtable[sym]

        self.in_function = False


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
        sym = ctx.variable().getText()

        self.valstack.append(sym)
        self.opstack.append( ':=' )

        print('OpStack',self.opstack)
        print('ValStack',self.valstack)

    # Exit a parse tree produced by SCVParser#assignation.
    def exitAssignation(self, ctx:SCVParser.AssignationContext):
        sym = ctx.variable().getText()

        if not self.valstack.empty():
            self.valstack.pop()

        pprint(self.symtable)

    # Enter a parse tree produced by SCVParser#if_block.
    def enterIf_block(self, ctx:SCVParser.If_blockContext):
        pass

    # Exit a parse tree produced by SCVParser#if_block.
    def exitIf_block(self, ctx:SCVParser.If_blockContext):
        pass

    # Enter a parse tree produced by SCVParser#if_trigger.
    def enterIf_trigger(self, ctx:SCVParser.If_triggerContext):
        cuad_jump = ['gotof', self.valstack.pop(), ' ']
        self.jumps.append(len(self.ir_code))
        self.ir_code.append(cuad_jump)

    # Exit a parse tree produced by SCVParser#if_trigger.
    def exitIf_trigger(self, ctx:SCVParser.If_triggerContext):
        pass

    # Enter a parse tree produced by SCVParser#alter.
    def enterAlter(self, ctx:SCVParser.AlterContext):
        i = self.jumps.pop()    
        next_jump = len(self.ir_code) + 1
        self.ir_code[i].append(next_jump)

    # Exit a parse tree produced by SCVParser#alter.
    def exitAlter(self, ctx:SCVParser.AlterContext):
        pass

    # Enter a parse tree produced by SCVParser#else_block.
    def enterElse_block(self, ctx:SCVParser.Else_blockContext):
        cuad_jump = ['goto', ' ', ' ']
        self.jumps.append(len(self.ir_code))
        self.ir_code.append(cuad_jump)

    # Exit a parse tree produced by SCVParser#else_block.
    def exitElse_block(self, ctx:SCVParser.Else_blockContext):
        i = self.jumps.pop()    
        next_jump = len(self.ir_code) 
        self.ir_code[i].append(next_jump)


    # Enter a parse tree produced by SCVParser#loop_block.
    def enterLoop_block(self, ctx:SCVParser.Loop_blockContext):
        pass

    # Exit a parse tree produced by SCVParser#loop_block.
    def exitLoop_block(self, ctx:SCVParser.Loop_blockContext):
        pass


    # Enter a parse tree produced by SCVParser#while_block.
    def enterWhile_block(self, ctx:SCVParser.While_blockContext):
        self.jumps.append(len(self.ir_code))

    # Exit a parse tree produced by SCVParser#while_block.
    def exitWhile_block(self, ctx:SCVParser.While_blockContext):
        cuad_jump = ['goto', ' ', ' ']
        self.ir_code.append(cuad_jump)

        i = self.jumps.pop()    
        next_jump = len(self.ir_code)
        self.ir_code[i].append(next_jump)
        
        i = self.jumps.pop()
        self.ir_code[-1].append(i)

    # Enter a parse tree produced by SCVParser#while_trigger.
    def enterWhile_trigger(self, ctx:SCVParser.While_triggerContext):
        cuad_jump = ['gotof', self.valstack.pop(), ' ']
        self.jumps.append(len(self.ir_code))
        self.ir_code.append(cuad_jump)

    # Exit a parse tree produced by SCVParser#while_trigger.
    def exitWhile_trigger(self, ctx:SCVParser.While_triggerContext):
        pass

    # Enter a parse tree produced by SCVParser#for_loop.
    def enterFor_loop(self, ctx:SCVParser.For_loopContext):
        self.reading_ctrl_var = True
        var = ctx.ID().getText()
        if var in self.symtable:
            raise Exception('Variable: ', var, 'no puede usarse como variable de control.', )
        else :
            self.ctrl_var.add(var)

        self.symtable[var] = dict()

        factor1 = int(ctx.for_inferior().factor().getText())
        factor2 = int(ctx.for_superior().factor().getText())

        if factor1 == factor2:
            raise Exception('Limites definidos no válidos')
        else:
            increment = 1 if factor1 < factor2 else 0
        
        if ctx.REVERSE() is None :
            if increment == 1 :
                self.opstack.append('+')
                self.valstack.append(var)
                self.valstack.append(1)

                gen_quad(self)
            else :
                raise Exception('Límites inválidos')
            


        self.jumps.append(len(self.ir_code)+1)


    # Exit a parse tree produced by SCVParser#for_loop.
    def exitFor_loop(self, ctx:SCVParser.For_loopContext):
        cuad_jump = ['gotof', ' ', ' ']
        self.ir_code.append(cuad_jump)

        i = self.jumps.pop()
        self.ir_code[-1].append(i)

        for sym in self.ctrl_var:
            del self.symtable[sym]

        self.ctrl_var.clear()

     # Enter a parse tree produced by SCVParser#loop_trigger1.
    def enterLoop_trigger1(self, ctx:SCVParser.Loop_trigger1Context):
        self.reading_ctrl_var = False

    # Enter a parse tree produced by SCVParser#for_inferior.
    def enterFor_inferior(self, ctx:SCVParser.For_inferiorContext):
        pass

    # Exit a parse tree produced by SCVParser#for_inferior.
    def exitFor_inferior(self, ctx:SCVParser.For_inferiorContext):
        pass


    # Enter a parse tree produced by SCVParser#for_superior.
    def enterFor_superior(self, ctx:SCVParser.For_superiorContext):
        pass

    # Exit a parse tree produced by SCVParser#for_superior.
    def exitFor_superior(self, ctx:SCVParser.For_superiorContext):
        pass
    
    # Exit a parse tree produced by SCVParser#loop_trigger1.
    def exitLoop_trigger1(self, ctx:SCVParser.Loop_trigger1Context):
        pass


    # Enter a parse tree produced by SCVParser#built_in_func.
    def enterBuilt_in_func(self, ctx:SCVParser.Built_in_funcContext):
        pass

    # Exit a parse tree produced by SCVParser#built_in_func.
    def exitBuilt_in_func(self, ctx:SCVParser.Built_in_funcContext):
        sym = ctx.id_list().ID().getText()

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
        if not self.opstack.empty():
            gen_quad(self)

        print('OpStack',self.opstack)
        print('ValStack',self.valstack)


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
        self.opstack.append(ctx.rel_operator().getText())
        gen_quad(self)


    # Enter a parse tree produced by SCVParser#num_exp.
    def enterNum_exp(self, ctx:SCVParser.Num_expContext):
        #self.opstack.append( '(' )
        pass

    # Exit a parse tree produced by SCVParser#num_exp.
    def exitNum_exp(self, ctx:SCVParser.Num_expContext):
        if not self.opstack.empty():
            operator = self.opstack.top()
            if not self.opstack.empty() and (operator == '*' or  operator == '/'):
                gen_quad(self)

    # Enter a parse tree produced by SCVParser#prod_exp.
    def enterProd_exp(self, ctx:SCVParser.Prod_expContext):
        pass

    # Exit a parse tree produced by SCVParser#prod_exp.
    def exitProd_exp(self, ctx:SCVParser.Prod_expContext):
        if not self.opstack.empty():
            operator = self.opstack.top()
            if not self.opstack.empty() and (operator == '+' or  operator == '-'):
                gen_quad(self)
            print('OpStack',self.opstack)
            print('ValStack',self.valstack)
        

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
        #self.valstack.append(ctx.getText())
        if self.reading_ctrl_var:
            return
        
        if ctx.CTE_INT() :
            self.valstack.append(int(ctx.getText()))
        elif ctx.CTE_FLOAT() :
            self.valstack.append(float(ctx.getText()))
        elif ctx.num_exp():
            self.opstack.append('(')
        elif ctx.getText():
            #print(ctx.getText())
            #print(self.symtable[ctx.getText()])
            self.valstack.append(ctx.getText())

        
        
    # Exit a parse tree produced by SCVParser#factor.
    def exitFactor(self, ctx:SCVParser.FactorContext):
        if not self.opstack.empty():
            operator = self.opstack.top()

            if operator == '*' or  operator == '/':
                gen_quad(self)

        if ctx.num_exp():
            self.opstack.append(')')

        print('OpStack',self.opstack)
        print('ValStack',self.valstack)

    # Enter a parse tree produced by SCVParser#prod_op.
    def enterProd_op(self, ctx:SCVParser.Prod_opContext):
        operator = ctx.getText()
        if operator == '*' :
            self.opstack.append( '*' )
        else:
            self.opstack.append( '/' )

    # Exit a parse tree produced by SCVParser#prod_op.
    def exitProd_op(self, ctx:SCVParser.Prod_opContext):
        pass


    # Enter a parse tree produced by SCVParser#sum_op.
    def enterSum_op(self, ctx:SCVParser.Sum_opContext):
        operator = ctx.getText()
        if operator == '+' :
            self.opstack.append( '+' )
        else:
            self.opstack.append( '-' )

    # Exit a parse tree produced by SCVParser#sum_op.
    def exitSum_op(self, ctx:SCVParser.Sum_opContext):
        pass

    # Enter a parse tree produced by SCVParser#rel_operator.
    def enterRel_operator(self, ctx:SCVParser.Rel_operatorContext):
        pass

    # Exit a parse tree produced by SCVParser#rel_operator.
    def exitRel_operator(self, ctx:SCVParser.Rel_operatorContext):
        pass
    
