import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


sns.set_theme()


#Veri setini yükleme

df = sns.load_dataset("diamonds")
print(df.head())
print(df.describe())

#Keşifsel veri analizi(EDA)

sns.scatterplot(x="carat", y="price", data=df , alpha=0.5)
plt.title("Elmas Karat Ağırlığı ve Fiyat İlişkisi")
plt.xlabel("Carat")
plt.ylabel("Price")
plt.show()

#Lineer Regresyon Modeli

X = df[['carat']]
y = df['price']

model = LinearRegression()
model.fit(X, y)

print(f"Model sabiti (b): {model.intercept_:.2f}")
print(f"Katsayı (w): {model.coef_[0]:.2f}")


#Regresyon Doğrusunun Görselleştirilmesi

sns.regplot(x="carat", y="price", data=df, ci=None, line_kws={"color": "red"})
plt.title(f"price = {model.coef_[0]:.2f} + {model.intercept_:.2f} * carat")
plt.xlabel("Carat")
plt.ylabel("Price")
plt.show()

#Model Performans Değerlenmesi

y_pred = model.predict(X)

mse = mean_squared_error(y, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y, y_pred)

print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")
print(f"R2 Score: {r2:.2f}")

#Yeni Gözlem Üzerinden Tahmin

yeni_elmas = [[1.2]]
tahmini_fiyat = model.predict(yeni_elmas)[0]
print(f"Tahmini Fiyat: {tahmini_fiyat:.2f} $")

