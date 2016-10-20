import chained
import states
from parse import parser
"""You can change the order here"""
order = 3
def wb_chain():
    p = parser()
    p.parse_file()  #File name can be changed in parse.py
    text = p.write_bytes
    text = states.write_bytes_states(text)
    chained.markov_chain(text,order)


def rb_chain():
    p = parser()
    p.parse_file()
    text = p.read_bytes
    text = states.write_bytes_states(text)
    chained.markov_chain(text,order)


def ost_chain():
    p = parser()
    p.parse_file()
    text = p.stripe_count
    text = states.ost_stripe_states(text)
    chained.markov_chain(text,order)


def inter_arrival():
    p = parser()
    p.parse_file()
    text = p.timestamp
    text = states.interarrival_states(text)
    chained.markov_chain(text,order)


def main():
        """Uncomment the function as needed """
        wb_chain()
#       rb_chain()
#       ost_chain()
#       inter_arrival()


if __name__ == "__main__": main()
