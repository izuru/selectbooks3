import feedparser
import urllib.request
import json
import sqlite3


def ccodechange(ccode):
    strCcode = ""
    if ccode == "":
        return("")

    if ccode[0] == "0":
        strCcode = "一般-"
    elif ccode[0] == "1":
        strCcode = "教養-"
    elif ccode[0] == "2":
        strCcode = "実用-"
    elif ccode[0] == "3":
        strCcode = "専門-"
    elif ccode[0] == "4":
        strCcode = "検定教科書-"
    elif ccode[0] == "5":
        strCcode = "婦人-"
    elif ccode[0] == "6":
        strCcode = "学参1(中･小)-"
    elif ccode[0] == "7":
        strCcode = "学参2(高校)"
    elif ccode[0] == "8":
        strCcode = "児童-"
    elif ccode[0] == "9":
        strCcode = "雑誌扱-"

    if ccode[1] == "0":
        strCcode = strCcode + "単行本-"
    elif ccode[1] == "1":
        strCcode = strCcode + "文庫-"
    elif ccode[1] == "2":
        strCcode = strCcode + "新書-"
    elif ccode[1] == "3":
        strCcode = strCcode + "全集･双書-"
    elif ccode[1] == "4":
        strCcode = strCcode + "ムック･その他-"
    elif ccode[1] == "5":
        strCcode = strCcode + "辞典･事典-"
    elif ccode[1] == "6":
        strCcode = strCcode + "図鑑-"
    elif ccode[1] == "7":
        strCcode = strCcode + "絵本"
    elif ccode[1] == "8":
        strCcode = strCcode + "磁性媒体など-"
    elif ccode[1] == "9":
        strCcode = strCcode + "コミックス-"

    if ccode[2:4] == "00":
        strCcode = strCcode + "総記"
    elif ccode[2:4] == "01":
        strCcode = strCcode + "百科事典"
    elif ccode[2:4] == "02":
        strCcode = strCcode + "年鑑･雑誌"
    elif ccode[2:4] == "04":
        strCcode = strCcode + "情報科学"
    elif ccode[2:4] == "10":
        strCcode = strCcode + "哲学"
    elif ccode[2:4] == "11":
        strCcode = strCcode + "心理(学)"
    elif ccode[2:4] == "12":
        strCcode = strCcode + "倫理(学)"
    elif ccode[2:4] == "14":
        strCcode = strCcode + "宗教"
    elif ccode[2:4] == "15":
        strCcode = strCcode + "仏教"
    elif ccode[2:4] == "16":
        strCcode = strCcode + "キリスト教"
    elif ccode[2:4] == "20":
        strCcode = strCcode + "歴史総記"
    elif ccode[2:4] == "21":
        strCcode = strCcode + "日本歴史"
    elif ccode[2:4] == "22":
        strCcode = strCcode + "外国歴史"
    elif ccode[2:4] == "23":
        strCcode = strCcode + "伝記･系譜"
    elif ccode[2:4] == "25":
        strCcode = strCcode + "地理"
    elif ccode[2:4] == "26":
        strCcode = strCcode + "旅行"
    elif ccode[2:4] == "30":
        strCcode = strCcode + "社会科学総記"
    elif ccode[2:4] == "31":
        strCcode = strCcode + "政治(国防･軍事含む)"
    elif ccode[2:4] == "32":
        strCcode = strCcode + "法律"
    elif ccode[2:4] == "33":
        strCcode = strCcode + "経済･財政･統計"
    elif ccode[2:4] == "34":
        strCcode = strCcode + "経営"
    elif ccode[2:4] == "36":
        strCcode = strCcode + "社会"
    elif ccode[2:4] == "37":
        strCcode = strCcode + "教育"
    elif ccode[2:4] == "39":
        strCcode = strCcode + "民俗･風習"
    elif ccode[2:4] == "40":
        strCcode = strCcode + "自然科学総記"
    elif ccode[2:4] == "41":
        strCcode = strCcode + "数学"
    elif ccode[2:4] == "42":
        strCcode = strCcode + "物理学"
    elif ccode[2:4] == "43":
        strCcode = strCcode + "化学"
    elif ccode[2:4] == "44":
        strCcode = strCcode + "天文･地学"
    elif ccode[2:4] == "45":
        strCcode = strCcode + "生物学"
    elif ccode[2:4] == "47":
        strCcode = strCcode + "医学･歯学･薬学"
    elif ccode[2:4] == "50":
        strCcode = strCcode + "工学･工学総記"
    elif ccode[2:4] == "51":
        strCcode = strCcode + "土木"
    elif ccode[2:4] == "52":
        strCcode = strCcode + "建築"
    elif ccode[2:4] == "53":
        strCcode = strCcode + "機械"
    elif ccode[2:4] == "54":
        strCcode = strCcode + "電気"
    elif ccode[2:4] == "55":
        strCcode = strCcode + "電子通信"
    elif ccode[2:4] == "56":
        strCcode = strCcode + "海事･兵器"
    elif ccode[2:4] == "57":
        strCcode = strCcode + "採鉱･冶金"
    elif ccode[2:4] == "58":
        strCcode = strCcode + "その他の工業"
    elif ccode[2:4] == "60":
        strCcode = strCcode + "産業総記"
    elif ccode[2:4] == "61":
        strCcode = strCcode + "農林業"
    elif ccode[2:4] == "62":
        strCcode = strCcode + "水産業"
    elif ccode[2:4] == "63":
        strCcode = strCcode + "商業"
    elif ccode[2:4] == "65":
        strCcode = strCcode + "交通･通信"
    elif ccode[2:4] == "70":
        strCcode = strCcode + "芸術総記"
    elif ccode[2:4] == "71":
        strCcode = strCcode + "絵画･彫刻"
    elif ccode[2:4] == "72":
        strCcode = strCcode + "写真･工芸"
    elif ccode[2:4] == "73":
        strCcode = strCcode + "音楽･舞踊"
    elif ccode[2:4] == "74":
        strCcode = strCcode + "演劇･映画"
    elif ccode[2:4] == "75":
        strCcode = strCcode + "体育･スポーツ"
    elif ccode[2:4] == "76":
        strCcode = strCcode + "諸芸･娯楽"
    elif ccode[2:4] == "77":
        strCcode = strCcode + "家事"
    elif ccode[2:4] == "78":
        strCcode = strCcode + "生活"
    elif ccode[2:4] == "79":
        strCcode = strCcode + "コミックス･劇画"
    elif ccode[2:4] == "80":
        strCcode = strCcode + "語学総記"
    elif ccode[2:4] == "81":
        strCcode = strCcode + "日本語"
    elif ccode[2:4] == "82":
        strCcode = strCcode + "英(米)語"
    elif ccode[2:4] == "84":
        strCcode = strCcode + "ドイツ語"
    elif ccode[2:4] == "85":
        strCcode = strCcode + "フランス語"
    elif ccode[2:4] == "87":
        strCcode = strCcode + "各国語"
    elif ccode[2:4] == "90":
        strCcode = strCcode + "文学総記"
    elif ccode[2:4] == "91":
        strCcode = strCcode + "日本文学総記"
    elif ccode[2:4] == "92":
        strCcode = strCcode + "日本文学詩歌"
    elif ccode[2:4] == "93":
        strCcode = strCcode + "日本文学小説･物語"
    elif ccode[2:4] == "95":
        strCcode = strCcode + "日本文学評論･随筆･その他"
    elif ccode[2:4] == "97":
        strCcode = strCcode + "外国文学小説"
    elif ccode[2:4] == "98":
        strCcode = strCcode + "外国文学その他"

    return(ccode + ":" + strCcode)

