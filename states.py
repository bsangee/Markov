import parse
import numpy as np
import numpy.core.defchararray as np_f

result=[]
def write_bytes_states(data):
        wb =  ([int (x) for x in data])
        for  i  in wb:
                if(i<1001):
                        result.append('0-1000 ')
                elif(i<4001):
                        result.append('1001-4000 ')
                elif(i<16001):
                        result.append('4001-16000 ')
                elif(i<48001):
                        result.append('48001-192000 ')
                elif(i<768001):
                        result.append('192001-768000 ')
                elif(i<3072000):
                        result.append('768001-3072000 ')
                else: result.append('>3072001 ')
        return result

def interarrival_states(data):
        ir =  ([int (x) for x in data])

        for i, x in enumerate(ir):
                if(i>0):
                        result.append(str(x - ir[i - 1])+' ')

        return result


def ost_stripe_states(data):
        for  i  in data:
                result.append(str(i) + ' ')

        return result
