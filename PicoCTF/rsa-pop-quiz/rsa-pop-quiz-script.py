from Crypto.Util.number import inverse
import binascii
import sys

def totient(p, q):
    return (p - 1)*(q - 1)

def encryption(plaintext, e, n):
    return (plaintext**e) % n

def responses():
    #1st
    q = 60413
    p = 76753
    print("Y")
    print(q*p)

    #2nd
    p = 54269
    n = 5051846941
    print("Y")
    print(n//p)

    #3rd
    print("N")

    #4th
    q = 66347
    p = 12611
    print("Y")
    print(totient(q, p))

    #5th
    plaintext = 6357294171489311547190987615544575133581967886499484091352661406414044440475205342882841236357665973431462491355089413710392273380203038793241564304774271529108729717
    e = 3
    n = 29129463609326322559521123136222078780585451208149138547799121083622333250646678767769126248182207478527881025116332742616201890576280859777513414460842754045651093593251726785499360828237897586278068419875517543013545369871704159718105354690802726645710699029936754265654381929650494383622583174075805797766685192325859982797796060391271817578087472948205626257717479858369754502615173773514087437504532994142632207906501079835037052797306690891600559321673928943158514646572885986881016569647357891598545880304236145548059520898133142087545369179876065657214225826997676844000054327141666320553082128424707948750331
    print("Y")
    print(encryption(plaintext,e, n)) 

    #6th
    print("N")  #Why??

    #7th
    q = 92092076805892533739724722602668675840671093008520241548191914215399824020372076186460768206814914423802230398410980218741906960527104568970225804374404612617736579286959865287226538692911376507934256844456333236362669879347073756238894784951597211105734179388300051579994253565459304743059533646753003894559
    p = 97846775312392801037224396977012615848433199640105786119757047098757998273009741128821931277074555731813289423891389911801250326299324018557072727051765547115514791337578758859803890173153277252326496062476389498019821358465433398338364421624871010292162533041884897182597065662521825095949253625730631876637
    e = 65537
    print("Y")
    print(inverse(e, (p-1)*(q-1)))

    #8th
    p = 153143042272527868798412612417204434156935146874282990942386694020462861918068684561281763577034706600608387699148071015194725533394126069826857182428660427818277378724977554365910231524827258160904493774748749088477328204812171935987088715261127321911849092207070653272176072509933245978935455542420691737433
    ciphertext = 18031488536864379496089550017272599246134435121343229164236671388038630752847645738968455413067773166115234039247540029174331743781203512108626594601293283737392240326020888417252388602914051828980913478927759934805755030493894728974208520271926698905550119698686762813722190657005740866343113838228101687566611695952746931293926696289378849403873881699852860519784750763227733530168282209363348322874740823803639617797763626570478847423136936562441423318948695084910283653593619962163665200322516949205854709192890808315604698217238383629613355109164122397545332736734824591444665706810731112586202816816647839648399
    e = 65537
    n = 23952937352643527451379227516428377705004894508566304313177880191662177061878993798938496818120987817049538365206671401938265663712351239785237507341311858383628932183083145614696585411921662992078376103990806989257289472590902167457302888198293135333083734504191910953238278860923153746261500759411620299864395158783509535039259714359526738924736952759753503357614939203434092075676169179112452620687731670534906069845965633455748606649062394293289967059348143206600765820021392608270528856238306849191113241355842396325210132358046616312901337987464473799040762271876389031455051640937681745409057246190498795697239
    r = (p-1)*(n//p-1)
    d = inverse(e,r)
    res = pow(ciphertext, d, n)
    print("Y")
    print(res)
    return res

if(sys.argv[1] == "-A"):
    responses()

elif(sys.argv[1] == "-B"):
    res = responses()
    print(bytes.fromhex(hex(res)[2:]).decode('ascii'))
