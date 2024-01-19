with open('5_1_2_table.html', 'w') as file:
    file.write('<html>')
    file.write('<body>')
    file.write('<table>')
    for row in range(1, 11):
        file.write('<tr>')
        for col in range(1, 11):
            file.write('<td>')
            file.write(f'{row * col}')
            file.write('</td>')
        file.write('</tr>')
    file.write('</table>')
    file.write('</body>')
    file.write('</html>')
