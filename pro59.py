bhte,sbte=map(str,input().split("|"))
ccte=input()
if  len(bhte)>len(sbte):
    if len(bhte)==len(sbte)+len(ccte):
        print(bhte+"|"+sbte+ccte)
elif len(bhte)<len(sbte):
     if len(sbte)==len(bhte)+len(ccte):
        print(bhte+ccte+"|"+sbte)
elif len(bhte)==len(sbte) and len(ccte)>1 or (len(sbte) or len(bhte)):
    print("impossible")
