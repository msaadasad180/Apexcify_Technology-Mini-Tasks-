import pandas as pd
import matplotlib.pyplot as plt

# Taking hypothetical create sales data

Company_data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    "Sales": [1200, 1500, 1700, 1600, 1800, 2000,
              2200, 2100, 2500, 2700, 3000, 3200]
}

df = pd.DataFrame(Company_data)

# Display Month on the x-axis and Sales on the y-axis

plt.plot(df["Month"], df["Sales"], 
         marker='o',                        # circle for data points
         linestyle='-',                     # connecting dots by line
         color='blue')                      # line color

plt.xlabel("Month")                             # x-axis label
plt.ylabel("Sales ($)")                         # y-axis label
plt.title("Company Monthly Sales Trend")        # chart title

# Step 3: Display the chart

plt.show()
