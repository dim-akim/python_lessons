with open('5_1_3_table.html', 'w') as file:
    file.write('<html>')
    file.write('<body>')
    file.write('<table>')
    for row in range(1, 11):
        file.write('<tr>')
        for col in range(1, 11):
            file.write('<td>')
            file.write(f'<a href="http://{row * col}.ru">{row * col}</a>')
            file.write('</td>')
        file.write('</tr>')
    file.write('</table>')
    file.write('</body>')
    file.write('</html>')
