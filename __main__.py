import os
import datetime


class loghandle:
    # Initial launch
    
    def __init__(self):
        self.setpath = []
    # Path Set

    def pathset(self, string):
        try:
            if isinstance(string, str):
                try:
                    self.setpath.append(string)
                except Exception as e:
                    print("Error -- "+
                          str(e))
            else:
                print("ERR A1 :: %PATH% MUST BE STRING")
        except:
            print("Error -- "+
                  str(e))
    # Main Handling

    def error(self, error, LINE=None, SECOND=None, MINUTE=None, HOUR=None, AT=None):
        date = datetime.datetime.now()
        refreshed_time = []
        small_time =[]
        refreshed_time.append(date.date())
        if AT is True:
            small_time.append(' - Second: '+
                              str(date.second))
            small_time.append(' - Minute: '+
                              str(date.minute))
            small_time.append(' - Hour: '+
                              str(date.hour))
        if SECOND is True:
            small_time.append(' - Second: '+
                              str(date.second))
        if MINUTE is True:
            small_time.append(' - Minute: '+
                              str(date.minute))
        if HOUR is True:
            small_time.append(' - Hour: '+
                              str(date.hour))


        #PathExist checker
        if len(self.setpath[0:]) >= 1:
            def write(error):
                dir = self.setpath[0]
                string = str(error)
                if LINE is None:
                    if len(small_time) >= 1: output =("\nLOGGED - "+
                                                      str(refreshed_time[0])+
                                                      " - "+str(small_time)+
                                                      " --> "+string)
                    else: output =("\nLOGGED - "+
                                   str(refreshed_time[0])+
                                   " - LINE:"+
                                   LINE+
                                   " --> "+
                                   string)
                else:
                    try:
                        if type(LINE) is str:
                            if len(small_time) >= 1: output =("\nLOGGED - "+
                                                              str(refreshed_time[0])+
                                                              " - LINE:"+LINE+" - "+
                                                              str(small_time)+
                                                              " --> "+
                                                              string)
                            else: output =("\nLOGGED - "+
                                           str(refreshed_time[0])+
                                           " - LINE:"+
                                           LINE+
                                           " --> "+
                                           string)

                        else: print("ERR C1 :: )%line_number% MUST BE INT :: "+
                                    str(type(LINE))+
                                    "_NotAccepted");return False
                    except Exception as e: print(str(e))
                try:
                    log_write = open(dir+
                                     "/logs/LOG "+
                                     str(datetime.datetime.now().date())+
                                     ".txt", "a+")
                    log_write.write(str(output)) #Where the lines are executed to the note // Written
                    log_write.close()
                except Exception as e:
                    try:
                        os.mkdir('logs')
                        write(error)
                    except: print(str(e));pass

            try:
                dic = self.setpath
                try:
                    write(error)
                except ImportError as e:
                    try:
                        print("Error -- "+
                              str(e))
                        print("Attempting install")
                        try:
                            os.system("pip install datetime")
                            write(error)
                        except OSError as e:
                            print("Error -- "+
                                  str(e))
                        except RuntimeError as e:
                            print("Error -- "+
                                  str(e))
                    except:
                        print("Error - *Imports not available")
            except KeyboardInterrupt or ValueError as e:
                print("Error -- "+
                      str(e))
            except RuntimeError as fatal:
                return ("FATAL ERROR CONTACT DEVELOPER ---- "+
                        str(fatal))
            except FileNotFoundError:
                os.mkdir('logs')
                write(error)
            except FileExistsError:
                write(error)
            except:
                return
        else:
            print("ERR A2 :: %PATH% MUST BE SET")
''' TEST ERROR
    try:
        1+a
    except Exception as e:
        handler = loghandle()
        handler.pathset(r"C:\Users\nolan.e.taft\Desktop\WinPy - Copy\WPy64-3920")
        handler.error(str(e))
'''
