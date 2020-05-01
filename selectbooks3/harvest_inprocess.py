import requests
import sqlite3
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup as bs4
import re


def get_xml(url):
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    bibxml = response.text
    return (ET.fromstring(bibxml))

def get_xml_soup(url):
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    bibxml = response.text
    return (bs4(bibxml, 'lxml-xml'))

def jan_to_asin(jan13):
    s = str(jan13)[3:12]
    a = 10
    c = 0

    for i in range(0, len(s)):
        c += int(s[i]) * (a - i)

    d = c % 11
    d = 11 - d
    if d == 10:
        d = "X"
    return str(s) + str(d)

def parse_record_soup(record):

    recordlist = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]

    if record.header.has_attr("status"):
        if record.header["status"] == 'deleted':
            return (recordlist)

    if record.materialType.string != "図書":
        return (recordlist)

    ISBN = ""
    ASIN = ""
    NDLBibID = ""
    stitle = ""
    svolume = ""
    sseriesTitle = ""
    screator = ""
    spub = ""
    spublicationPlace = ""
    sdate = ""
    NDC = ""
    ssubject = ""
    sprice = ""
    sextent = ""
    sdescription = ""
    spartTC = ""

    for identifier in record.find_all("identifier"):
        if identifier.has_attr("xsi:type"):
            if identifier["xsi:type"] == 'dcndl:ISBN':
                ISBN = recordcheck(ISBN, identifier.string)
                ASIN = jan_to_asin(identifier.string.replace("-", ""))
            elif identifier["xsi:type"] == 'dcndl:NDLBibID':
                NDLBibID = identifier.string

    for title in record.find_all('title'):
        stitle = recordcheck(stitle, title.string)

    for volume in record.find_all('volume'):
        svolume = recordcheck(svolume, volume.string)

    for seriesTitle in record.find_all('seriesTitle'):
        sseriesTitle = recordcheck(sseriesTitle, seriesTitle.string)

    for creator in record.find_all('creator'):
        if re.search(r'[^,] [^a-zA-Z]+', creator.string):
            screator = recordcheck(screator, creator.string)

    for publisher in record.find_all('publisher'):
        spub = recordcheck(spub, publisher.string)

    spublicationPlace = record.publicationPlace.string

    for date in record.find_all('date'):
        sdate = recordcheck(sdate, date.string)

    for subject in record.find_all('subject'):
        if subject.has_attr('xsi:type'):
            if subject['xsi:type'] == 'dcndl:NDC10':
                NDC = subject.string
            elif subject['xsi:type'] == 'dcndl:NDC9':
                if len(NDC) == 0:
                    NDC = subject.string
        else:
            ssubject = recordcheck(ssubject, subject.string)

    for price in record.find_all('price'):
        sprice = recordcheck(sprice, price.string)

    for extent in record.find_all('extent'):
        sextent = recordcheck(sextent, extent.string)

    for description in record.find_all('description'):
        if description.string != "NDC（9版）はNDC（10版）を自動変換した値である。":
            sdescription = recordcheck(sdescription, description.string)

    pC = 0
    for partTC in record.find_all(re.compile('part.*')):
        if len(spartTC) == 0:
            spartTC = "「" + partTC.string + "」"
        elif partTC.name =='partTitle':
            spartTC = spartTC + ";「" + partTC.string + "」"
        elif partTC.name == 'partCreator':
            spartTC = spartTC + " " + partTC.string
            pC += 1

    if pC == 0:
        spartTC = spartTC.replace("「", "")
        spartTC = spartTC.replace("」", "")

    recordlist = ["", ISBN, ASIN, NDLBibID, stitle, svolume, sseriesTitle, screator, spub, \
                  spublicationPlace, sdate, NDC, ssubject, sprice, sextent, sdescription, spartTC]
    print(recordlist)
    return (recordlist)

def recordcheck(record1, record2):
    if len(record1) == 0:
        return(record2)
    else:
        return(record1 + "; " + record2)

def getbibdata(root_soup, c, i):
    # us = '{http://www.openarchives.org/OAI/2.0/}'
    # for record in root_s.iter(us + 'record')
    for record in root_soup.find_all('record'):
        recordlist = parse_record_soup(record)
        recordlist[0] = i
        if recordlist[1] != "":
            c.execute("INSERT INTO cms_book VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", recordlist)
            i += 1
    return(i)

def main():
    date = '2020-04-23'

    conn = sqlite3.connect('C:/Users/出/PycharmProjects/selectbooks3/db.sqlite3')
    c = conn.cursor()
    c.execute('DELETE FROM cms_book')

    url_s = 'http://iss.ndl.go.jp/api/oaipmh?verb=ListRecords&metadataPrefix=dcndl_simple&from=' + \
            date + '&set=iss-ndl-opac-inprocess'
    # root_s = get_xml(url_s)
    root_soup = get_xml_soup(url_s)
    i = getbibdata(root_soup, c, 1)

    while root_soup.resumptionToken.string != None:
        url_s = 'http://iss.ndl.go.jp/api/oaipmh?verb=ListRecords&resumptionToken=' + \
            root_soup.resumptionToken.string
        print(url_s)
        root_soup = get_xml_soup(url_s)
        i = getbibdata(root_soup, c, i)

    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()
