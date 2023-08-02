--[[
Chapter 1. Getting started
]]

--[[
print("Hello world!")
--]]

-- Defines a factorial function

--[[
function fact (n)
  if n == 0 then
    return 1
  else
    return n * fact(n - 1)
  end
end

print("Enter a number:")
a = io.read("*n")
print(fact(a))

--]]


-- A chunk of code in Lua is basically a snippet of code. It should be enclosed
-- in ().

-- Invoke Lua command prompt
-- lua
-- Exit using CTRL-C or with os.exit()

-- -i option instructs Lua to start an interactive session after running a given
-- chunk.
-- > lua -i prog.lua

-- dofile() loads a script.
-- > dofile("lib1.lua")
-- > n = functionInFile(43)

-- Avoid identifiers starting with an underscore such as _VERSION.

-- A comment in Lua.

--[[
-- A multile comment in Lua.
--]]

-- To reactivate the code, we add a single hyphen to the first line.

-- Global variables do not need declarations.

-- The function type gives the type of any given value:
-- type(true) --> boolean

--[[
type(true) --> boolean
--]]

-- We can assign nil to a global variable to delete it!

-- x = x or v is equivalent to: 
-- if not x then x = v end

--[[
Chapter 1. Exercises
]]

-- Exercise 1.1: Run the factorial example. What happens to your program if you
-- enter a negative number?
-- Modify the example to avoid this problem.

--[[
-- A negative number results in a stack traceback error.
-- We can easily fix this error restricting the value of n.
function fact (n)
  if n <= 0 then -- n must be greater than or equal to 0 
    return 1
  else
    return n * fact(n - 1)
  end
end

print("Enter a number:")
a = io.read("*n")
print(fact(a))
--]]

-- Exercise 1.2: Run the twice example, both by loading the file with the -l
-- option and with dofile. Which way do you prefer?

-- [[
-- I prefer the dofile option
-- ]]

-- Exercise 1.3: Can you name other languages that use "--" for comments?

--[[
-- I do not know of any other language that use "--" for comments.
-- A quick search shows up Ada, Applescript, Eiffel, Haskell, SQL and VHDL.
--]]

-- Exercise 1.4: Which of the following strings are valid identifiers?

--[[
  ___
  _end
  End
  nil
  NULL

--]]

-- Exercise 1.5: What is the value of the expression type(nil) == nil

--[[
print(type(nil) == nil) --> false
--]]

-- Exercise 1.6: How can you check whether a value is a Boolean without using
-- the function type?

--[[
-- I would do:
local value = true
print(value == true)
--]]

-- Exercise 1.7: Are the parentheses necessary? Would you recommend their use in
-- that expression?

--[[
-- I would, since it improves readability.
--]]

-- Exercise 1.8: Write a simple script that prints its own name without knowing
-- it in advance.

--[[
print(arg[0]) -- No text formatting due to experience.
--]]

--[[
Chapter 2. Interlude: The Eight-Queen Puzzle
]]