def genrechange(gc):
    if gc == "01":
        return("文芸")
    elif gc == "02":
        return("新書")
    elif gc == "03":
        return("社会一般")
    elif gc == "04":
        return("資格･試験")
    elif gc == "05":
        return("ビジネス")
    elif gc == "06":
        return("スポーツ･健康")
    elif gc == "07":
        return("趣味･実用")
    elif gc == "09":
        return("ゲーム")
    elif gc == "10":
        return("芸能･タレント")
    elif gc == "11":
        return("テレビ･映画化")
    elif gc == "12":
        return("芸術")
    elif gc == "13":
        return("哲学･宗教")
    elif gc == "14":
        return("歴史･地理")
    elif gc == "15":
        return("社会科学")
    elif gc == "16":
        return("教育")
    elif gc == "17":
        return("自然科学")
    elif gc == "18":
        return("医学")
    elif gc == "19":
        return("工業･工学")
    elif gc == "20":
        return("コンピュータ")
    elif gc == "21":
        return("語学･辞事典")
    elif gc == "22":
        return("学参")
    elif gc == "23":
        return("児童図書")
    elif gc == "24":
        return("ヤングアダルト")
    elif gc == "29":
        return("新刊セット")
    elif gc == "30":
        return("全集")
    elif gc == "31":
        return("文庫")
    elif gc == "36":
        return("コミック文庫")
    elif gc == "41":
        return("コミックス(欠番扱)")
    elif gc == "42":
        return("コミックス(雑誌扱)")
    elif gc == "43":
        return("コミックス(書籍)")
    elif gc == "44":
        return("コミックス(廉価版)")
    elif gc == "51":
        return("ムック")
    else:
        return("")

