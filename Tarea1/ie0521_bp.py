class ie0521_bp:
    def __init__(self, bits_to_index, history_size):
        #Escriba aquí el init de la clase
        self.local_history_size = int(history_size)
        self.bits_to_index = bits_to_index
        self.size_of_branch_table = 2**bits_to_index
        self.branch_table = [[0]*self.local_history_size for i in range(self.size_of_branch_table)]
        self.global_history_size = int(history_size/2)
        self.global_history_reg = [0]*(self.global_history_size)
        self.total_predictions = 0
        self.total_taken_pred_taken = 0
        self.total_taken_pred_not_taken = 0
        self.total_not_taken_pred_taken = 0
        self.total_not_taken_pred_not_taken = 0

        #print(self.branch_table)

    def print_info(self):
        print("Parámetros del predictor:")
        print("\tTipo de predictor:\t\t\tNombre de su predictor")

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
        PC_index = int(PC) % self.size_of_branch_table
        n_counter = 0
        t_counter = 0
        for i in range(0, self.local_history_size):
            if self.branch_table[PC_index][i] == 0:
                n_counter += 1
            else: 
                t_counter += 1

        n_counter_g = 0
        t_counter_g = 0
        for i in range(0, self.global_history_size):
            if self.global_history_reg[i] == 0:
                n_counter_g += 1
            else: 
                t_counter_g += 1
        if (t_counter_g > n_counter_g):
            t_counter += t_counter_g

        if (n_counter >= t_counter):
            return "N"
        else: 
            return "T"
  

    def update(self, PC, result, prediction):
        PC_index = int(PC) % self.size_of_branch_table

        #print(self.branch_table[PC_index])
        self.branch_table[PC_index].pop(0)
        self.global_history_reg.pop(0)
        if result == "T": 
            #print("Take")
            self.branch_table[PC_index].append(1)
            self.global_history_reg.append(1)
            
            
        else: 
            #print("No Take")
            self.branch_table[PC_index].append(0)
            self.global_history_reg.append(0)
            
        #print(self.branch_table[PC_index])
        #print(self.global_history_reg)

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
