name = ["Mirzan","Thuvaraka","Archana","Kamshika","Anojan"]
subject = ["English","Maths","Commerce"]
marks = [
    [89,67,35],
    [67,75,74],
    [54,89,76],
    [87,90,65],
    [87,73,62]
    ]
total = []
average = []

for x in range(len(student)):
    tot = ave = 0
    for y in range(len(subject)):
        tot = tot+marks[x][y]
    