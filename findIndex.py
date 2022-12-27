def findIndex(inputString:str, findString:str) -> int:
    """
    находит индекс первого вхождения findString в inputString
    или -1 если не найдено
    """
    pass

def testFindIndex():
    assert findIndex("хахаха", "ха") == 0, 'ошибка теста 1'
    assert findIndex("012345678", "456") == 4, 'ошибка теста 2'
    assert findIndex("012345678", "637") == -1, 'ошибка теста 3'