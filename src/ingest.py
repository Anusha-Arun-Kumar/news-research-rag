import pandas as pd

data_path = "/Users/anushakumar/Documents/news-research-rag/data/News_Category_Dataset_v3.json"

def load_data(data):

    print("Loading Data..")
    df = pd.read_json(data, lines = True)
    print("Original Dataset Size: ", len(df))
    print(df.head(10))
    df = df[['headline', 'short_description', 'category']]

    df = df.dropna()

    df['text'] = df['headline'] + ". " + df['short_description']

    print("Cleaned dataset size:", len(df))


    return df

def show_sample(df):
    print("\nExample article:\n")
    print(df.iloc[0]['text'])
    print("\nCategory:", df.iloc[0]['category'])

if __name__ == "__main__":
    df = load_data(data_path)
    show_sample(df)



