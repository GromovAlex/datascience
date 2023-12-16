import pandas as pd
df = pd.DataFrame(
    {
        'data': [1,2,3,4,5,6,], 
        'columns': [1,2,3,4,5,6]
    }
)
df.rename(index={0:'column'}, columns = {'columns':'колонка'}, inplace = True)
print(df)

