# Data list
random_list = [3.1, 105, 'Hello', 2.7, 737, 'Python', 5.5, 412, 'world', 'AI']

# Filter untuk memisahkan nilai float, int, dan string
filtered_floats = list(filter(lambda x: isinstance(x, float), random_list))
filtered_ints = list(filter(lambda x: isinstance(x, int), random_list))
filtered_strings = list(filter(lambda x: isinstance(x, str), random_list))

# Map untuk memetakan nilai int menjadi satuan, puluhan, dan ratusan
mapped_ints = list(map(lambda x: {'ratusan': x // 100, 'puluhan': (x // 10) % 10, 'satuan': x % 10}, filtered_ints))

# Cetak hasil
print('Data Float:', tuple(filtered_floats))
print('Data Int:')
for item in mapped_ints:
    print(item)
print('Data String:', filtered_strings)
