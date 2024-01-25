import sys
from sys import argv
import webbrowser

cli_arg = argv[1]
src_arg = argv[2] if len(sys.argv) > 2 else '0'
search_text = 'https://www.google.com/search?q='
marketcap = 'https://coinmarketcap.com'


def run_url():
    try:
        match cli_arg:
            case 'cmc':
                webbrowser.open(marketcap, new=2, autoraise=True)
            case 'search':
                webbrowser.open(search_text + src_arg, new=2, autoraise=True)
            case _:
                print('\nWARNING: invalid input\n')
    except IndexError:
        return None


if __name__ == '__main__':
    run_url()
