class perceptron:
    def __init__(self, bits_to_index, global_history_size):
        self.bits_to_index = bits_to_index
        self.size_of_perceptrones_table = (2**bits_to_index)
        self.global_history_size = global_history_size
        self.num_weights = self.global_history_size + 1 #Including the bias 
        self.perceptrones = [[0]*(self.num_weights+1) for i in range(self.size_of_perceptrones_table)]
        self.history = [-1]*(self.global_history_size)
        self.threshold = int(1.93*(self.global_history_size) + 14)
        self.bias = 0
        self.yout = 0
        #Escriba aquí el init de la clase
        self.total_predictions = 0
        self.total_taken_pred_taken = 0
        self.total_taken_pred_not_taken = 0
        self.total_not_taken_pred_taken = 0
        self.total_not_taken_pred_not_taken = 0

        #print(self.history)
        #print(self.perceptrones)

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
        #mask = (1<<self.bits_to_index) - 1
        PC_index = int(PC) & (self.size_of_perceptrones_table - 1)
        #PC_index = int(PC) % (self.size_of_perceptrones_table-1)
        #print(PC_index)
        
        self.bias = self.perceptrones[PC_index][0]
        self.yout = self.bias
        for i in range(1,self.global_history_size+1):
            if (self.history[i-1] == 1): 
                self.yout += self.perceptrones[PC_index][i]
            else:
                self.yout -= self.perceptrones[PC_index][i]

        if (self.yout > 0):
            prediction = "T"
        else: 
            prediction = "N"
        
        return prediction
    
    def train_preceptrons(self, PC, result):
        #mask = (1<<self.bits_to_index) - 1
        PC_index = int(PC) & (self.size_of_perceptrones_table - 1)
        #PC_index = int(PC) % (self.size_of_perceptrones_table-1)
        if (result == "T"):
            t = 1
        else:
            t = -1

        for i in range(0, self.global_history_size+1):
            if (i == 0):
                self.perceptrones[PC_index][i] += t
            else:  
                if (t == self.history[i-1]):
                    self.perceptrones[PC_index][i] += 1
                else: 
                    self.perceptrones[PC_index][i] -= 1

    def update(self, PC, result, prediction):

        
        #if(result == prediction):
        #    print("No update")
        #else: print("Need update")
        #print(self.history)

        if((prediction != result) or (abs(self.yout) <= self.threshold)):
            #print("going to training")
            #print(self.yout)
            self.train_preceptrons(PC, result)

        #Update history
        #if(prediction != result):
        self.history.pop(0)
        if result == "T":
            self.history.append(1)
        else:
            self.history.append(-1)
            
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