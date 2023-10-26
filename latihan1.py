def convert_to_minutes(data):
    output_data = []
    for item in data:
        # Pisahkan string menjadi kata-kata
        words = item.split()

        # Konversi minggu, hari, jam, dan menit menjadi menit
        minggu = int(words[0])
        hari = int(words[2])
        jam = int(words[4])
        menit = int(words[6])

        total_menit = (minggu * 7 * 24 * 60) + (hari * 24 * 60) + (jam * 60) + menit
        output_data.append(total_menit)

    return output_data


data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

output_data = convert_to_minutes(data)
print("Output Data = ")
print(output_data)

