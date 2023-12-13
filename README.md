<img src="images/DOC4TF.png" width="100" height="100" style="float: right;">

Ideally, a comprehensive documentation set should be created as part of developing a Text-Fabric dataset. However, in practice, this is not always completed during the initial phase or after changes to features. This [Jupyter Notebook](https://github.com/tonyjurg/Doc4TF/blob/main/CreateFeatureDoc.ipynb) contains Python code to automatically generate (and thus ensure consistency) a documentation set for any Text-Fabric dataset. It serves as a robust starting point for the development of a brand new documentation set or as validation for an existing one. One major advantage is that the resulting documentation set is fully hyperlinked, a task that can be laborious if done manually.

The main steps in producing the documentation set are:
* Load a Text-Fabric database
* Execute the code pressent in the subsequent cells. The code will:
   * Construct a few python dictionaries with relevant data from the TF datase.
   * Create separate files for each feature.
   * Create an overview page of all featers per node type.

An example documentation set created by this script is found at the [results directory](https://github.com/tonyjurg/Doc4TF/blob/main/results/featurebynodetype.md). 

# About Text-Fabric

Text-Fabric is a powerful Python library and framework designed to facilitate the analysis and manipulation of large-scale textual data, particularly in the context of ancient languages and biblical texts. It provides a comprehensive set of tools for processing and querying structured text data efficiently. Text-Fabric was developed by [Dirk Roorda](https://github.com/dirkroorda). The software package is accessible at [https://github.com/annotation/text-fabric](https://github.com/annotation/text-fabric).
