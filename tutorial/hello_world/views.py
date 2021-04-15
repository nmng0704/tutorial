from django.http import HttpResponse
from mlxtend.frequent_patterns import association_rules
from mlxtend.frequent_patterns import apriori
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from .connectToSql import getData
from django.shortcuts import render

def index(request):
    #get data
    dataset = getData()

    #transfer dataset into an array format with 1,0
    te = TransactionEncoder()
    te_ary = te.fit(dataset).transform(dataset)

    df = pd.DataFrame(te_ary, columns=te.columns_)

    #find frequent itemsets over the whole database
    frequent_itemsets = apriori(df, min_support=0.1, use_colnames=True)


    #filter the result, can tune the measuring values and itemsets here
    rules = association_rules(
        frequent_itemsets, metric="confidence", min_threshold=0.4)
    rules["antecedent_len"] = rules["antecedents"].apply(lambda x: len(x))
    rules = rules[(rules['consequents'] == {'Good'}) & (
        rules['antecedent_len'] >= 2)]


    
    #return render(request,"home.html",{'rules':rules})
    return HttpResponse(rules.to_html())
