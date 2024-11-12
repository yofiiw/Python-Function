num = int(input('Masukkan Nilai Faktorial :'))
faktorial = 1

for i in range(1, num + 1):
  faktorial *= i

print(f'Nilai dari {num}! adalah {faktorial}')
