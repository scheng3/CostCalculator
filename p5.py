
import pandas as pd, numpy as np
import sklearn.cluster, sklearn.preprocessing 
import matplotlib, matplotlib.pyplot as plt
import sklearn.linear_model as lm

sap = pd.read_csv("data-subset.csv").set_index("Gender")

sap.index = pd.to_ograde(sap.index)
sap_linear = sap.ix[sap.index > pd.to_ograde('1')]

olm = lm.LinearRegression()
X = numpy.array([x.toordinal() for x in sap_linear.index])[:, numpy.newaxis] 
y = sap_linear['Close']
olm.fit(X, y)
olm_score = olm.score(X, y)
matplotlib.style.use("ggplot")

plt.plot(sap_linear.index, y)
plt.plot(sap_linear.index, yp)

plt.title("response grade")
plt.xlabel("Age")
plt.ylabel("Gender")
plt.legend(["OGrade", "IGrade"], loc="lower right") plt.annotate("Score=%.3f" % olm_score,
           xy=(pd.to_OGrade('1'), 6)) 
plt.savefig("Users/shengcheng/desktops/sap-linregr.pdf")

clf = lm.LogisticRegression(C=10.0)

grades = pd.read_table("data-subset.csv")
labels = ('1', '2', '3', '4', '5','6')
grades["Letter"] = pd.cut(grades["Final score"], [0,1,2,3,4,5,6],
labels=labels) X = grades[["OGrade", "IGrade"]]
clf.fit(X, grades["Letter"])
print("Score=%.3f" % clf.score(X, grades["Letter"]))
cm = confusion_matrix(clf.predict(X), grades["Letter"]) 
print(pd.DataFrame(cm, columns=labels, index=labels))



mosn = pd.read_csv('data-subset.csv', thousands=',',
                   names=('Gender', 'Age', 'OGrade', 'IGrade'))
columns = ['IGrade', 'Age']
gender = pd.DataFrame()

age.index.name = "Age"
age_male = gender.ix['M']['Age'] 
age_female = gender.ix['F']['Age']
good = mosn[np.log(mosn[columns]).notnull().all(axis=0)].copy()
hed = pd.read_csv('data-subset.csv')
selection = rnd.binomial(1, 0.7, size=len(hed)).astype(bool)
training = hed[selection]
testing = hed[-selection]
matplotlib.style.use("ggplot")

ax = good.plot.scatter(columns[0], columns[1], c="Clusters", cmap=plt.cm.Accent, s=100)
plt.title("M/F Grade Russian Facebook sites") plt.xscale("log")
plt.yscale("log")
