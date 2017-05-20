# KMeans clustering

from src.data.explore_dataset import DataExplorer

DE = DataExplorer()
logs = DE.get_wk1_logs()

df = logs.groupby(['username','component','action','target']).size().unstack([1,2,3]).fillna(0)

from sklearn.decomposition import PCA
from sklearn.preprocessing import scale

pca = PCA()
pca.fit(df.values)
pca_df = pca.fit_transform(scale(df))

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3, random_state=123).fit(df.values)


# KMeans
for k, col in zip(range(3), colors):
    my_members = kmeans.labels_ == k
    plt.plot(pca_df[my_members, 0], pca_df[my_members, 1], 'w',
            markerfacecolor=col, marker='o')
# plt.set_title('KMeans')



def plot_pca():
    fig = plt.figure(figsize=(12, 12))
    colors = ['#4EACC5', '#FF9C34', '#4E9A06']
    fig.suptitle("PCAnime",fontsize=20 )

    i = 1

    for d1,d2 in combinations(range(6),2):
        ax = fig.add_subplot(4, 4, i)
        i+=1
    # for d1,d2 in [(0,1),(2,1),(0,2)]:
    #     ax = fig.add_subplot(2, 2, i)
    #     i+=1

        ax.set_title("PCA[{},{}]".format(d1,d1))

        mask = (FF.y.astype(int).values == 0)
        ax.plot(pca_df[mask,d1],pca_df[mask,d2],'b',
            markerfacecolor=colors[0],marker='o')
        ax.plot(pca_df[~mask,d1],pca_df[~mask,d2],'k',
            markerfacecolor=colors[1],marker='o')
    plt.show()
