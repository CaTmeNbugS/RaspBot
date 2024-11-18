from typing import Union
from bs4    import BeautifulSoup

import requests
import json

class Shedule:
        
    def __init__(self, date: str, userType: str, userGroup: str) -> None:

        self.date:      str = date
        self.userType:  str = userType
        self.userGroup: str = userGroup.upper()

    def isAvailable(self) -> bool:

        url:      str = 'https://www.uc.osu.ru/chek_file.php'
        response: str = requests.request('POST', url, headers={}, data={'data': self.date}, files=[]).text

        return True if response == "ok" else False
    
    def getUserGroupId(self) -> str:
            
        url:      str = 'https://www.uc.osu.ru/back_parametr.php'
        response: str = requests.request('POST', url, headers={}, data={'data': self.date, 'type_id': self.userType}, files=[]).text

        for key, value in json.loads(response).items():

            if(value.upper() == self.userGroup):
                return str(key)

        return 'err'
    
    def getDictShedule(self) -> list[dict[str, str]]:   

        url:      str = 'https://www.uc.osu.ru/generate_data.php'
        response: str = requests.request('POST', url, headers={}, data={'data': self.date, 'type': self.userType, 'id': self.getUserGroupId()}, files=[]).text

        isStudentShedule:        bool = True if BeautifulSoup(response, "html.parser").find('td').text == '№'else False
        coupleMask:    dict[int, str] = { 0: 'number', 1: 'subject', 2: 'classroom' }
        couples: list[dict[str, str]] = []

        lines = BeautifulSoup(response, 'html.parser').find_all('tr')

        for i, line in enumerate(lines):
            
            cells = line.find_all('td')

            if (i % 2 == int(isStudentShedule)):

                couple = { 'number': '', 'subject': '', 'classroom': '', 'teacher': '' }

                for j, cell in enumerate(cells):

                    couple[coupleMask[j]] = cell.text

                couples.append(couple)

            elif (i % 2 == int(not isStudentShedule)) & (i > int(isStudentShedule)):

                couples[int(i / 2) - int(isStudentShedule)]['teacher'] = cells[0].text

        return couples
    
    def getMsgShedule(self) -> str:

        try:

            if self.isAvailable():

                sheduleDict: list[dict[str, str]] = self.getDictShedule()

                lineLengthList: list[int] = []
                maxLineLength:        int = 0
                sheduleMsg:           str = f'<blockquote><b><i> {self.userGroup} | {self.date}</i></b></blockquote>\n'

                for couple in sheduleDict:

                    lineLength: int = len(couple['subject']) + len(couple['classroom'].replace(' ', ''))
                    lineLengthList.append(lineLength)

                    if lineLength > maxLineLength:
                        maxLineLength = lineLength

                for i, couple in enumerate(sheduleDict):

                    sheduleMsg += f'<pre> {couple['number']} | {couple['subject']}{(maxLineLength - lineLengthList[i] + 1) * ' '}{couple['classroom'].replace(' ', '')}{(' ' + couple['teacher'] if self.userType == '2' else '')}</pre>\n'
    
                return sheduleMsg

            else:

                return 'Я ничего не нашел 🤷‍♂️'
        
        except:

            return 'Я ничего не нашел 🤷‍♂️'
    
def findGroup(type: str, group: str) -> Union[str, bool]:

    url:      str = 'https://www.uc.osu.ru/back_parametr.php'
    response: str = requests.request('POST', url, headers={}, data={'data': '02-09-2024', 'type_id': type}, files=[]).text

    for key, value in json.loads(response).items():

        if(value.upper().find(group.upper()) != -1):

            return value

    return False

