from PySparkTools.Visualization.PyPlots import plt_confusion_matrix

y_true = ["cat", "ant", "cat", "cat", "ant", "bird"]
y_pred = ["ant", "ant", "cat", "cat", "ant", "cat"]


class_names = ["ant", "bird", "cat"]

cnf_matrix = plt_confusion_matrix(y_true, y_pred, class_names)
