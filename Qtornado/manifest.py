import sys
import os
import argparse

# load functional lib 
from Qtornado.Qtornado import TreeFile

root_path = os.path.dirname(__file__)

def handle_args():
    desc = """
this is a assistant for write web html
weite by Qingluan
github : http://github.com/Qingluan
    """
    parser = argparse.ArgumentParser(usage='it is usage for qingluanTornado ', description=desc)
    parser.add_argument('-u','--unintall',action="store_true",default=False,help="uninstall this project")
    parser.add_argument('-c','--add-controller',default=None)
    parser.add_argument('-t','--theme-choice',default=None)
    parser.add_argument('--websocket',action="store_true", default=False, help="websocket mode")
    parser.add_argument('-e','--extends',default=None,help="this will create a new html by extends another template ")  
    # args,remind = parser.parse_known_args(args)
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = handle_args()

    workpath =  os.path.dirname(__file__) #  
    tree = TreeFile(workpath)


    if args.unintall:
        os.popen("rm -rf ./*")

    if args.add_controller:
        tree.add_controller(
            args.add_controller, 
            extends=args.extends, 
            websocket=args.websocket,
            theme=args.theme_choice)


