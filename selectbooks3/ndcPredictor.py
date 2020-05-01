import feedparser
import urllib.request
import json
import sqlite3


def ndc_ccode(NDC, ccode):
    for n in NDC:
        if ccode[2:4] == "00":
            if n[:2] == "01" or n[:2] == "02" or n[:2] == "04" or n[:2] == "06" or n[:2] == "07" or \
                    n[:2] == "08":
                return(n)
        elif ccode[2:4] == "01":
            if n[:2] == "03":
                return(n)
        elif ccode[2:4] == "02":
            if n[:2] == "05":
                return(n)
        elif ccode[2:4] == "04":
            if n == "007" or n == "548":
                return(n)
        elif n[2:4] == "10":
            if n[:2] == "10" or n[:2] == "11" or n[:2] == "12" or n[:2] == "13":
                return(n)
        elif ccode[2:4] == "11":
            if n[:2] == "14":
                return(n)
        elif ccode[2:4] == "12":
            if n[:2] == "15":
                return(n)
        elif ccode[2:4] == "14":
            if n[:2] == "16" or n[:2] == "17":
                return(n)
        elif ccode[2:4] == "15":
            if n[:2] == "18":
                return(n)
        elif ccode[2:4] == "16":
            if n[:2] == "19":
                return(n)
        elif ccode[2:4] == "20":
            if n[:2] == "20":
                return(n)
        elif ccode[2:4] == "21":
            if n[:2] == "21":
                return(n)
        elif ccode[2:4] == "22":
            if n[:2] == "22" or n[:2] == "23" or n[:2] == "24" or n[:2] == "25" or n[:2] == "26" or \
                n[:2] == "27":
                return(n)
        elif ccode[2:4] == "23":
            if n[:2] == "28":
                return(n)
        elif ccode[2:4] == "25":
            if n[:2] == "29":
                return(n)
        elif ccode[2:4] == "26":
            if n[:2] == "29":
                return(n)
            if n[:1] == "9" and n[2:] =="5":
                return (n)
        elif ccode[2:4] == "30":
            if n[:2] == "30":
                return(n)
        elif ccode[2:4] == "31":
            if n[:2] == "31" or n[:2] == "39":
                return(n)
        elif ccode[2:4] == "32":
            if n[:2] == "32":
                return(n)
        elif ccode[2:4] == "34":
            if n == "335" or n == "336":
                return(n)
        elif ccode[2:4] == "33":
            if n[:2] == "33" or n[:2] == "34" or n[:2] == "35":
                return(n)
        elif ccode[2:4] == "36":
            if n[:2] == "36":
                return(n)
        elif ccode[2:4] == "37":
            if n[:2] == "37":
                return(n)
        elif ccode[2:4] == "39":
            if n[:2] == "38":
                return(n)
        elif ccode[2:4] == "40":
            if n[:2] == "40":
                return(n)
        elif ccode[2:4] == "41":
            if n[:2] == "41":
                return(n)
        elif ccode[2:4] == "42":
            if n[:2] == "42":
                return(n)
        elif ccode[2:4] == "43":
            if n[:2] == "43":
                return(n)
        elif ccode[2:4] == "44":
            if n[:2] == "44" or n[:2] == "45":
                return(n)
        elif ccode[2:4] == "45":
            if n[:2] == "46" or n[:2] == "47" or n[:2] == "48":
                return(n)
        elif ccode[2:4] == "47":
            if n[:2] == "49":
                return(n)
        elif ccode[2:4] == "50":
            if n[:2] == "50":
                return(n)
        elif ccode[2:4] == "51":
            if n[:2] == "51":
                return(n)
        elif ccode[2:4] == "52":
            if n[:2] == "52":
                return(n)
        elif ccode[2:4] == "53":
            if n[:2] == "53":
                return(n)
        elif ccode[2:4] == "54":
            if n[:2] == "54":
                return(n)
        elif ccode[2:4] == "55":
            if n == "547" or n == "549":
                return(n)
        elif ccode[2:4] == "56":
            if n[:2] == "55":
                return(n)
        elif ccode[2:4] == "57":
            if n[:2] == "56":
                return(n)
        elif ccode[2:4] == "58":
            if n[:2] == "56" or n[:2] == "57" or n[:2] == "58":
                return(n)
        elif ccode[2:4] == "60":
            if n[:2] == "60":
                return(n)
        elif ccode[2:4] == "61":
            if n[:2] == "61" or n[:2] == "62" or n[:2] == "63" or n[:2] == "64" or n[:2] == "65":
                return(n)
        elif ccode[2:4] == "62":
            if n[:2] == "66":
                return(n)
        elif ccode[2:4] == "63":
            if n[:2] == "67":
                return(n)
        elif ccode[2:4] == "65":
            if n[:2] == "68" or n[:2] == "69":
                return(n)
        elif ccode[2:4] == "70":
            if n[:2] == "70":
                return(n)
        elif ccode[2:4] == "71":
            if n[:2] == "71" or n[:2] == "72" or n[:2] == "73":
                return(n)
        elif ccode[2:4] == "72":
            if n[:2] == "74" or n[:2] == "75":
                return(n)
        elif ccode[2:4] == "73":
            if n[:2] == "76":
                return(n)
        elif ccode[2:4] == "74":
            if n[:2] == "77":
                return(n)
        elif ccode[2:4] == "75":
            if n[:2] == "78":
                return(n)
        elif ccode[2:4] == "76":
            if n[:2] == "79" or n == "779":
                return(n)
        elif ccode[2:4] == "77":
            if n[:2] == "59":
                return(n)
        elif ccode[2:4] == "78":
            if n[:1] == "9" and n[2:] =="5":
                return(n)
        elif ccode[2:4] == "79":
            if n == "726":
                return(n)
        elif ccode[2:4] == "80":
            if n[:2] == "80":
                return(n)
        elif ccode[2:4] == "81":
            if n[:2] == "81":
                return(n)
        elif ccode[2:4] == "82":
            if n[:2] == "83":
                return(n)
        elif ccode[2:4] == "84":
            if n[:2] == "84":
                return(n)
        elif ccode[2:4] == "85":
            if n[:2] == "85":
                return(n)
        elif ccode[2:4] == "87":
            if n[:2] == "82" or n[:2] == "86" or n[:2] == "87" or n[:2] == "88" or n[:2] == "89":
                return(n)
        elif ccode[2:4] == "90":
            if n == "90":
                return(n)
        elif ccode[2:4] == "91":
            if n == "910":
                return(n)
        elif ccode[2:4] == "92":
            if n == "911":
                return(n)
        elif ccode[2:4] == "93":
            if n == "912" or n == "913":
                return(n)
        elif ccode[2:4] == "95":
            if n == "914" or n == "915" or n == "916" or n == "917":
                return(n)
        elif ccode[2:4] == "97":
            if n[:1] == "9" and n[1:2] != "1":
                if n[2:] == "2" or n[2:] == "3":
                    return(n)
        elif ccode[2:4] == "98":
            if n[:1] == "9" and n[1:2] != "1":
                if n[2:] != "2" and n[2:] != "3":
                    return(n)
    return(NDC[0])

