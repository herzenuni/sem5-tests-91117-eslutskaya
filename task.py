list1 = list('123456')
list2 = list('abcd')
#создаем списки разной длины

def dictionaryFromKeys(k, v):
    try:
        res = dict.fromkeys(k, None)
        res.update(zip(k, v))
    except TypeError:
        res = 'TypeError'
    return res

result = dictionaryFromKeys(list1, list2)
#получаме словарь
print (result)


#юни тест
if __name__ == '__main__':
    import unittest

    class TestFactorialMethods(unittest.TestCase):

#тестироание при правильном вводе

        def test_normal_values(self):
            self.assertEqual(dictionaryFromKeys([1,2,3, 4],[2,3,4,5]),{1: 2, 2: 3, 3: 4, 4: 5})
            self.assertEqual(dictionaryFromKeys([1, 2, 3, 4, 5],[2,3,4,5]),{1: 2, 2: 3, 3: 4, 4: 5, 5: None})
#если вместо списка ввести цифру
        def test_vals_float_type(self):
            self.assertTrue(dictionaryFromKeys(3,4) is None)
            self.assertTrue(dictionaryFromKeys(5,[6]) is None)
#если ввести булевы зачения
        def test_vals_bool_type(self):
            self.assertIsNone(dictionaryFromKeys(True,True), None)
#если ввести отрецательные числа

        def test_negative_values(self):
            self.assertEqual(dictionaryFromKeys(-3,-4), None)
            self.assertEqual(dictionaryFromKeys(-5,-6), None)



 
