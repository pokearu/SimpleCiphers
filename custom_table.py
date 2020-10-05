"""Custom substitution table script
"""

def get_substitution_map(english_letter, message_letter):
    """
    Takes a list of most frequent english alphabets and sorted list of alphabets from the message.
    Returns a map of the substitution table.
    """
    return { message_letter[i] : english_letter[i] for i in range(0,26)}

def letter_frequency_calculator(message):
    """
    Takes the message as input.
    Computes the frequency of occurance of each alphabet and returns a map. 
    """
    count_map = {}
    message = message.upper()
    for letter in message:
        if not letter.isalpha():
            continue
        if letter in count_map:
            count_map[letter] = count_map[letter] + 1
        else:
            count_map[letter] = 1

    total_letters = sum(val for val in count_map.values())
    freq_map = {k: round((v/total_letters) * 100, 2)
                for k, v in sorted(count_map.items(), key=lambda item: item[1], reverse=True)}
    
    return freq_map

def decode_message(input, substitution_map):
    """
    Takes an encoded string as input along with substitution table.
    Maps every alphabet in the table with the message and returns the decryted message. 
    """
    input = list(input)
    message_len = len(input)
    for i in range(message_len):
        alphabet = input[i].upper()
        if alphabet in substitution_map:
            input[i] = substitution_map[alphabet] if input[i].isupper() else substitution_map[alphabet].lower()
    
    return "".join(input)