def formchange(PF):
    if PF == "B108":
        return("A5")
    elif PF == "B109":
        return("B5")
    elif PF == "B110":
        return("B6")
    elif PF == "B111":
        return("文庫")
    elif PF == "B112":
        return ("新書")
    elif PF == "B119":
        return ("46判")
    elif PF == "B120":
        return ("46変形")
    elif PF == "B121":
        return("A4")
    elif PF == "B122":
        return("A4変形")
    elif PF == "B123":
        return("A5変形")
    elif PF == "B124":
        return ("B5変形")
    elif PF == "B125":
        return ("B6変形")
    elif PF == "B126":
        return ("AB判")
    elif PF == "B127":
        return ("B7")
    elif PF == "B128":
        return ("菊判")
    elif PF == "B129":
        return ("菊変形")
    elif PF == "B130":
        return ("B4")
    else:
        return("")

def openBD(contentBD):
    ISBN = ProductForm = Volume = SeriesTitle = SeriesNumber = Subtitle = ContributorName = ""
    ContributorNote = extent = Ccode = Genrecode = Keywords = dcsDescription = ""
    dcDescription = ToC = dcFeature = Publisher = Price = impub = NDC = ""
    Series = []
    Contributor = []
    Audience = []

    if contentBD['onix']['DescriptiveDetail'].get('ProductFormDetail') != None:
        ProductForm = contentBD['onix']['DescriptiveDetail']['ProductFormDetail']
    if contentBD['onix']['DescriptiveDetail'].get('Collection') != None:
        if contentBD['onix']['DescriptiveDetail']['Collection'].get('TitleDetail') != None:
            if contentBD['onix']['DescriptiveDetail']['Collection']['TitleDetail']\
                    .get('TitleElement') != None:
                iSeries = contentBD['onix']['DescriptiveDetail']['Collection']['TitleDetail']\
                    ['TitleElement']
                for s in iSeries:
                    if s['TitleText'].get('content') != None:
                        SeriesTitle = s['TitleText']['content']
                        if s.get('PartNumber') != None:
                            SeriesNumber = s['PartNumber']
                        Series.append([SeriesTitle, SeriesNumber])

    Title = contentBD['onix']['DescriptiveDetail']['TitleDetail']['TitleElement']\
        ['TitleText']['content']
    if contentBD['onix']['DescriptiveDetail']['TitleDetail']['TitleElement'].get('PartNumber') != None:
        Volume = contentBD['onix']['DescriptiveDetail']['TitleDetail']['TitleElement']['PartNumber']
    if contentBD['onix']['DescriptiveDetail']['TitleDetail']['TitleElement'].get('Subtitle') != None:
        Subtitle = contentBD['onix']['DescriptiveDetail']['TitleDetail']['TitleElement'] \
            ['Subtitle']['content']
    if contentBD['onix']['DescriptiveDetail'].get('Contributor') != None:
        icontributor = contentBD['onix']['DescriptiveDetail']['Contributor']
        for cont in icontributor:
            if cont.get('ContributorRole') != None:
                ContributorRole = []
                for icont in cont.get('ContributorRole'):
                    ContributorRole.append(icont)
            ContributorName = cont['PersonName']['content']
            ContributorNote = cont.get('BiographicalNote')
            Contributor.append([ContributorName, ContributorRole, ContributorNote])
    simpleContributor = contentBD['summary']['author']
    if contentBD['onix']['DescriptiveDetail'].get('Extent') != None:
        iextent = contentBD['onix']['DescriptiveDetail']['Extent']
        extent = ""
        for ex in iextent:
            if extent != "":
                extent = extent + ", "
            extent = extent + ex['ExtentValue'] + "p"
    if contentBD['onix']['DescriptiveDetail'].get('Subject') != None:
        for isubject in contentBD['onix']['DescriptiveDetail']['Subject']:
            if isubject['SubjectSchemeIdentifier'] == "78":
                Ccode = isubject['SubjectCode']
            elif isubject['SubjectSchemeIdentifier'] == "79":
                Genrecode = isubject['SubjectCode']
            elif isubject['SubjectSchemeIdentifier'] == "20":
                Keywords = isubject['SubjectHeadingText']
    if contentBD['onix']['DescriptiveDetail'].get('Audience') != None:
        Audience = []
        for iaudience in contentBD['onix']['DescriptiveDetail']['Audience']:
            if iaudience['AudienceCodeType'] == "22":
                AudienceCodeType = "一般"
                if iaudience['AudienceCodeValue'] == "00":
                    AudienceCodeValue = "指定なし"
                elif iaudience['AudienceCodeValue'] == "01":
                    AudienceCodeValue = "成人指定"
                elif iaudience['AudienceCodeValue'] == "02":
                    AudienceCodeValue = "成人向け"
                elif iaudience['AudienceCodeValue'] == "03":
                    AudienceCodeValue = "成人向け(性)"
                elif iaudience['AudienceCodeValue'] == "04":
                    AudienceCodeValue = "成人向け(暴力)"
                elif iaudience['AudienceCodeValue'] == "05":
                    AudienceCodeValue = "成人向け(薬物)"
                elif iaudience['AudienceCodeValue'] == "06":
                    AudienceCodeValue = "成人向け(言語)"
            elif iaudience['AudienceCodeType'] == "21":
                AudienceCodeType = "児童"
                if iaudience['AudienceCodeValue'] == "01":
                    AudienceCodeValue = "0～2歳"
                elif iaudience['AudienceCodeValue'] == "02":
                    AudienceCodeValue = "3～5歳"
                elif iaudience['AudienceCodeValue'] == "03":
                    AudienceCodeValue = "小学低学年"
                elif iaudience['AudienceCodeValue'] == "04":
                    AudienceCodeValue = "小学中学年"
                elif iaudience['AudienceCodeValue'] == "05":
                    AudienceCodeValue = "小学高学年"
                elif iaudience['AudienceCodeValue'] == "06":
                    AudienceCodeValue = "小学全般"
                elif iaudience['AudienceCodeValue'] == "07":
                    AudienceCodeValue = "中学以上"
                elif iaudience['AudienceCodeValue'] == "08":
                    AudienceCodeValue = "高校"
            Audience.append(AudienceCodeType + "-" + AudienceCodeValue)
    if contentBD['onix'].get('CollateralDetail') != None:
        if contentBD['onix']['CollateralDetail'].get('TextContent') != None:
            for idc in contentBD['onix']['CollateralDetail']['TextContent']:
                if idc['TextType'] == "02":
                    dcsDescription = idc['Text']
                elif idc['TextType'] == "03":
                    dcDescription = idc['Text']
                elif idc['TextType'] == "04":
                    ToC = idc['Text']
                elif idc['TextType'] == "11":
                    dcFeature = idc['Text']
    Imprint = contentBD['onix']['PublishingDetail']['Imprint']['ImprintName']
    if contentBD['onix']['PublishingDetail'].get('Publisher') != None:
        Publisher = contentBD['onix']['PublishingDetail']['Publisher']['PublisherName']
        impub = Imprint + " ; " + Publisher
    else:
        impub = Imprint
    if contentBD['onix']['PublishingDetail'].get('PublishingDate') != None:
        for date in contentBD['onix']['PublishingDetail']['PublishingDate']:
            if date['PublishingDateRole'] == "01":
                PublishingDate = date['Date']
                break
    if contentBD['onix']['ProductSupply']['SupplyDetail'].get('Price') != None:
        Price = contentBD['onix']['ProductSupply']['SupplyDetail']['Price'][0]['PriceAmount']
    datemodified = contentBD['hanmoto']['datemodified']
    ISBN = contentBD['summary']['isbn']

    conNoteList = []
    for con in Contributor:
        if con[2] != "":
            if con[2] != None:
                conNoteList.append(con[2])

    if dcDescription == "":
        if dcsDescription != "":
            description = dcsDescription
        else:
            description = ""
    else:
        description = dcDescription

    if extent == "":
        if ProductForm != "":
            exform = formchange(ProductForm)
        else:
            exform = ""
    else:
        if ProductForm != "":
            exform = formchange(ProductForm) + " ; " + extent
        else:
            exform = extent

    if Ccode[1:2] == "7":
        NDC = "E"
    elif Ccode[2:4] == "79" or Ccode[2:4] == "92":
        if Ccode[0:1] == "8":
            NDC = "K"
        if Ccode[2:4] == "79":
            NDC = NDC + "726"
        elif Ccode[2:4] == "92":
            NDC = NDC + "911"

    return(["", ISBN, Title, Volume, Subtitle, serieslist(Series), simpleContributor, \
            impub, PublishingDate, Price, exform, ccodechange(Ccode), genrechange(Genrecode), \
            Keywords, recordList(Audience), recordList(conNoteList),description, ToC, datemodified, \
            NDC])

    #print(ProductForm, Series, Title, Volume, Subtitle, extent, simpleContributor)
    #print(Contributor)
    #print(Ccode, Genrecode, Keywords, Audience, Imprint, Publisher, PublishingDate, Price + "円")
    #print(dcsDescription)
    #print(dcDescription.replace("\n", ""), dcFeature)
    #print(ToC.replace("\n", ""))
    #print(datemodified)

