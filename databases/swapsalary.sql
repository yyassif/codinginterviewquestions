# Myungho Sim
#swap sex variable's value from m to f and f to m
#solution using case when then
update salary 
set sex = case
when sex='f' then 'm'
when sex='m' then 'f'
end
