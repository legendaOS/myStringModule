def split(inputString: str, startIndex:int, endIndex:int, step:int) -> str:
    """
        отрезает кусок строки начиная с startIndex заканчивая 
        endInex(не включая его) с шагом в step символов
    """
    pass

def testSplit():
    assert split("0123456789", 3,7,1) == "3456", "ошибка теста 1"
    assert split("0123456789", 3,10,2) == "3579", "ошибка теста 2"