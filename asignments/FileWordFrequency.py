
# coding: utf-8

#question 2

class WordFrequency(object):
    """
    Analyses files to genrate a dictionary that has words and their frequencies
    """
    
    def __init__(self):
        self.freq_dict = {}
        self.special_character = ",./;<>?:{}[]\1234567890!@#%^&*()-_=+"
    

    def getFreq(self,key):
        """Input the word you want to check for"""
        
        if key in self.freq_dict:
            return self.freq_dict[key] 
        else:
            return(False)
    

    def analyzeFile(self, filename):
        """
        After initialization this method of class analyzes the file given in argument
        
        Keyword arguments:
        filename : file you want to analyze
        """
        
        self.freq_dict = {}
        file_obj = open(filename,'r')
        all_lines = file_obj.readlines()
        for line in all_lines:
            clean_line = self._clean(line)
            words = clean_line.split(' ')
            for word in words:
                if word in self.freq_dict: self.freq_dict[word] += 1
                else: self.freq_dict[word] = 1
    

    def _clean(self, string):
        """Cleans string from special characters and punctuations"""
        
        string = string.replace("\n",'')
        string = string.lower()
        for character in self.special_character: string = string.replace(character,'')
        return string
        

if __name__=="__main__":

    calculator = WordFrequency()
    calculator.analyzeFile("test_file.txt")
    print(calculator.getFreq(input("Enter the word for its frequency : ")))
    



