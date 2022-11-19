def from_base10(n:int,b:int):
    if n<0:
        raise ValueError ("Enter positive number ")
    if b<2:
        raise ValueError ("Enter correct base ")    
    digits=[]
    while n >0:
        n,m=divmod(n,b)
        digits.insert(0,m)
    return (digits)    
def encode (digits,digits_map):
    if max (digits) >= len(digits_map):
        raise ValueError ("Error")
    encoding=''.join(digits_map[d] for d in digits)
    return encoding
def rebase_from10(number,base):
    if 2>base >32:
        raise ValueError ("Error")
    digits_map="0123456789abcdefghijklmnopqrstuvwxyz"    
    sign=-1 if number <0 else 1
    number*=sign
    encoding =encode (from_base10(number,base),digits_map)
    return encoding
print (rebase_from10(3451,16))    




        