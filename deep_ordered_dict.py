from collections import OrderedDict
"""customization of the class collections.OrderedDict.
changes:
    --self.__contains__() performs a deep (only for nested DeepOrderedDict)
    search for the key up to the given depth.
    --self.move_to_end() now moves nested (DeepOderedDict) items to the end.
    The deepest level gets moved to the end most position.
new methods:
    --self.get_end(), returns the end most items down to the given level depth.

"""
class DeepOrderedDict(OrderedDict):
    def __lt__(self, other, cmp_max=False, by_key=False):
        if by_key:
            item = self.keys()
        else:
            item = self.values()
            
        if cmp_max:
            return max(item) < other
        else:
            return min(item) < other

    def __gt__(self, other, cmp_max=False, by_key=False):
        if by_key:
            item = self.keys()
        else:
            item = self.values()
            
        if cmp_max:
            return max(item) > other
        else:
            return min(item) > other



    def __contains__(self, target, by_key=True, depth=-1):
        """Search for target in self.keys() or self.values()
        up to 'depth' level deep.
        
        Parameters
        ----------
        by_key: bool
            if true, search for target in the keys.
            if false, search for target in the values
        depth: int
            if depth == 0, only search the current dict.
            if depth > 0, search 'depth' level deep.
            if depth < 0, search to the deepest level.
        """
        if by_key:
            items = self.keys()
        else:
            items = self.values()
        if depth != 0:
            for value in self.values():
                try:
                    if value.__contains__(target,by_key,depth-1):
                        return True
                except(TypeError,AttributeError) as e:
                    pass
        return target in items
    

    def move_to_end(self,key,last=True,depth=-1):
        """Move (key,value) to the end position recursively
        to 'depth' level deep.
        if there are more than one same key (in different nested levels),
        the deepest one are moved to the end most position.
        
        Parameters
        ----------
        key: str
            the key of the (key,value) pair to move.
        last: bool
            if true, move to last, else move to first.
        depth: int
            if depth == 0, only move item in the top level of the current dict.
            if depth > 0, move 'depth' level deep.
            if depth < 0, move down to the deepest level.
            
        Notes
        -----
        I got some <RuntimeError: OrderedDict mutated during iteration> earlier
        but can't replicate them anymore.
        So I assume it has to do with the particular nested instance 
        that I used to test the function with.
        """
        moved = False
        try:
            OrderedDict.move_to_end(self,key,last)
            moved = True
        except KeyError:
            pass
        if depth != 0:
            for i in self:
                try:
                    if key in self[i]:
                        self[i].move_to_end(key,last,depth-1)
                        OrderedDict.move_to_end(self,i,last)
                        moved = True                    
                except (TypeError,AttributeError) as e:
                    pass
        if not moved:
            raise KeyError(key)
    
    def get_end(self,what='key',last=True,depth=-1):
        
        if last:
            idx = -1
        else:
            idx = 0
        
        end_key = list(self.keys())[idx]
        
        item = False
        if depth != 0:
            try:
                item = self[end_key].get_end(what,last,depth-1)
            except AttributeError:
                pass
        if not item:
            if what.lower() == 'key':
                item = end_key
            elif what.lower() == 'value':
                item = self[end_key]
            elif what.lower() == 'item':
                item = (end_key,self[end_key])
            else:
                raise ValueError(what+'. The \'what\' keyword argument must be one of \'key\', \'value\', or \'item\'.')
        return item
            
                
        

if __name__ == '__main__':
    a = DeepOrderedDict([('a',1)])
    b = DeepOrderedDict([('b',10)])
    c = DeepOrderedDict([('c',100),('d',200)])
    a['b'] = b.copy()
    a['b']['c'] = c.copy()
