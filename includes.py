def includes(inputString: str, findString:str) -> bool:
    """
    проверить включает ли в себя inputString findString
    """
    pass

def testIncludes():
    assert includes("012345", "123") == True, 'ошибка теста 1'
    assert includes("012345", "245") == False, 'ошибка теста 2'