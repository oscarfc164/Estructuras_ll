class perceptron:
    def __init__(self, bits_to_index, global_history_size):
        self.bits_to_index = bits_to_index
        self.size_of_branch_table = 2**bits_to_index
        self.global_history_size = global_history_size
        self.max_index_global_history = 2**self.global_history_size
        self.num_preceptrons = 2**(bits_to_index+global_history_size)
        self.weights = [[0]*(self.global_history_size+1) for i in range(self.num_preceptrons)]
        self.history = [0]*self.global_history_size
        self.threshold = int(1.93*(self.global_history_size) + 14)
        self.bias = 0
        #Escriba aquí el init de la clase
        self.total_predictions = 0
        self.total_taken_pred_taken = 0
        self.total_taken_pred_not_taken = 0
        self.total_not_taken_pred_taken = 0
        self.total_not_taken_pred_not_taken = 0

        print(len(self.weights))

    def print_info(self):
        print("Parámetros del predictor:")
        print("\tTipo de predictor:\t\t\tPerceptron")

    def print_stats(self):
        print("Resultados de la simulación")
        print("\t# branches:\t\t\t\t\t\t"+str(self.total_predictions))
        print("\t# branches tomados predichos correctamente:\t\t"+str(self.total_taken_pred_taken))
        print("\t# branches tomados predichos incorrectamente:\t\t"+str(self.total_taken_pred_not_taken))
        print("\t# branches no tomados predichos correctamente:\t\t"+str(self.total_not_taken_pred_not_taken))
        print("\t# branches no tomados predichos incorrectamente:\t"+str(self.total_not_taken_pred_taken))
        perc_correct = 100*(self.total_taken_pred_taken+self.total_not_taken_pred_not_taken)/self.total_predictions
        formatted_perc = "{:.3f}".format(perc_correct)
        print("\t% predicciones correctas:\t\t\t\t"+str(formatted_perc)+"%")

    def predict(self, PC):
        PC_index = int(PC) % self.num_preceptrons
        #print(PC_index)
        
        self.bias = self.weights[PC_index][0]
        for i in range(0, self.global_history_size):
            self.bias += self.history[i]*self.weights[PC_index][i]

        if (self.bias >= 0):
            
            prediction = "T"
        else: 
            prediction = "N"

        return prediction
    
    def train_preceptrons(self, PC, result):
        PC_index = int(PC) % self.num_preceptrons
        for i in range(0, self.global_history_size):
            if (result == "T"):
                self.weights[PC_index][i] += self.history[i]
            else: 
                self.weights[PC_index][i] -= self.history[i]


    def update(self, PC, result, prediction):
        PC_index = int(PC) % self.num_preceptrons

        if((prediction != result) or (abs(self.bias) <= self.threshold)):
            self.train_preceptrons(PC, result)

            #Update history
            self.history.pop(0)
            if(result == "T"):
                self.history.append(1)
            else: 
                self.history.append(0)
        #Update stats
        if result == "T" and result == prediction:
            self.total_taken_pred_taken += 1
        elif result == "T" and result != prediction:
            self.total_taken_pred_not_taken += 1
        elif result == "N" and result == prediction:
            self.total_not_taken_pred_not_taken += 1
        else:
            self.total_not_taken_pred_taken += 1

        self.total_predictions += 1