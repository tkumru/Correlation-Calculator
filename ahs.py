import pandas as pd
import numpy as np

class AHS:
    def __init__(self, dataframe):
        self.dataframe = dataframe
        self.size = len(self.dataframe) 

        self.controlDataframe = self.control_DivideTotal(dataframe=self.dataframe, total=self.control_dataframe(self.dataframe), size=self.size)
        self.control = self.control_DivideTotal(dataframe=self.dataframe, total=self.control_dataframe(self.dataframe), size=self.size)

    def control_dataframe(self, dataframe):
        return [np.sum(x) for x in dataframe[:].values]

    def control_DivideTotal(self, dataframe, total, size):
        control = pd.DataFrame()
        for x in range(size):
            for y in range(size):
                control.at[y, x] = dataframe.at[y, x] / total[x]

        return control

    def control_isEqualOne(self, control, size):
        result =list()
        for count in range(size):
            result.append(np.sum(control[count]))
        return result

    def add_mean(self, dataframe):
        dataframe[self.size] = dataframe.mean(axis=1)
        return dataframe, dataframe[self.size]

if __name__ == '__main__':
    base_dataframe = pd.read_excel("data.xlsx", header=None)

    ahs = AHS(base_dataframe)
    df = ahs.controlDataframe
    df_mean, mean = ahs.add_mean(df)

    weight = np.dot(ahs.control, mean)
    weight = weight.reshape(ahs.size, 1)

    base_dataframe["Weight"] = weight
    base_dataframe.to_excel("weight.xlsx")
