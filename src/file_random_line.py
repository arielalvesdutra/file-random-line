import random

class FileRandomLine:
    
    def __init__(self, parameter_file):
        self._validate_file(parameter_file)
        
        self.file = parameter_file
        
    def get_file_random_line(self):
        opened_file_values = self._get_file_values()
        random_index = random.randrange(0, len(opened_file_values))
        return opened_file_values[random_index]
    
    def _get_file_values(self):
        file_values = []
        for line in self.file:
            file_values.append(line.rstrip())
            
        return file_values
    
    def _validate_file(self, file_to_validate):        
        if (len(file_to_validate.read()) == 0):
            file_to_validate.close()
            raise Exception("O arquivo fornecido está vazio.")
    
        file_to_validate.seek(0)
