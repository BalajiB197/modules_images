import modules
import argparse

# print(f'loading main.py: __name__ = {__name__}')

if __name__ == "__main__":
    print('running this code')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('conversion_format', 
                        type=str,
                        help='convert jpg to png.')
    parser.add_argument('path', 
                        type=str,
                        help='convert jpg to png.')
    parser.add_argument('--new_percent', 
                        type=float,
                        default=0.5,
                        help='conversion percent')
    args = parser.parse_args()

    if args.__dict__['conversion_format'] == 'j2p':
        print(f'jpeg_to_png: {args.path}...')
        modules.j2p(args.path)
    elif args.__dict__['conversion_format'] == 'p2j':
        print(f'png_to_jpeg: {args.path}...') 
        modules.p2j(args.path)  
    elif args.__dict__['conversion_format'] == 'res_p':
        modules.res_p(args.path, args.new_percent)
    elif args.__dict__['conversion_format'] == 'res_w':
        modules.res_w(args.path, args.new_percent)
    elif args.__dict__['conversion_format'] == 'res_h':
        modules.res_h(args.path, args.new_percent)
    elif args.__dict__['conversion_format'] == 'crp_px': 
        modules.crp_px(args.path, args.new_percent)