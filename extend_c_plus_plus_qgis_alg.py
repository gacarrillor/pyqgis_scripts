# How to extend "native:printlayouttopdf" algorithm with extra parameters and custom logic.
#
# By default, C++ child algorithms are not exposed as Python classes. That's why we cannot subclass them directly.
# Nonetheless, there are some C++ algorithms exposed as Python classes for Python devs to extend them. 
#    For instance: QgsBatchGeocodeAlgorithm or QgsProcessingFeatureBasedAlgorithm.
#
# For extending "native:printlayouttopdf", we could grab its input/output params and pass them to our new SubAlgorithm,
# as well as other properties (e.g., flags).
# We should in any case overwrite its processAlgorithm() method, which contains the main logic.

alg = QgsApplication.processingRegistry().algorithmById("native:printlayouttopdf")


class SubAlg(QgsProcessingAlgorithm):
  
    def __init__(self, base_alg=None, extra_params=[]):
        QgsProcessingAlgorithm.__init__(self)
        self.__base_alg = base_alg
        self.__extra_params = extra_params
        
    def createInstance(self):
        return SubAlg(self.__base_alg, self.__extra_params)
    
    def name(self):
        return "My own SubAlgorithm"
    
    def flags(self):
        return self.__base_alg.flags()
    
    def initAlgorithm(self, config):
        if self.__base_alg:
            for p in self.__base_alg.parameterDefinitions():
                self.addParameter(p.clone(), p.name() == 'OUTPUT')
            
        for p in self.__extra_params:
            self.addParameter(p.clone())

    #def processAlgorithm(self, parameters, context, feedback):
    #    pass
            
            
subalg = SubAlg(alg, [])
print(subalg.canExecute())

# Check flags:
#   bool(subalg.flags() & QgsProcessingAlgorithm.FlagNoThreading)
#   bool(subalg.flags() & QgsProcessingAlgorithm.FlagRequiresProject)
#
# Show me the alg's dialog: processing.execAlgorithmDialog(subalg)
#
# Depending on your use case, you might need to call the following line to get parameters initialized:
# subalg.initAlgorithm(None)
# However, that's not required for commands like execAlgorithmDialog().

