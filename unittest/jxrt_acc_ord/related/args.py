def fun_parms1(parm):
    print("args is %s" %parm)
def fun_parms2(parms1,parms2):
    print("parms1 is %s parms2 is %s" %(parms1,parms2))

#灵活，可以传多个参数 *可以是任意个数
def fun_var_parms(*parms):
    for value in parms:
        print("parms:",value)


fun_parms1('爱我中华！')
fun_parms2('爱我中华！','祖国大好河山')
fun_var_parms('爱我中华！','祖国大好河山！','人生苦短，我要学Python！')