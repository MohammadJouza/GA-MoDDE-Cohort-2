# class - defined a class  def = > func
# Error - the name f the class
# ValueTooSmallError
# 
class Error(Exception):
    """00- BASE CLASS FOR OTHER CUSTOMACTION EXCEPTIONS"""
    pass

class ValueTooSmallError(Error):
    """RAISED WHEN THE INPUT VALUE IS TOO SMALL"""
    pass

class ValueTooLargeError(Error):
    """RAISED WHEN THE INPUT VALUE IS TOO LARGE"""
    pass
