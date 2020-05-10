import argparse

def add2Num(args):
    print("adding the inputs: {0} and {1}".format(args.a,args.b))
    print(args.a+args.b)
    

def add3Num(args):
    print("adding the inputs: {0} and {1} and {2}".format(args.a,args.b,args.c))
    print(args.a + args.b + args.c)

def main():
    parser = argparse.ArgumentParser(prog='PROG')
    subparsers = parser.add_subparsers()
    
    #defining arguments for 1st command: add2
    add2 = subparsers.add_parser('add2')
    add2.add_argument('a',type=int)
    add2.add_argument('b',type=int)
    add2.set_defaults(func=add2Num)
    
    #defining arguments for second command: add3
    add3 = subparsers.add_parser('add3')
    add3.add_argument('a',type=int)
    add3.add_argument('b',type=int)
    add3.add_argument('c',type=int)
    add3.set_defaults(func=add3Num)
    
    args = parser.parse_args()
    args.func(args)
        
if __name__ == '__main__':
    main()



