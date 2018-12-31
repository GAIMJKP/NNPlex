import numpy

class CategoryNeuron:
    
    def __init__(self, num_categories, cat_periodicity):
        self.num_categories = num_categories
        self.cat_periodicity = cat_periodicity
        pass 

    def z_to_class(self, z):
        angle = numpy.mod(numpy.angle(z) + 2*numpy.pi, 2 * numpy.pi)
        intermediate = int(numpy.floor(self.num_categories * self.cat_periodicity * angle) / (2*numpy.pi))
        return numpy.mod(intermediate, self.num_categories)

    def category_to_bisectors(self, category):
        return (category + 0.5 + (self.num_categories * numpy.arange(self.cat_periodicity))) / (self.num_categories * self.cat_periodicity) * (2*numpy.pi)
                  
 

#TESTING               
#neuron = CategoryNeuron(4,1)

#similar class
#vpi6 = complex(numpy.sqrt(3)/2, 1/2)
#vpi4 = complex(numpy.sqrt(2)/2, numpy.sqrt(2)/2)
#vpi3 = complex(1/2, numpy.sqrt(3)/2)
#vpi2 = complex(0,1)

#print(neuron.z_to_class(vpi3))
#print(neuron.z_to_class(vpi4))
#print(neuron.z_to_class(vpi6))
#print(neuron.z_to_class(vpi2))

#similar class
#v2pi3 = complex(-1/2, numpy.sqrt(3)/2)
#v3pi4 = complex(-(numpy.sqrt(2)/2), numpy.sqrt(2)/2)
#v5pi6 = complex(-(numpy.sqrt(3)/2), 1/2)
#vpi = complex(-1,0)

#print(neuron.z_to_class(v2pi3))
#print(neuron.z_to_class(v3pi4))
#print(neuron.z_to_class(v5pi6))
#print(neuron.z_to_class(vpi))

#print(neuron.category_to_bisectors(0))