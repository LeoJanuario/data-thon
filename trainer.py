import numpy as np
from sklearn.cluster import KMeans

def rank_prospects(valid_prospects, all_features):
    """
    Recebe lista de prospects e features, retorna prospects ordenados por distância do cluster.
    """
    if len(valid_prospects) > 1 and len(set(map(tuple, all_features))) > 1:
        all_features = np.array(all_features)
        kmeans = KMeans(n_clusters=2, random_state=42, n_init=10)
        labels = kmeans.fit_predict(all_features)

        distances = [
            kmeans.transform([feat])[0][label]
            for feat, label in zip(all_features, labels)
        ]
        return [p for _, p in sorted(zip(distances, valid_prospects), key=lambda x: x[0])]
    return valid_prospects
