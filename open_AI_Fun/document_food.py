import pdfkit

food_items = ["Pizza", "Burger", "Sandwich", "Pasta", "French Fries", "Salad"] 

# Create a html file
html_file = open("menu.html", "w")

# Write the html code
html_file.write("<html>\n")
html_file.write("<body>\n")
html_file.write("<h1>Menu</h1>\n")
html_file.write("<ul>\n")

for item in food_items:
    html_file.write("<li>" + item + "</li>\n")

html_file.write("</ul>\n")
html_file.write("</body>\n")
html_file.write("</html>\n")

# Close the file
html_file.close()

# Convert the html file to pdf
pdfkit.from_file("menu.html", "menu.pdf")