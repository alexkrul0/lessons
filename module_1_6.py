my_dict = {'Alex' : 1972, 'Mike' : 1985, 'Mary' : 1995, 'Fredy' : 2001}
print('Dict:', my_dict)
print('Existing value:', my_dict['Mike'])
print('Not existing value:', my_dict.get('Tom'))
my_dict.update({'Ann' : 2004, 'Tony' : 2012})
a = my_dict.pop('Ann')
print('Deleted value:', a)
print('Modified dictionary:', my_dict)
print(" ")

my_set = {1, 'text', 0.5, 1, 2, 5, True, False, 2}
print('Set:', my_set)
my_set.add(0.7)
my_set.add(7)
my_set.remove(5)
print('Modified set:', my_set)