def recordList(record):
    slist = ""
    for r in record:
        if slist != "":
            slist = slist + " ; " + r
        elif r != None:
            slist = r
    return(slist)

def serieslist(record):
    slist = ""
    for r in record:
        if slist != "":
            slist = slist + " ; " + r[0]
            if r[1] != "":
                slist = slist + " , " + r[1]
        else:
            slist = r[0]
            if r[1] != "":
                slist = slist + " , " + r[1]
    return (slist)

def isbn_get():
    d = feedparser.parse('https://www.hanmoto.com/ci/bd/search/sdate/today/edate/today/hdt/' + \
                         '%E6%9C%AC%E6%97%A5%E7%99%BA%E5%A3%B2%E3%81%AE%E6%9C%AC/order/desc/vw/rss20')

    ISBN = ""
    for entry in d.entries:
        if ISBN == "":
            ISBN = entry.link[-13:]
        else:
            ISBN = ISBN + "," + entry.link[-13:]
    return(ISBN)

def main():
    conn = sqlite3.connect('C:/Users/出/PycharmProjects/selectbooks3/db.sqlite3')
    c = conn.cursor()
    c.execute('DELETE FROM cms_jpro')

    ISBN = isbn_get()
    print(ISBN)
    url = 'https://api.openbd.jp/v1/get?isbn=' + ISBN + '&pretty'
    response = urllib.request.urlopen(url)
    content = json.loads(response.read().decode('utf8'))
    i = 1
    for bd in content:
        if bd != None:
            recordlist = openBD(bd)
            recordlist[0] = i
            if recordlist[1] != "":
                print(recordlist)
                c.execute("INSERT INTO cms_jpro VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", \
                          recordlist)
                i += 1

    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()

