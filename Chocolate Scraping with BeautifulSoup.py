import codecademylib3_seaborn
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

webpage = requests.get("https://content.codecademy.com/courses/beautifulsoup/cacao/index.html")
soup = BeautifulSoup(webpage.content, "html.parser")
#print(soup)

bar_rating = soup.find_all(attrs={"class": "Rating"})
ratings = []
for rating in bar_rating[1:]:
  rating_text = rating.get_text()
  ratings.append(float(rating_text))
#print(ratings)

#plt.hist(ratings)
#plt.show()

comp_tags = soup.select(".Company")
companies = []
for comp in comp_tags[1:]:
  companies.append(comp.get_text())
#print(companies)

cocoa_lvl = soup.select(".CocoaPercent")
cocoa_percent = []
for cocoa in cocoa_lvl[1:]:
  percent = (cocoa.get_text().strip('%'))
  cocoa_percent.append(float(percent))
#print(cocoa_percent)

dcomp = {"Companies": companies, "Ratings": ratings, "CocoaPercentage": cocoa_percent}
cocoa_df = pd.DataFrame.from_dict(dcomp)
mean_val = cocoa_df.groupby("Companies").Ratings.mean()
ten_best = mean_val.nlargest(10)
#print(ten_best)

plt.clf()
plt.scatter(cocoa_df.CocoaPercentage, cocoa_df.Ratings)
z = np.polyfit(cocoa_df.CocoaPercentage, cocoa_df.Ratings, 1)
line_function = np.poly1d(z)
plt.plot(cocoa_df.CocoaPercentage, line_function(cocoa_df.CocoaPercentage), "r--")
plt.show()