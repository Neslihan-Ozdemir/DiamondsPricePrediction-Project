# DiamondsPricePrediction-Project
Bu proje, elmasların karat ağırlığına (carat) göre fiyat tahmini yapmak amacıyla geliştirilmiştir. Python kullanılarak veri analizi yapılmış, görselleştirme uygulanmış ve makine öğrenmesi yöntemi olarak Lineer Regresyon modeli kullanılmıştır.

Projede, seaborn kütüphanesinde bulunan hazır diamonds veri seti kullanılmıştır. Bu veri seti içerisinde elmasların karat, fiyat, kesim kalitesi, renk ve saflık gibi çeşitli özellikleri bulunmaktadır. Ancak bu çalışmada yalnızca carat (karat ağırlığı) ile price (fiyat) değişkenleri ele alınmıştır.

Amaç, karat arttıkça fiyatın nasıl değiştiğini analiz etmek ve bu ilişkiyi matematiksel bir modele dönüştürmektir. Öncelikle veri seti incelenmiş, ardından scatter plot ile değişkenler arasındaki ilişki görselleştirilmiştir. Daha sonra Scikit-learn kullanılarak doğrusal regresyon modeli eğitilmiş ve regresyon doğrusu grafik üzerinde gösterilmiştir.

Modelin başarısını değerlendirmek için:

Mean Squared Error (MSE)
Root Mean Squared Error (RMSE)
R² Score

gibi performans metrikleri hesaplanmıştır.

Son olarak, yeni bir gözlem olarak 1.2 karatlık bir elmas için tahmini fiyat hesaplanmıştır.

Bu proje özellikle veri bilimi ve makine öğrenmesine yeni başlayanlar için temel seviyede anlaşılır bir regresyon örneğidir. Veri analizi, model kurma, görselleştirme ve tahmin süreçlerini bir arada göstermektedir.
