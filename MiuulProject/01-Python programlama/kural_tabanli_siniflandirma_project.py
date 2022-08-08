### Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama ###

##########################################
# İş Problemi
##########################################

#Bir oyun şirketi müşterilerinin bazı özelliklerini kullanarak
#seviye tabanlı (level based) yeni müşteri tanımları (persona)
#oluşturmak ve bu yeni müşteri tanımlarına göre segmentler
#oluşturup bu segmentlere göre yeni gelebilecek müşterilerin
#şirkete ortalama ne kadar kazandırabileceğini tahmin etmek istemektedir.

#Örneğin:
#Türkiye’den IOS kullanıcısı olan 25 yaşındaki bir erkek
#kullanıcının ortalama ne kadar kazandırabileceği belirlenmek
#isteniyor.

##########################################
# Veri Seti Hikayesi
##########################################

#Persona.csv veri seti uluslararası bir oyun şirketinin sattığı ürünlerin fiyatlarını ve bu
#ürünleri satın alan kullanıcıların bazı demografik bilgilerini barındırmaktadır. Veri
#seti her satış işleminde oluşan kayıtlardan meydana gelmektedir. Bunun anlamı
#tablo tekilleştirilmemiştir. Diğer bir ifade ile belirli demografik özelliklere sahip bir
#kullanıcı birden fazla alışveriş yapmış olabilir.

##########################################
# Değişkenler
##########################################

#PRICE      – Müşterinin harcama tutarı
#SOURCE     – Müşterinin bağlandığı cihaz türü
#SEX        – Müşterinin cinsiyeti
#COUNTRY    – Müşterinin ülkesi
#AGE        – Müşterinin yaşı

################### Uygulama Öncesi #######################

# PRICE    SOURCE   SEX     COUNTRY     AGE
#    39   android   male        bra      17
#    39   android   male        bra      17
#    49   android   male        bra      17
#    29   android   male        tur      17
#    49   android   male        tur      17

################### Uygulama Sonrası #######################

#       customers_level_based       PRICE       SEGMENT
#     BRA_ANDROID_FEMALE_0_18       35.6453           B
#     BRA_ANDROID_FEMALE_19_23      34.0773           C
#     BRA_ANDROID_FEMALE_24_30      33.8639           C
#     BRA_ANDROID_FEMALE_31_40      34.8983           B
#     BRA_ANDROID_FEMALE_41_66      36.7371           A

# Proje Görevleri #

# Soru 1: persona.csv dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.

import pandas as pd
pd.set_option("display.max_rows", None)
df = pd.read_csv(r"C:\Users\suhey\PycharmProjects\pythonProject1\Datasets\persona.csv")
df.head()
df.shape
df.info()

# Soru 2: Kaç unique SOURCE vardır? Frekansları nedir?

df.nunique()

# Soru 3: Kaç unique PRICE vardır?

df["PRICE"].nunique()

# Soru 4: Hangi PRICE'dan kaçar tane satış gerçekleşmiş?

df["PRICE"].value_counts()

# Soru 5: Hangi ülkeden kaçar tane satış olmuş?

df["COUNTRY"].value_counts()
df.groupby("COUNTRY")["PRICE"].count()
df.groupby("COUNTRY").agg({"PRICE": "count"})

# Soru 6: Ülkelere göre satışlardan toplam ne kadar kazanılmış?

df.groupby("COUNTRY")["PRICE"].sum()
df.groupby("COUNTRY").agg({"PRICE": "sum"})

# Soru 7: SOURCE türlerine göre satış sayıları nedir?

df["SOURCE"].value_counts()
df.groupby("SOURCE").agg({"PRICE": "count"})

# Soru 8: Ülkelere göre PRICE ortalamaları nedir?

df.groupby("COUNTRY")["PRICE"].mean()
df.groupby("COUNTRY").agg({"PRICE": "mean"})

# Soru 9: SOURCE'lara göre PRICE ortalamaları nedir?

df.groupby("SOURCE")["PRICE"].mean()
df.groupby("SOURCE").agg({"PRICE": "mean"})

# Soru 10: COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?

df.groupby(["COUNTRY", "SOURCE"]).agg({"PRICE": "mean"})


# Soru 11: COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?

################### Beklenen Çıktı #######################

#                                           PRICE
#       COUNTRY    SOURCE      SEX   AGE
#   0       bra   android   female    15    38.71
#   1                                 16    35.94
#   2                                 17    35.66
#   3                                 18    32.25
#   4                                 19    35.20

df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"}).head()


# Soru 12: Çıktıyı PRICE’a göre sıralayınız.

# Önceki sorudaki çıktıyı daha iyi görebilmek için sort_values metodunu azalan olacak şekilde PRICE’a göre uygulayınız.
# Çıktıyı agg_df olarak kaydediniz.

