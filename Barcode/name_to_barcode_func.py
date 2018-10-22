entering_name = input("Enter your name: ").upper()
 
name_dict = dict(A='101', B='102', C='103', D='104', E='105',
                 F='106', G='107', H='108', I='109', J='110',
                 K='111', L='112', M='113', N='114', O='115',
                 P='116', Q='117', R='118', S='119', T='120',
                 U='121', V='122', W='123', X='124', Y='125',
                 Z='126')
 
barcode_name = []
 
 
def create_barcode(name):
    for x in name:
        if x == ' ':
            barcode_name.append('000')
        elif name_dict.get(x) is None:
            print("Non-Latin letters do not allowed")
            continue
        else:
            barcode_name.append(name_dict.get(x))
 
    barcode = int(''.join((str(i) for i in barcode_name)))
 
    return barcode