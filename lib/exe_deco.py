# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2018-06-02 16:07:18
# @Last Modified by:   Administrator
# @Last Modified time: 2018-06-02 21:08:08

import traceback
from .write_log import write_log
from  utils.utils import str_2_tuple


def exe_deco(func):
    def _deco(*args, **kwargs):
        print('func exe_deco')
        result = ()
        try:
            ret = func(*args, **kwargs)
        except Exception as e:
            log = 'Exception in ' + func.__name__ + 'method :' + str(e)
            write_log(log)
            result = result+str_2_tuple(log)
        else:
            log = 'No exception in '+func.__name__+"  method"
            write_log(log)
            result = result+str_2_tuple(log)
        finally:
            return result

    return _deco