################### Beklenen Çıktı #######################

#                                           PRICE
#       COUNTRY    SOURCE      SEX   AGE
#   0       bra   android     male    46    59.0
#   1       usa   android     male    36    59.0
#   2       fra   android   female    24    59.0
#   3       usa       ios     male    32    54.0
#   4       deu   android   female    36    49.0


agg_df = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"}).sort_values("PRICE", ascending=False)

# Soru 13: Indekste yer alan isimleri değişken ismine çeviriniz.

# Üçüncü sorunun çıktısında yer alan PRICE dışındaki tüm değişkenler index isimleridir.
# Bu isimleri değişken isimlerine çeviriniz.

agg_df.head()
agg_df = agg_df.reset_index()

# Soru 14: Age değişkenini kategorik değişkene çeviriniz ve agg_df’e ekleyiniz.

# Age sayısal değişkenini kategorik değişkene çeviriniz.
# Aralıkları ikna edici şekilde oluşturunuz.
# Örneğin: ‘0_18', ‘19_23', '24_30', '31_40', '41_70'

################### Beklenen Çıktı #######################

#       COUNTRY    SOURCE      SEX   AGE   PRICE   AGE_CAT
#   0       bra   android     male    46    59.0     41_70
#   1       usa   android     male    36    59.0     31_40
#   2       fra   android   female    24    59.0     24_30
#   3       usa       ios     male    32    54.0     31_40
#   4       deu   android   female    36    49.0     31_40


#AGE değişkenimizin nerelerden bölüneceğini gösterelim.
bins = [0, 18, 23, 30, 40, agg_df["AGE"].max()]

#Bölünen noktalara karşılık isimlendirmelerin ne olacağını ifade edelim.
mylabels = ['0_18', '19_23', '24_30', '31_40', '41_' + str(agg_df["AGE"].max())]

#AGE değişkenimizi bölelim
agg_df["AGE_CAT"] = pd.cut(agg_df["AGE"], bins, labels=mylabels)
agg_df.head()

# Soru 15: Yeni seviye tabanlı müşterileri (persona) tanımlayınız.

# Yeni seviye tabanlı müşterileri (persona) tanımlayınız ve veri setine değişken olarak ekleyiniz.
# Yeni eklenecek değişkenin adı: customers_level_based
# Önceki soruda elde edeceğiniz çıktıdaki gözlemleri bir araya getirerek customers_level_based değişkenini oluşturmanız gerekmektedir.

################### Beklenen Çıktı #######################

#       CUSTOMERS_LEVEL_BASED       PRICE
#      BRA_ANDROID_MALE_41_66        59.0
#      USA_ANDROID_MALE_31_40        59.0
#    FRA_ANDROID_FEMALE_24_30        59.0
#          USA_IOS_MALE_31_40        54.0
#    DEU_ANDROID_FEMALE_31_40        49.0

#Değişkenlerimiz;
agg_df.columns

#Gözlem değerlerine erişme;
for row in agg_df.values:
    print(row)

[row[0].upper() + "_" + row[1].upper() + "_" + row[2].upper() + "_" + row[5].upper() for row in agg_df.values]


agg_df["CUSTOMERS_LEVEL_BASED"] = [row[0].upper() + "_" + row[1].upper() + "_" + row[2].upper() + "_" + row[5].upper() for row in agg_df.values]
agg_df.head()

#Gereksiz değişkenleri çıkaralım.
agg_df = agg_df[["CUSTOMERS_LEVEL_BASED", "PRICE"]]
agg_df.head()

for i in agg_df["CUSTOMERS_LEVEL_BASED"].values:
    print(i.split("_"))

# Soru 16: Yeni müşterileri (personaları) segmentlere ayırınız.

# Yeni müşterileri (Örnek: USA_ANDROID_MALE_0_18) PRICE’a göre 4 segmente ayırınız.
# Segmentleri SEGMENT isimlendirmesi ile değişken olarak agg_df’e ekleyiniz.
# Segmentleri betimleyiniz (Segmentlere göre group by yapıp price mean, max, sum’larını alınız).

agg_df.head()
agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"])
agg_df.groupby("SEGMENT").agg({"PRICE": "mean"})

# Soru 17: Yeni gelen müşterileri sınıflandırıp, ne kadar gelir getirebileceklerini tahmin ediniz.

# 33 yaşında ANDROID kullanan bir Türk kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?
# 35 yaşında IOS kullanan bir Fransız kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?

new_user = "TUR_ANDROID_FEMALE_31_40"
agg_df[agg_df["CUSTOMERS_LEVEL_BASED"] == new_user]

new_user2 = "FRA_IOS_FEMALE_31_40"
agg_df[agg_df["CUSTOMERS_LEVEL_BASED"] == new_user2]

