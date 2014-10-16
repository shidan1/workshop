# Things to consider?
from slimit.lexer import Lexer

# Problem string: \u, \x, 0x, %u

# Does String contain \x or 0x
def feature101(str):
    #f = open(path)
    #script = f.read()
    lexer = Lexer()
    lexer.input(str)
    counter = 0
    while True:
        token = lexer.token()
        if not token:
            break
        if token.type == 'STRING':
            counter = token.value.count('\\x')
    return counter

def feature102(str):
    #f = open(path)
    #script = f.read()
    return str.count('0x')

def feature103(str):
    #f = open(path)
    #script = f.read()
    return str.count('\\u')
    
def feature104(str):
    #f = open(path)
    #script = f.read()
    return str.count('%u')


s1 = r'''var _0xb3c2=["\x63\x72\x75\x65\x6C\x20\x77\x6F\x72\x6C\x64"];function 
hello(){alert(_0xb3c2[0]);} ;'''
s2 = '''var Ol0='7kSKlBXYjNXZfhSZwF2YzVmb1hSZ0lmc35CduVWb1N2bktTKwwGMfhCZslGaDRmblBHch5yTxkkC70FMblyJkFWZodCKl1WYOdWYUlnQzRnbl1WZsVEdldmL05WZtV3YvRGI9AyTxkEIyFmdKsTKMJVVuQnbl1Wdj9GZoQnbl52bw12bDlkUVVGZvNmbltyJ9wmc1ZyJrkiclJnclZWZy5CduVWb1N2bkhCduVmbvBXbvNUSSVVZk92YuV2Kn0jZlJnJnsyJr9WPjJ3c0V2Z/8SbvNmLy9GdhN2c1ZmYvxWb0hmLpBXYv8iOwRHdodCI9AyYyNnLwwGMfpwOpcCdwlmcjN3JoQnbl1WZsVUZ0FWZyNmL05WZtV3YvRGI9ACMsBzXgIXY2tzJFNTJ0BXayN2cvM0MlEEMlQ0NlEEMlI0MlkjMlIjMlQGby92dwITJsVWdyNmMyUCOyUCdyVGbhBjMlAjMlEEMlI0NlAjMlkjMlgjMl8GbsVGawITJu9Wa0Nmb1ZWRzUCdwlmcjN3QzUyJ9UGchN2cl9FIyFmd';var _0x84de=["ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=","","charAt","indexOf","fromCharCode","length"];function _1I1(data){var lOIlOI=_0x84de[0];var o1,o2,o3,h1,h2,h3,h4,bits,i=0,enc=_0x84de[1];do{h1=lOIlOI[_0x84de[3]](data[_0x84de[2]](i++));h2=lOIlOI[_0x84de[3]](data[_0x84de[2]](i++));h3=lOIlOI[_0x84de[3]](data[_0x84de[2]](i++));h4=lOIlOI[_0x84de[3]](data[_0x84de[2]](i++));bits=h1<<18|h2<<12|h3<<6|h4;o1=bits>>16&0xff;o2=bits>>8&0xff;o3=bits&0xff;if(h3==64){enc+=String[_0x84de[4]](o1);} else {if(h4==64){enc+=String[_0x84de[4]](o1,o2);} else {enc+=String[_0x84de[4]](o1,o2,o3);} ;} ;} while(i<data[_0x84de[5]]);;return enc;} ;function lOI(string){var ret=_0x84de[1],i=0;for(i=string[_0x84de[5]]-1;i>=0;i--){ret+=string[_0x84de[2]](i);} ;return ret;} ;eval(_1I1(lOI(Ol0)));'''

print(feature102(s2))