def ndc_predict(bib):
    url = 'https://lab.ndl.go.jp/ndc/api/predict'
    data = urllib.parse.urlencode({'bib': bib}).encode('utf-8')
    request = urllib.request.Request(url, data)
    response = urllib.request.urlopen(request)
    content = json.loads(response.read().decode('utf8'))

    ndc = []
    #for predict in content:
    if content != None:
        return(content[0]['value'], content[1]['value'], content[2]['value'])

def main():
    conn = sqlite3.connect('C:/Users/出/PycharmProjects/selectbooks3/db.sqlite3')
    c = conn.cursor()
    row_ndc = [["",""]]
    i = 1
    for row in c.execute('SELECT * FROM cms_jpro ORDER BY id'):
        if row[19] == "":
            bib = row[2] + " " + row[4] + " " + row[5] + " " + row[6] + " " + row[13].replace(";", " ")
            NDC = ndc_predict(bib)
            ccode = row[11][0:4]
            cNDC = ndc_ccode(NDC, ccode)
            if ccode[:1] == "8":
                cNDC = "K" + cNDC
            if row_ndc[0] == ["",""]:
                row_ndc[0] = [row[0], cNDC]
            else:
                row_ndc.append([row[0], cNDC])
            print(row[0], cNDC)

    for r in row_ndc:
        c.execute('UPDATE cms_jpro SET NDC = ? WHERE id = ?', (r[1], r[0]))

    conn.commit()
    conn.close()

if __name__ == '__main__':
        main()