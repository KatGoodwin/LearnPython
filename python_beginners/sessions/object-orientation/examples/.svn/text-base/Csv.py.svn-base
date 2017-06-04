class Csv(object):
    def __init__(self, filename, *args, **kwargs):
        csv = open(filename)
        self.data = self._load_csv(csv)
        csv.close()
            
    
    def show_csv(self):
        for line in self.data:
            print line
            
    def _load_csv(self, csv):
        data = []
        lines = csv.readlines()    
        if len(lines)<2:
            raise CsvError, "Empty csv file: " + csv.filename
            return
        titles = lines.pop(0).replace('"', '').split(',')
    
        for line in lines:
            item = line.split(',')
            #check for badly formed csv lines        
            dict an= {}
            for num in range(len(titles)):
                dict[titles[num]] = item[num]
            data.append(dict)
        return data
        
    #list comprehension version    
    def get_average_age(self):    
        total =0
        for item in self.data:
            total += int(item['Age'])
        return total/len(self.data)
        
    def get_oldest(self):
        ages = []
        for item in self.data:
            ages.append(int(item['Age']))
        return max(ages)
    
    
    
if __name__ == '__main__':    

    actors = Csv('actors.csv')
    cartoons = Csv('cartoons.csv')
    
    print "==Actors=="
    print "= showing csv ="
    print actors.show_csv()
    print "= getting oldest ="
    print actors.get_oldest()
    print "= getting average age ="
    print actors.get_average_age()
    print "= getting directly at data ="
    
    print"==Cartoons=="
    print "= showing csv ="
    print cartoons.show_csv()
    print "= getting oldest ="
    print cartoons.get_oldest()
    print "= getting average age ="
    print cartoons.get_average_age()
