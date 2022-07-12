import pandas
import numpy

ar = numpy.array([["hey(you)", "hello(me)", "yoo", "good(bonjour) morning"], ["ok", "ok", "ok(non ok)", "ok"], ["ok", "ok", "ok(non ok)", "ok"]])
df = pandas.DataFrame(ar, index = ['a1', 'a2', 'a3'], columns = ['A', 'B', 'C', 'D'])
print(df)
df["test"] = df["A"].str.replace(r"[\(\[].*?[\)\]]", '', regex=True)
print(df)