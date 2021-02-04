import tester, sys
app = tester.loghandle()
app.pathset('.')
try:
    print(s) #Error on purpose
except Exception as e:
    exception_type, exception_object, exception_traceback = sys.exc_info()
    line_number = str(exception_traceback.tb_lineno)
    app.error(e, LINE=line_number, AT=True )