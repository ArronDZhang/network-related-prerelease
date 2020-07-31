deepwalk --format mat --input example_graphs/new_USAir.mat --max-memory-data-size 0 --number-walks 80 --representation-size 128 --walk-length 40 --window-size 10 --workers 1 --output example_graphs/USAir.embeddings

deepwalk --format mat --input example_graphs/new_PB.mat --max-memory-data-size 0 --number-walks 80 --representation-size 128 --walk-length 40 --window-size 10 --workers 1 --output example_graphs/PB.embeddings

deepwalk --format mat --input example_graphs/new_NS.mat --max-memory-data-size 0 --number-walks 80 --representation-size 128 --walk-length 40 --window-size 10 --workers 1 --output example_graphs/NS.embeddings

deepwalk --format mat --input example_graphs/new_Power.mat --max-memory-data-size 0 --number-walks 80 --representation-size 128 --walk-length 40 --window-size 10 --workers 1 --output example_graphs/Power.embeddings

deepwalk --format mat --input example_graphs/new_Router.mat --max-memory-data-size 0 --number-walks 80 --representation-size 128 --walk-length 40 --window-size 10 --workers 1 --output example_graphs/Router.embeddings

deepwalk --format mat --input example_graphs/new_Yeast.mat --max-memory-data-size 0 --number-walks 80 --representation-size 128 --walk-length 40 --window-size 10 --workers 1 --output example_graphs/Yeast.embeddings

deepwalk --format mat --input example_graphs/new_Celegans.mat --max-memory-data-size 0 --number-walks 80 --representation-size 128 --walk-length 40 --window-size 10 --workers 1 --output example_graphs/Celegans.embeddings

deepwalk --format mat --input example_graphs/new_Ecoli.mat --max-memory-data-size 0 --number-walks 80 --representation-size 128 --walk-length 40 --window-size 10 --workers 1 --output example_graphs/Ecoli.embeddings
