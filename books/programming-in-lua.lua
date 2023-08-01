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
A multile comment in Lua.
]]

-- To reactivate the code, we add a single hyphen to the first line.

-- Global variables do not need declarations.