if __name__ == "__main__":
    encrypted_message = """
        Wn wb z nxhnt hmwsjxbzaao zeimrgajycjy, ntzn z bwmcaj pzm wm frbbjbbwrm rq z crry
        qrxnhmj, phbn lj wm gzmn rq z gwqj.
        Trgjsjx awnnaj imrgm ntj qjjawmcb rx swjgb rq bhet z pzm pzo lj rm twb qwxbn jmnjxwmc
        z mjwctlrhxtrry, ntwb nxhnt wb br gjaa qwkjy wm ntj pwmyb rq ntj bhxxrhmywmc qzpwawjb,
        ntzn tj wb ermbwyjxjy ntj xwctnqha fxrfjxno rq brpj rmj rx rntjx rq ntjwx yzhctnjxb.
        "Po yjzx Px. Ljmmjn," bzwy twb azyo nr twp rmj yzo, "tzsj orh tjzxy ntzn Mjntjxqwjay
        Fzxi wb ajn zn azbn?"
        Px. Ljmmjn xjfawjy ntzn tj tzy mrn.
        "Lhn wn wb," xjnhxmjy btj; "qrx Pxb. Armc tzb dhbn ljjm tjxj, zmy btj nray pj
        zaa zlrhn wn."
        Px. Ljmmjn pzyj mr zmbgjx.
        "Yr orh mrn gzmn nr imrg gtr tzb nzijm wn?" exwjy twb gwqj wpfznwjmnao.
        " Orh gzmn nr njaa pj, zmy W tzsj mr rldjenwrm nr tjzxwmc wn."
        Ntwb gzb wmswnznwrm jmrhct.
        "Gto, po yjzx, orh phbn imrg, Pxb. Armc bzob ntzn Mjntjxqwjay wb nzijm lo z orhmc
        pzm rq azxcj qrxnhmj qxrp ntj mrxnt rq Jmcazmy; ntzn tj ezpj yrgm rm Prmyzo wm
        z etzwbj zmy qrhx nr bjj ntj fazej, zmy gzb br phet yjawctnjy gwnt wn, ntzn tj
        zcxjjy gwnt Px. Prxxwb wppjywznjao; ntzn tj wb nr nzij frbbjbbwrm ljqrxj Pwetzjapzb,
        zmy brpj rq twb bjxszmnb zxj nr lj wm ntj trhbj lo ntj jmy rq mjkn gjji."
        "Gtzn wb twb mzpj?"
        "Lwmcajo."
        "Wb tj pzxxwjy rx bwmcaj?"
        "Rt! Bwmcaj, po yjzx, nr lj bhxj! Z bwmcaj pzm rq azxcj qrxnhmj; qrhx rx qwsj
        ntrhbzmy z ojzx. Gtzn z qwmj ntwmc qrx rhx cwxab!"
        "Trg br? Trg ezm wn zqqjen ntjp?"
        "Po yjzx Px. Ljmmjn," xjfawjy twb gwqj, \trg ezm orh lj br nwxjbrpj! Orh phbn
        imrg ntzn W zp ntwmiwmc rq twb pzxxowmc rmj rq ntjp."
        "Wb ntzn twb yjbwcm wm bjnnawmc tjxj?"
        "Yjbwcm! Mrmbjmbj, trg ezm orh nzai br! Lhn wn wb sjxo awijao ntzn tj pzo
        qzaa wm arsj gwnt rmj rq ntjp, zmy ntjxjqrxj orh phbn swbwn twp zb brrm zb tj
        erpjb."
        "W bjj mr reezbwrm qrx ntzn. Orh zmy ntj cwxab pzo cr, rx orh pzo bjmy ntjp lo
        ntjpbjasjb, gtwet fjxtzfb gwaa lj bnwaa ljnnjx, qrx zb orh zxj zb tzmybrpj zb
        zmo rq ntjp, Px. Lwmcajo pzo awij orh ntj ljbn rq ntj fzxno."
        "Po yjzx, orh qaznnjx pj. W ejxnzwmao tzsj tzy po btzxj rq ljzhno, lhn W yr
        mrn fxjnjmy nr lj zmontwmc jknxzrxywmzxo mrg. Gtjm z grpzm tzb qwsj cxrgm-hf
        yzhctnjxb, btj rhctn nr cwsj rsjx ntwmiwmc rq tjx rgm ljzhno."
        "Wm bhet ezbjb, z grpzm tzb mrn rqnjm phet ljzhno nr ntwmi rq."
        "Lhn, po yjzx, orh phbn wmyjjy cr zmy bjj Px. Lwmcajo gtjm tj erpjb wmnr ntj
        mjwctlrhxtrry."
        "Wn wb prxj ntzm W jmczcj qrx, W zbbhxj orh."
        "Lhn ermbwyjx orhx yzhctnjxb. Rmao ntwmi gtzn zm jbnzlawbtpjmn wn grhay lj qrx
        rmj rq ntjp. Bwx Gwaawzp zmy Azyo Ahezb zxj yjnjxpwmjy nr cr, pjxjao rm ntzn
        zeerhmn, qrx wm cjmjxza, orh imrg, ntjo swbwn mr mjgerpjxb. Wmyjjy orh phbn cr,
        qrx wn gwaa lj wpfrbbwlaj qrx hb nr swbwn twp wq orh yr mrn."
        "Orh zxj rsjx-bexhfharhb, bhxjao. W yzxj bzo Px. Lwmcajo gwaa lj sjxo cazy nr
        bjj orh; zmy W gwaa bjmy z qjg awmjb lo orh nr zbbhxj twp rq po tjzxno ermbjmn
        nr twb pzxxowmc gtwetjsjx tj etrrbjb rq ntj cwxab; ntrhct W phbn ntxrg wm z crry
        grxy qrx po awnnaj Awvvo."
        "W yjbwxj orh gwaa yr mr bhet ntwmc. Awvvo wb mrn z lwn ljnnjx ntzm ntj rntjxb;
        zmy W zp bhxj btj wb mrn tzaq br tzmybrpj zb Dzmj, mrx tzaq br crry-thprhxjy zb
        Aoywz. Lhn orh zxj zagzob cwswmc tjx ntj fxjqjxjmej."
        "Ntjo tzsj mrmj rq ntjp phet nr xjerppjmy ntjp," xjfawjy tj; "ntjo zxj zaa bwaao
        zmy wcmrxzmn awij rntjx cwxab; lhn Awvvo tzb brpjntwmc prxj rq uhweimjbb ntzm
        tjx bwbnjxb."
        "Px. Ljmmjn, trg ezm orh zlhbj orhx rgm etwayxjm wm bhet z gzo? Orh nzij yjawctn
        wm sjkwmc pj. Orh tzsj mr erpfzbbwrm qrx po frrx mjxsjb."
        "Orh pwbnzij pj, po yjzx. W tzsj z twct xjbfjen qrx orhx mjxsjb. Ntjo zxj po
        ray qxwjmyb. W tzsj tjzxy orh pjmnwrm ntjp gwnt ermbwyjxznwrm ntjbj azbn ngjmno
        ojzxb zn ajzbn."
        "Zt, orh yr mrn imrg gtzn W bhqqjx."
        "Lhn W trfj orh gwaa cjn rsjx wn, zmy awsj nr bjj pzmo orhmc pjm rq qrhx ntrhbzmy
        z ojzx erpj wmnr ntj mjwctlrhxtrry."
        "Wn gwaa lj mr hbj nr hb, wq ngjmno bhet btrhay erpj, bwmej orh gwaa mrn swbwn
        ntjp."
        "Yjfjmy hfrm wn, po yjzx, ntzn gtjm ntjxj zxj ngjmno, W gwaa swbwn ntjp zaa."
        Px. Ljmmjn gzb br ryy z pwknhxj rq uhwei fzxnb, bzxezbnwe thprhx, xjbjxsj, zmy
        ezfxwej, ntzn ntj jkfjxwjmej rq ntxjj-zmy-ngjmno ojzxb tzy ljjm wmbhqqwewjmn nr
        pzij twb gwqj hmyjxbnzmy twb etzxzenjx. Tjx pwmy gzb ajbb ywqqwehan nr yjsjarf.
        Btj gzb z grpzm rq pjzm hmyjxbnzmywmc, awnnaj wmqrxpznwrm, zmy hmejxnzwm njpfjx.
        Gtjm btj gzb ywbermnjmnjy, btj qzmewjy tjxbjaq mjxsrhb. Ntj lhbwmjbb rq tjx awqj
        gzb nr cjn tjx yzhctnjxb pzxxwjy; wnb brazej gzb swbwnwmc zmy mjgb.
    """
    english_letter_list = [ 'E','T','O','N','I','A','S','H','R','U','L',
                            'D','M','Y','F','W','G','C','B','V','P','K',
                            'X','Q','J','Z' ]
    
    message_freq_map = letter_frequency_calculator(encrypted_message)
    substitution_map = get_substitution_map(english_letter_list, list(message_freq_map.keys()))
    print("Dcrypted message:\n{0}".format(decode_message(encrypted_message, substitution_map)))
