import parse
import numpy as np
import numpy.core.defchararray as np_f

result=[]
def write_bytes_states(data):
        wb =  ([int (x) for x in data])
        for  i  in wb:
                if(i<1001):
                        result.append('500.5 ')
                elif(i<4001):
                        result.append('2500.5 ')
                elif(i<16001):
                        result.append('10000.5 ')
                elif(i<48001):
                        result.append('32000.5')
                elif(i<192000):
                        result.append('120000.5 ')
                elif(i<768001):
                        result.append('480000.5 ')
                elif(i<3072000):
                        result.append('1920000.5 ')
                else: result.append('3072001 ')
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
