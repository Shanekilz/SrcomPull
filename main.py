import sys, getopt
import srcomapi, srcomapi.datatypes as dt
api = srcomapi.SpeedrunCom(); api.debug = 1

def main(argv):
    query = ''
    categoryType = ''
    dataReturn = ''
    try:
        opts, args = getopt.getopt(argv, "hq:c:d:", ["query=", "type=", "return="])
    except getopt.GetoptError:
        print('main.py -q <query> -c <category or data> -d <json|csv|tsv>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('main.py -q <query> -c <category or data> -d <json|csv|tsv>')
            sys.exit()
        elif opt in ("-q", "-query"):
            query = arg
        elif opt in ("-c", '-type'):
            categoryType = arg
        elif opt in (-"-d", "-return"):
            dataReturn = arg
    print('Query is ', query)
    print('Data Type is ', categoryType)
    print('Returned data will as ', dataReturn)
    print(api.search(srcomapi.datatypes.Series, {"name": query}))



if __name__ == "__main__":
    main(sys.argv[1:])
