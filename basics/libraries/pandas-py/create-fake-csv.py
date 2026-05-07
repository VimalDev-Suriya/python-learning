from faker import Faker
import pandas as pd

fake = Faker()
data = []
null_chance = 0.2

for _ in range(40):
    data.append({
        "Username": fake.user_name(),
        "Phone": fake.phone_number(),
        "Company": fake.company(),
        "Email": fake.email()
    })

# We need to create the data frame, so on that occasion we can work on the analysis.
# without creating the dataframe we cannot analyze the data.
df = pd.DataFrame(data);

# Picking up few of the random values and setting them as null
df.loc[df.sample(frac=null_chance).index, "Company"] = ""
df.loc[df.sample(frac=null_chance).index, "Email"] = ""

# Creating new CSV file with the provided path.
df.to_csv("./basics/libraries/pandas/employee.csv", index=False)
