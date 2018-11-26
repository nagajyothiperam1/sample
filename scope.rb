MR_COUNT = 0        
module Foo
   MR_COUNT = 0
   ::MR_COUNT = 1    
   MR_COUNT = 2      
end
puts MR_COUNT        
puts Foo::MR_COUNT  