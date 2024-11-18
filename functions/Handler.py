def Handler(handlers):

    def handler(msg):

        try:

            handler_ = handlers().index(msg)
        
            return True

        except:

            return False
    
    return handler
